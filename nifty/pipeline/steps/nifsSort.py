#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MIT License

# Copyright (c) 2015, 2017 Marie Lemoine-Busserolle

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

################################################################################
#                Import some useful Python utilities/modules                   #
################################################################################

# STDLIB

from xml.dom.minidom import parseString
import urllib
from pyraf import iraf
import astropy.io.fits
import os, sys, shutil, glob, math, logging, pkg_resources, time, datetime, re
import numpy as np
# Import config parsing.
from ..configobj.configobj import ConfigObj

# LOCAL

# Import custom Nifty functions.
# TODO(nat): goodness, this is a lot of functions. It would be nice to split this up somehow.
from ..nifsUtils import getUrlFiles, getFitsHeader, FitsKeyEntry, stripString, stripNumber, \
datefmt, checkOverCopy, checkQAPIreq, checkDate, writeList, checkEntry, timeCalc, checkSameLengthFlatLists, \
rewriteSciImageList, datefmt

# Import NDMapper gemini data download, by James E.H. Turner.
from ..downloadFromGeminiPublicArchive import download_query_gemini

# Define constants
# Paths to Nifty data.
RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')


def start():
    """
    nifsSort

    This module contains all the functions needed to copy and sort
    the NIFS raw data, where the data is located in a local directory.

    INPUT FILES:
    + rawPath files
      - Science frames
      - Calibration frames
      - Telluric frames
      - Acquisition frames (optional, but if data is copied from archive
        then acquisition frames will be copied and sorted)

    OUTPUT:
      - Sorted data
      - Lists of paths to the calibrations, science and telluric frames
      - Names of frames stored in text files for later use by the pipeline

    If -c True or a program or date is specified with -p or -d data will be copied from
    Gemini North internal network (used ONLY within Gemini).

    Args:
        rawPath (string):   Local path to raw files directory. Specified with -q at command line.
        over (boolean): If True old files will be overwritten during data reduction. Specified
                        with -o at command line. Default: False.
        program (string): OT observation id (used only within Gemini network). Specified with
                          -p at command line. "GN-2013B-Q-109".

    TODO(nat): add a way to open .tar.bz gemini public archive data, unzip it, and verify the md5 of
               each.

    """

    # Store current working directory for later use.
    path = os.getcwd()

    # Format logging options.
    FORMAT = '%(asctime)s %(message)s'
    DATEFMT = datefmt()

    """# Set up the logging file.
    logging.basicConfig(filename='Nifty.log',format=FORMAT,datefmt=DATEFMT,level=logging.DEBUG)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # This lets us logging.info(to stdout AND a logfile. Cool, huh?
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)"""

    # Set up the logging file.
    log = os.getcwd()+'/Nifty.log'

    logging.info('\n####################################')
    logging.info('#                                  #')
    logging.info('#  Start NIFS sorting and copying  #')
    logging.info('#                                  #')
    logging.info('####################################\n')

    # Load reduction parameters from runtimeData/config.cfg.
    with open('./config.cfg') as config_file:
        options = ConfigObj(config_file, unrepr=True)
        # Read general config.
        over = options['over']
        manualMode = options['manualMode']
        # Read sort specific config.
        sortConfig = options['sortConfig']
        rawPath = sortConfig['rawPath']
        program = sortConfig['program']
        proprietaryCookie = sortConfig['proprietaryCookie']
        skyThreshold = sortConfig['skyThreshold']
        sortTellurics = sortConfig['sortTellurics']
        telluricTimeThreshold = sortConfig['telluricTimeThreshold']

    # Check for invalid command line input. Cannot both copy from Gemini and sort local files.
    # Exit if -q <path to raw frame files> and -c True are specified at command line (cannot copy from
    # Gemini North internal network AND use local raw data).
    if rawPath and program:
        logging.info("\nError in sort: both a local path and a Gemini program ID (to download from Gemini Public Archive) were provided.\n")
        raise SystemExit

    # Download data from gemini public archive to ./rawData/.
    if program:
        url = 'https://archive.gemini.edu/download/'+ str(program) + '/notengineering/NotFail/present/canonical'
        if not os.path.exists('./rawData'):
            os.mkdir('./rawData')
        logging.info('\nDownloading data from Gemini public archive to ./rawData. This will take a few minutes.')
        logging.info('\nURL used for the download: \n' + str(url))
        if proprietaryCookie:
            download_query_gemini(url, './rawData', proprietaryCookie)
        else:
            download_query_gemini(url, './rawData')
        rawPath = os.getcwd()+'/rawData'


    ############################################################################
    ############################################################################
    #                                                                          #
    #              CASE 1: NIFS RAW DATA in local directory                    #
    #                                                                          #
    #    These conditions are used when a local path to raw files              #
    #    is specified with -q at command line.                                 #
    #                                                                          #
    #                                                                          #
    ############################################################################
    ############################################################################


    # IF a local raw directory path is provided, sort data.
    if rawPath:
        if manualMode:
            a = raw_input("About to enter makePythonLists().")
        allfilelist, arclist, arcdarklist, flatlist, flatdarklist, ronchilist, objectDateGratingList, skyFrameList, telskyFrameList, obsidDateList, sciImageList = makePythonLists(rawPath, skyThreshold)
        if manualMode:
            a = raw_input("About to enter sortScienceAndTelluric().")
        objDirList, scienceDirectoryList, telluricDirectoryList = sortScienceAndTelluric(allfilelist, skyFrameList, telskyFrameList, sciImageList, rawPath)
        if manualMode:
            a = raw_input("About to enter sortCalibrations().")
        calibrationDirectoryList = sortCalibrations(arcdarklist, arclist, flatlist, flatdarklist, ronchilist, objectDateGratingList, objDirList, obsidDateList, sciImageList, rawPath, manualMode)
        # If a telluric reduction will be performed sort the science and telluric images based on time between observations.
        # This will NOT be executed if -t False is specified at command line.
        if sortTellurics:
            if manualMode:
                a = raw_input("About to enter matchTellurics().")
            matchTellurics(telluricDirectoryList, scienceDirectoryList, telluricTimeThreshold)

    # Exit if no or incorrectly formatted input is given.
    else:
        logging.info("\nERROR in sort: Enter a program ID, observation date, or directory where the raw files are located.\n")
        raise SystemExit

    ############################################################################
    ############################################################################
    #                                                                          #
    #               CASE 2: NIFS RAW DATA in GEMINI PRIVATE NETWORT            #
    #                                                                          #
    #     These conditions are used if a program, date or copy is specified    #
    #     with -p, -d or -c True at command line. Files can be copied from     #
    #     Gemini North internal network and sorted.                            #
    #                                                                          #
    #                                                                          #
    ############################################################################
    ############################################################################

    """# TODO(nat): implement private gemini archive downloads.
    elif copy or program or date:
        try:
            import gemini_sort
        except ImportError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: gemini_sort.py module is needed to find NIFS data")
            logging.info("                      within the Gemini Internal Network. This option")
            logging.info("                      is only available when the pipeline is run at")
            logging.info("                      the observatory.")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")
            raise SystemExit
        else:
            gemini_sort.start(over, copy, program, date)"""


    os.chdir(path)

    # Update runtimeData/config.cfg with the paths to each:
    # 1) Science observation directory
    # 2) Calibration observation directory
    # 3) Telluric observation directory
    logging.info("\nnifsSort: writing scienceDirectoryList, calibrationDirectoryList and telluricDirectoryList in ./config.cfg.")
    with open('./config.cfg') as config_file:
        options = ConfigObj(config_file, unrepr=True)
    options['scienceDirectoryList'] = scienceDirectoryList
    options['telluricDirectoryList'] = telluricDirectoryList
    options['calibrationDirectoryList'] = calibrationDirectoryList
    with open('./config.cfg', 'w') as config_file:
        options.write(config_file)

##################################################################################################################
#                                                                                                                #
#                                                   FUNCTIONS                                                    #
#                                                                                                                #
##################################################################################################################

def makePythonLists(rawPath, skyThreshold):

    """Creates python lists of file names by type. No directories are created and no
    files are copied in this step."""

    allfilelist = [] # List of tellurics, science frames, aquisitions... But not calibrations!
    flatlist = [] # List of lamps on flat frames.
    flatdarklist = [] # List of lamps off flat frames.
    ronchilist = [] # List of ronchi flat frames.
    arclist = [] # List of arc frames.
    arcdarklist = [] # List of arc dark frames.

    objectDateGratingList = [] # 2D list of object (science or telluric) name, date pairs.

    skyFrameList = [] # List of sky frames.
    telskyFrameList = [] # List of telluric sky frames.

    obsidDateList = [] # 2D list of date, observation id pairs.
    sciDateList = [] # List of unique dates by science (including sky) frames.

    sciImageList = [] # List of science observation directories.

    # Store current working directory for later use.
    path = os.getcwd()

    # If files were copied from Gemini Internal network raw files directory will
    # be path+"/rawPath".
    if rawPath:
        rawPath = rawPath
    else:
        rawPath = path+'/rawPath'

    # Change to raw files directory, copy and sort FILE NAMES into lists of each type (Eg: science frames, ronchi flat frames).
    # Sort by opening the .fits headers, reading header data into variables and sorting based on those variables.
    # DOES NOT COPY RAW .fits DATA IN THIS STEP
    os.chdir(rawPath)
    logging.info("\nPath to raw file directory is: " + str(rawPath))

    logging.info("\nI am making lists of each type of file.")

    # Make a list of all the files in the rawPath directory.
    rawfiles = glob.glob('N*.fits')

    # Sort and copy each filename in the rawfiles directory into lists.
    for entry in rawfiles:

        # Open the .fits header.
        header = astropy.io.fits.open(entry)

        # Store information in variables.
        obstype = header[0].header['OBSTYPE'].strip()
        ID = header[0].header['OBSID']
        date = header[0].header[ 'DATE'].replace('-','')
        aper = header[0].header['APERTURE']
        obsclass = header[0].header['OBSCLASS']
        # If object name isn't alphanumeric, make it alphanumeric.
        objname = header[0].header['OBJECT']
        objname = re.sub('[^a-zA-Z0-9\n\.]', '', objname)
        poff = header[0].header['POFFSET']
        qoff = header[0].header['QOFFSET']

        # Make a list of science, telluric and acquisition frames.
        # Use the copied variable (1 not copied, 0 copied) to check later that
        # the file was copied correctly. allfilelist is a 2D list of
        # [[filename1, copied, obsclass1], [filename2, copied, obsclass2]] pairs.
        if obstype == 'OBJECT' and (obsclass == 'science' or obsclass == 'acq' or obsclass == 'acqCal' or obsclass == 'partnerCal'):

            # Append a list of [filename, copied, obsclass] to the list. copied is
            # 1 if not copied, 0 if copied. obsclass is used later for checks.
            templist = [entry, 1, obsclass]
            allfilelist.append(templist)

            # Create a list of science sky frames.
            # Differentiating between on target and sky frames.
            rad = math.sqrt(((poff)**2) + ((qoff)**2))

            # If the offsets are outside a circle of 5.0 units in radius, append to skyFrameList.
            if obsclass == 'science':
                sciImageList.append(entry)
                if rad  >= skyThreshold:
                    skyFrameList.append(entry)

            # Create a list of telluric sky frames.
            if obsclass == 'partnerCal':
                if rad >= skyThreshold:
                    telskyFrameList.append(entry)

            # Create sciDateList: list of unique dates of science observations.
            if obsclass == 'science':
                # Append if list is empty or not a duplicate of last entry.
                if not sciDateList or not sciDateList[-1]==date:
                    sciDateList.append(date)

        # Add arc frame names to arclist.
        if obstype == 'ARC':
            arclist.append(entry)

        # Add arc dark frame names to arcdarklist.
        if obstype == 'DARK':
            arcdarklist.append(entry)

        # Add lamps on flat frames to flatlist,
        # add lamps off flat frames to flatdarklist,
        # add ronchi flat frames to ronchilist.
        # Lamps on and lamps off flats, and lamps on and lamps off ronchis are
        # seperated by mean number of counts per pixel. Arbitrary threshold is
        # if mean_counts < 500, it is a lamps off flat or ronchi.
        if obstype == 'FLAT':

            if aper == 'Ronchi_Screen_G5615':
                # Only use lamps on ronchi flat frames.
                # Open the image and store pixel values in an array and
                # take the mean of all pixel values.
                array = astropy.io.fits.getdata(entry)
                mean_counts = np.mean(array)

                # Once the mean is stored in mean_counts we can check whether the
                # frame is a lamps off ronchi or a lamps on ronchi based on the counts.
                # 500.0 is an arbitrary threshold that appears to work well.
                if mean_counts < 500.0:
                    pass
                else:
                    ronchilist.append(entry)

            else:
                # Open the image and store pixel values in an array and
                # take the mean of all pixel values.
                array = astropy.io.fits.getdata(entry)
                mean_counts = np.mean(array)

                # Once the mean is stored in mean_counts we can check whether the
                # frame is a sky or an object based on the counts. 500.0 is an
                # arbitrary threshold that appears to work well.
                if mean_counts < 500.0:
                    flatdarklist.append(entry)
                else:
                    flatlist.append(entry)

    # Based on science (including sky) frames, make a list of unique [object, date] list pairs to be used later.
    for i in range(len(rawfiles)):

        header = astropy.io.fits.open(rawfiles[i])
        date = header[0].header['DATE'].replace('-','')
        obsclass = header[0].header['OBSCLASS']
        obj = header[0].header['OBJECT']
        obj= re.sub('[^a-zA-Z0-9\n\.]', '', obj)
        obstype = header[0].header['OBSTYPE'].strip()
        obsid = header[0].header['OBSID']
        grat = header[0].header['GRATING'][0:1]

        if obsclass == 'science':
            list1 = [obj, date, grat]
            # Append if list is empty or not a duplicate of last entry.
            if not objectDateGratingList or not list1 in objectDateGratingList:
                objectDateGratingList.append(list1)

    # Make list of unique [date, obsid] pairs from FLATS. If flat was taken on the same day as a science
    # frame, append that flat date. If not, append an arbitrary unique date from sciDateList.
    # This is so we can sort calibrations later by date and observation id.
    n = 0
    for flat in flatlist:
        header = astropy.io.fits.open(flat)
        obsid = header[0].header['OBSID']
        date = header[0].header['DATE'].replace('-','')
        # Make sure no duplicate dates are being entered.
        if flatlist.index(flat)==0 or not oldobsid==obsid:
            if date in sciDateList:
                list1 = [date, obsid]
            else:
                list1 = [sciDateList[n], obsid]
            obsidDateList.append(list1)
            n+=1
        oldobsid = obsid

    os.chdir(path)

    # Print information for user.
    logging.info("\nTotal number of files found by type.\n")
    logging.info("Length allfilelist (science and telluric frames): " +  str(len(allfilelist)))
    logging.info("Length sciImageList (science and science sky frames): " +  str(len(sciImageList)))
    logging.info("Length arclist (arc frames): " + str(len(arclist)))
    logging.info("Length arcdarklist (arc dark frames): " + str(len(arcdarklist)))
    logging.info("Length flatlist (lamps on flat frames): " + str(len(flatlist)))
    logging.info("Length flatdarklist (lamps off flat frames): "+str(len(flatdarklist)))
    logging.info("Length ronchilist (ronchi flat frames): "+str(len(ronchilist)))
    logging.info("Length skyFrameList (science sky frames): "+str(len(skyFrameList)))
    logging.info("Length telskyFrameList (telluric sky frames): "+str(len(telskyFrameList)))

    # Store number of telluric, telluric, sky, telluric sky and acquisition frames in number_files_to_be_copied.
    number_files_to_be_copied = len(allfilelist)

    # Store number of arcs, arc darks, lamps on flats, lamps off flats and ronchi flats in number_calibration_files_to_be_copied.
    number_calibration_files_to_be_copied = len(arclist) + len(arcdarklist) +\
                         len(flatlist) + len(flatdarklist) + len(ronchilist)

    logging.info("\nTotal number of frames to be copied: " + str(number_files_to_be_copied + number_calibration_files_to_be_copied))

    return allfilelist, arclist, arcdarklist, flatlist, flatdarklist, ronchilist, objectDateGratingList, skyFrameList, telskyFrameList, obsidDateList, sciImageList

#----------------------------------------------------------------------------------------#

def sortScienceAndTelluric(allfilelist, skyFrameList, telskyFrameList, sciImageList, rawPath):

    """Sorts the science frames, tellurics and acquisitions into the appropriate directories based on date, grating, obsid, obsclass.
    """

    # Store number of science, telluric, sky, telluric sky and acquisition frames in number_files_to_be_copied
    number_files_to_be_copied = len(allfilelist)

    # Initialize a counter to track how many files were copied. If this is different than
    # number_files_to_be_copied logging.info("a warning for the user at the end of sortScienceAndTelluric.")
    number_files_that_were_copied = 0

    logging.info("\n\nMaking new directories and copying files. In this step I will process " + str(number_files_to_be_copied) + " files.")

    # List of paths sorted by object and date. ['path/to/object1/date1', 'path/to/object1/date2'].
    objDirList = []
    # Create a 2D list scienceDirList. Second part is a path to a science directory.
    # First part is a list of calculated times of each frame in that science directory.
    # Eg: [[[5400,6500,7200], '/path/to/first/science'], [[3400,4300,5200], '/path/to/second/science']...]
    scienceDirList = []
    # List of paths to telluric directories.
    telDirList = []

    path = os.getcwd()
    if rawPath:
        rawPath = rawPath
    else:
        rawPath = path+'/rawPath'

    # Make new sorted directories to copy files in to.
    logging.info("\nMaking new directories.\n")

    # All data is sorted by science frame data.
    # For each science frame, create a "science_object_name/date/" directory in
    # the current working directory.
    for entry in allfilelist:
        header = astropy.io.fits.open(rawPath+'/'+entry[0])

        objname = header[0].header['OBJECT']
        objname = re.sub('[^a-zA-Z0-9\n\.]', '', objname)
        obsclass = header[0].header['OBSCLASS']
        date = header[0].header[ 'DATE'].replace('-','')

        if obsclass=='science':
            if not os.path.exists(path+'/'+objname):
                os.mkdir(path+'/'+objname)
            if not os.path.exists(path+'/'+objname+'/'+date):
                os.mkdir(path+'/'+objname+'/'+date)
                objDir = path+'/'+objname+'/'+date
                if not objDirList or not objDirList[-1]==objDir:
                    objDirList.append(objDir)
            else:
                objDir = path+'/'+objname+'/'+date
                if not objDirList or not objDirList[-1]==objDir:
                    objDirList.append(objDir)

    # For each science frame, create a "science_object_name/date/grating/observationid/"
    # directory in the current working directory.
    for entry in allfilelist:
        header = astropy.io.fits.open(rawPath+'/'+entry[0])

        obstype = header[0].header['OBSTYPE'].strip()
        obsid = header[0].header['OBSID'][-3:].replace('-','')
        grat = header[0].header['GRATING'][0:1]
        date = header[0].header[ 'DATE'].replace('-','')
        obsclass = header[0].header['OBSCLASS']
        obj = header[0].header['OBJECT']
        obj = re.sub('[^a-zA-Z0-9\n\.]', '', obj)

        if obsclass=='science':
            # Important- calculate the time of day in seconds that the science (and sky) frames
            # were taken. Used because one way to match telluric frames with science frames is
            # to pair the frames closest in time.
            time = timeCalc(rawPath+'/'+entry[0])

            objDir = path+'/'+obj
            # Create a directory for each observation date (YYYYMMDD) in objDir/.
            if not os.path.exists(objDir+'/'+date):
                os.mkdir(objDir+'/'+date)
            # Create a directory for each grating used in objDir/YYYYMMDD/.
            if not os.path.exists(objDir+'/'+date+'/'+grat):
                os.mkdir(objDir+'/'+date+'/'+grat)
            # Create a directory for each obsid (eg. obs25) in objDir/YYYYMMDD/grating/.
            if not os.path.exists(objDir+'/'+date+'/'+grat+'/obs'+obsid):
                os.mkdir(objDir+'/'+date+'/'+grat+'/obs'+obsid)
                # If a new directory append time of science (or sky) frame and directory name to scienceDirList.
                scienceDirList.append([[time], objDir+'/'+date+'/'+grat+'/obs'+obsid])
            # Else if a new list or not a duplicate of the previous entry append time and directory name to scienceDirList.
            elif not scienceDirList or not scienceDirList[-1][1]==objDir+'/'+date+'/'+grat+'/obs'+obsid:
                scienceDirList.append([[time], objDir+'/'+date+'/'+grat+'/obs'+obsid])
            # IF A DUPLICATE:
            # Append the time to an existing time list.
            #
            # Eg, before appending: [[[5400,6500,7200], '/path/to/first/science'], [[5200], '/path/to/second/science']]
            # If we are processing the second frame in /path/to/second/science/, scienceDirList[-1][1] will equal /path/to/second/science.
            # Then append the new time to the second entry.
            #
            # [[[5400,6500,7200], '/path/to/first/science'], [[5200, NEWTIMEHERE], '/path/to/second/science']]

            elif scienceDirList[-1][1] == objDir+'/'+date+'/'+grat+'/obs'+obsid:
                scienceDirList[-1][0].append(time)


    # Copy science and acquisition frames to the appropriate directory.
    logging.info("\nCopying Science and Acquisitions.\nCopying science frames and science acquisitions.\nNow copying: ")

    for i in range(len(allfilelist)):
        header = astropy.io.fits.open(rawPath+'/'+allfilelist[i][0])

        obstype = header[0].header['OBSTYPE'].strip()
        obsid = header[0].header['OBSID'][-3:].replace('-','')
        grat = header[0].header['GRATING'][0:1]
        date = header[0].header[ 'DATE'].replace('-','')
        obsclass = header[0].header['OBSCLASS']
        obj = header[0].header['OBJECT']
        obj = re.sub('[^a-zA-Z0-9\n\.]', '', obj)

        # Only grab the most recent aquisition frame.
        if i!=len(allfilelist)-1:
            header2 = astropy.io.fits.open(rawPath+'/'+allfilelist[i+1][0])
            obsclass2 = header2[0].header['OBSCLASS']
            obj2 = header2[0].header['OBJECT']
            obj2 = re.sub('[^a-zA-Z0-9\n\.]', '', obj2)

        # Copy sky and science frames to appropriate directories. Write two text files in
        # those directories that store the names of the science frames and sky frames for later
        # use by the pipeline.
        if obsclass=='science':
            logging.info(allfilelist[i][0])
            objDir = path+'/'+obj
            shutil.copy(rawPath+'/'+allfilelist[i][0], objDir+'/'+date+'/'+grat+'/obs'+obsid+'/')
            number_files_that_were_copied += 1
            # Update status flag to show entry was copied.
            allfilelist[i][1] = 0
            # Create an scienceFrameList in the relevant directory.
            if allfilelist[i][0] not in skyFrameList:
                writeList(allfilelist[i][0], 'scienceFrameList', objDir+'/'+date+'/'+grat+'/obs'+obsid+'/')
            # Create a skyFrameList in the relevant directory.
            if allfilelist[i][0] in skyFrameList:
                writeList(allfilelist[i][0], 'skyFrameList', objDir+'/'+date+'/'+grat+'/obs'+obsid+'/')

        # Copy the most recent acquisition in each set to a new directory to be optionally
        # used later by the user for checks (not used by the pipeline).
        if obsclass=='acq' and obsclass2=='science':
            logging.info(allfilelist[i][0])
            # create an Acquisitions directory in objDir/YYYYMMDD/grating
            if not os.path.exists(path+'/'+obj2+'/'+date+'/'+grat+'/Acquisitions/'):
                os.makedirs(path+'/'+obj2+'/'+date+'/'+grat+'/Acquisitions/')
            shutil.copy(rawPath+'/'+allfilelist[i][0], path+'/'+obj2+'/'+date+'/'+grat+'/Acquisitions/')
            number_files_that_were_copied += 1
            allfilelist[i][1] = 0

    # Copy telluric frames to the appropriate folder.
    # Note: Because the 'OBJECT' of a telluric file header is different then the
    # science target, we need to sort by date, grating AND most recent time.
    logging.info("\nCopying telluric frames.\nNow copying: ")
    for i in range(len(allfilelist)):
        header = astropy.io.fits.open(rawPath+'/'+allfilelist[i][0])

        obstype = header[0].header['OBSTYPE'].strip()
        obsid = header[0].header['OBSID'][-3:].replace('-','')
        grat = header[0].header['GRATING'][0:1]
        date = header[0].header[ 'DATE'].replace('-','')
        obsclass = header[0].header['OBSCLASS']
        obj = header[0].header['OBJECT']
        obj = re.sub('[^a-zA-Z0-9\n\.]', '', obj)
        telluric_time = timeCalc(rawPath+'/'+allfilelist[i][0])


        if obsclass=='partnerCal':
            logging.info(allfilelist[i][0])
            timeList = []
            for k in range(len(scienceDirList)):
                # Make sure date and gratings match.
                tempDir = scienceDirList[k][1].split(os.sep)
                if date in tempDir and grat in tempDir:
                    # Open the times of all science frames in science_directory.
                    times = scienceDirList[k][0]
                    # Find difference in each time from the telluric frame we're trying to sort.
                    diffList = []
                    for b in range(len(times)):
                        difference = abs(telluric_time-scienceDirList[k][0][b])
                        templist = []
                        templist.append(difference)
                        templist.append(scienceDirList[k][1])
                        diffList.append(templist)
                    # Find the science frame with the smallest difference.
                    minDiff = min(diffList)
                    # Pass that time and path out of the for loop.
                    timeList.append(minDiff)
            # Out of the for loop, compare min times from different directories.
            if timeList:
                closest_time = min(timeList)
                # Copy the telluric frame to the path of that science frame.
                path_to_science_dir = closest_time[1]
                path_to_tellurics = os.path.split(path_to_science_dir)[0]

                # Create a Tellurics directory in science_object_name/YYYYMMDD/grating.

                if not os.path.exists(path_to_tellurics + '/Tellurics'):
                    os.mkdir(path_to_tellurics + '/Tellurics')
                # Create an obsid (eg. obs25) directory in the Tellurics directory.
                if not os.path.exists(path_to_tellurics+'/Tellurics/obs'+obsid):
                    os.mkdir(path_to_tellurics+'/Tellurics/obs'+obsid)
                    telDirList.append(path_to_tellurics+'/Tellurics/obs'+obsid)
                elif not telDirList or not telDirList[-1]==path_to_tellurics+'/Tellurics/obs'+obsid:
                    telDirList.append(path_to_tellurics+'/Tellurics/obs'+obsid)
                shutil.copy(rawPath+'/'+allfilelist[i][0], path_to_tellurics+'/Tellurics/obs'+obsid+'/')
                number_files_that_were_copied += 1
                allfilelist[i][1] = 0
                # Create an scienceFrameList in the relevant directory.
                if allfilelist[i][0] not in telskyFrameList:
                    writeList(allfilelist[i][0], 'tellist', path_to_tellurics+'/Tellurics/obs'+obsid+'/')
                # Create a skyFrameList in the relevant directory.
                if allfilelist[i][0] in telskyFrameList:
                    writeList(allfilelist[i][0], 'skyFrameList', path_to_tellurics+'/Tellurics/obs'+obsid+'/')

    # Modify scienceDirList to a format telSort can use.
    tempList = []
    for i in range(len(scienceDirList)):
        tempList.append(scienceDirList[i][1])
    scienceDirList = tempList

    #------------------------------ TESTS -------------------------------------#

    # Check to see which files were not copied.
    logging.info("\nChecking for non-copied science, tellurics and acquisitions.\n")
    for i in range(len(allfilelist)):
        # Check the copied flag. If not 0, logging.info("the entry.")
        if allfilelist[i][1] != 0:
            logging.info(str(allfilelist[i][0]) + " " + str(allfilelist[i][2]) + " was not copied.")
    logging.info("\nEnd non-copied science, tellurics and acquisitions.\n")

    # Check that all science frames and sky frames were copied.
    count_from_raw_files = len(sciImageList) + len(skyFrameList)

    count = 0
    for science_directory in scienceDirList:
        for file in os.listdir(science_directory):
            if file.endswith('.fits'):
                count += 1

    if count_from_raw_files != count:
        logging.info("\nWARNING: " + str(count_from_raw_files - count) + " science frames (or sky frames) \
        were not copied.\n")
    else:
        logging.info("\nExpected number of science and sky frames copied.\n")

    logging.info("\nDone sorting and copying science and tellurics. Moving on to Calibrations.\n")

    # Test for telluric directories with mis-identified sky frames. For now, we identify sky frames
    # based on absolute P and Q offsets, not relative to a zero point. This can cause problems.
    # TODO(nat): look into if it is worth it to use relative P and Q offsets.
    for telluric_directory in telDirList:
        if os.path.exists(telluric_directory + '/skyFrameList') and not os.path.exists(telluric_directory + '/tellist'):
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: a telluric directory exists that Nifty thinks ")
            logging.info("                      contains only sky frames. Nifty uses absolute")
            logging.info("                      P and Q offsets to identify sky frames; a target")
            logging.info("                      not being at 0, 0 P and Q can cause this. If this is not")
            logging.info("                      the case you can try adjusting the skyThreshold")
            logging.info("                      parameter in Nifty's configuration.")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")
            os.chdir(telluric_directory)
            rewriteSciImageList(2.0, "Telluric")
            try:
                sciImageList = open('tellist', "r").readlines()
                logging.info("\nSucceeded; a telluric frame list exists in " + str(os.getcwd()))
            except IOError:
                logging.info("\nWARNING: no telluric frames found in " + str(os.getcwd()) + ". You may have to adjust the skyThreshold parameter.")
                a = raw_input("Please make a tellist (list of telluric frames) in " + str(telluric_directory))
            os.chdir(path)

    os.chdir(path)

    return objDirList, scienceDirList, telDirList

#----------------------------------------------------------------------------------------#

def sortCalibrations(arcdarklist, arclist, flatlist, flatdarklist, ronchilist, objectDateGratingList, objDirList, obsidDateList, sciImageList, rawPath, manualMode):

    """Sort calibrations into appropriate directories based on date.
    """
    calDirList = []
    filelist = ['arclist', 'arcdarklist', 'flatlist', 'ronchilist', 'flatdarklist']

    # Save path for later use. The rawPath part is for Gemini North network sorting.
    path1 = os.getcwd()
    if rawPath:
        rawPath = rawPath
    else:
        rawPath = path1+'/rawPath'

    # Set up some tests and checks.
    count = 0
    expected_count = len(arcdarklist) + len(arclist) + len(flatlist)\
          + len(flatdarklist) + len(ronchilist)

    logging.info("\nI am attempting to sort " + str(expected_count) + " files.\n")

    # To make sure data was copied later in the pipeline:
    # Add a small copied flag to each frame in calibration file lists.
    new_flatlist = []
    for i in range(len(flatlist)):
        # Transform 1D list into 2D list of [[filename, 'copied']]
        # "copied" is 1 for not copied and 0 for copied.
        templist = []
        templist.append(flatlist[i])
        templist.append(1)
        new_flatlist.append(templist)
    flatlist = new_flatlist

    new_flatdarklist = []
    for i in range(len(flatdarklist)):
        # Transform 1D list into 2D list.
        templist = []
        templist.append(flatdarklist[i])
        templist.append(1)
        new_flatdarklist.append(templist)
    flatdarklist = new_flatdarklist

    new_arclist = []
    for i in range(len(arclist)):
        # Transform 1D list into 2D list.
        templist = []
        templist.append(arclist[i])
        templist.append(1)
        new_arclist.append(templist)
    arclist = new_arclist

    new_arcdarklist = []
    for i in range(len(arcdarklist)):
        # Transform 1D list into 2D list.
        templist = []
        templist.append(arcdarklist[i])
        templist.append(1)
        new_arcdarklist.append(templist)
    arcdarklist = new_arcdarklist

    new_ronchilist = []
    for i in range(len(ronchilist)):
        # Transform 1D list into 2D list.
        templist = []
        templist.append(ronchilist[i])
        templist.append(1)
        new_ronchilist.append(templist)
    ronchilist = new_ronchilist

    os.chdir(rawPath)

    # Create Calibrations directories in each of the observation date directories based on existence of
    # lamps on flats. Eg: YYYYMMDD/Calibrations
    # Sort lamps on flats.
    logging.info("\nSorting flats:")
    # Create a flag so we only warn about non-standard gratings once.
    grating_warning_flag = False
    for i in range(len(flatlist)):
        header = astropy.io.fits.open(flatlist[i][0])
        obsid = header[0].header['OBSID']
        grating = header[0].header['GRATING'][0:1]
        if grating not in ["K", "J", "H", "Z"]:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: non-standard (non K, J, H, K) grating encountered. ")
            logging.info("                      NIFTY has not been tested with non-standard")
            logging.info("                      gratings!")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")
        # TODO(nat): this is horrendous. Do this in a better way.
        # "Flat is better than nested."
        for objDir in objDirList:
            for item in obsidDateList:
                if obsid in item:
                    date = item[0]
                    if date in objDir:
                        for entry in objectDateGratingList:
                            if entry[1] == date and entry[2] == grating:
                                if not os.path.exists(path1+'/'+entry[0]+'/'+entry[1]+'/Calibrations_'+grating):
                                    os.mkdir(path1+'/'+entry[0]+'/'+entry[1]+'/Calibrations_'+grating)
                                    calDirList.append(path1+'/'+entry[0]+'/'+entry[1]+'/Calibrations_'+grating)
                                else:
                                    if path1+'/'+entry[0]+'/'+entry[1]+'/Calibrations_'+grating not in calDirList:
                                        calDirList.append(path1+'/'+entry[0]+'/'+entry[1]+'/Calibrations_'+grating)
                                # Copy lamps on flats to appropriate directory.
                                shutil.copy('./'+flatlist[i][0], objDir+'/Calibrations_'+grating+'/')
                                flatlist[i][1] = 0
                                logging.info(flatlist[i][0])
                                count += 1
                                path = objDir+'/Calibrations_'+grating+'/'
                                # Create a flatlist in the relevent directory.
                                # Create a text file called flatlist to store the names of the
                                # lamps on flats for later use by the pipeline.
                                writeList(flatlist[i][0], 'flatlist', path)

    # Sort lamps off flats.
    logging.info("\nSorting lamps off flats:")
    for i in range(len(flatdarklist)):
        os.chdir(rawPath)
        header = astropy.io.fits.open(flatdarklist[i][0])
        obsid = header[0].header['OBSID']
        grating = header[0].header['GRATING'][0:1]
        for objDir in objDirList:
            for item in obsidDateList:
                if obsid in item:
                    date = item[0]
                    if date in objDir:
                        if not os.path.exists(objDir+'/Calibrations_'+grating):
                            os.mkdir(objDir+'/Calibrations_'+grating)
                        shutil.copy('./'+flatdarklist[i][0], objDir+'/Calibrations_'+grating+'/')
                        flatdarklist[i][1] = 0
                        logging.info(flatdarklist[i][0])
                        count += 1
                        path = objDir+'/Calibrations_'+grating+'/'
                        # Create a flatdarklist in the relevant directory.
                        writeList(flatdarklist[i][0], 'flatdarklist', path)

    # Sort ronchi flats.
    logging.info("\nSorting ronchi flats:")
    for i in range(len(ronchilist)):
        os.chdir(rawPath)
        header = astropy.io.fits.open(ronchilist[i][0])
        obsid = header[0].header['OBSID']
        grating = header[0].header['GRATING'][0:1]
        for objDir in objDirList:
            for item in obsidDateList:
                if obsid in item:
                    date = item[0]
                    if date in objDir:
                        if not os.path.exists(objDir+'/Calibrations_'+grating):
                            os.mkdir(objDir+'/Calibrations_'+grating)
                        shutil.copy('./'+ronchilist[i][0], objDir+'/Calibrations_'+grating+'/')
                        ronchilist[i][1] = 0
                        logging.info(ronchilist[i][0])
                        count += 1
                        path = objDir+'/Calibrations_'+grating+'/'
                        # create a ronchilist in the relevant directory
                        writeList(ronchilist[i][0], 'ronchilist', path)

    # Sort arcs.
    logging.info("\nSorting arcs:")
    for i in range(len(arclist)):
        header = astropy.io.fits.open(arclist[i][0])
        date = header[0].header['DATE'].replace('-','')
        grating = header[0].header['GRATING'][0:1]
        for objDir in objDirList:
            if date in objDir:
                if not os.path.exists(objDir+'/Calibrations_'+grating):
                    os.mkdir(objDir+'/Calibrations_'+grating)
                shutil.copy('./'+arclist[i][0], objDir+'/Calibrations_'+grating+'/')
                arclist[i][1] = 0
                logging.info(arclist[i][0])
                count += 1
                path = objDir+'/Calibrations_'+grating+'/'
                # Create an arclist in the relevant directory.
                writeList(arclist[i][0], 'arclist', path)

    # Sort arc darks.
    logging.info("\nSorting arc darks:")
    for i in range(len(arcdarklist)):
        header = astropy.io.fits.open(arcdarklist[i][0])
        obsid = header[0].header['OBSID']
        grating = header[0].header['GRATING'][0:1]
        for objDir in objDirList:
            for item in obsidDateList:
                if obsid in item:
                    date = item[0]
                    if date in objDir:
                        if not os.path.exists(objDir+'/Calibrations_'+grating):
                            os.mkdir(objDir+'/Calibrations_'+grating)
                        shutil.copy('./'+arcdarklist[i][0], objDir+'/Calibrations_'+grating+'/')
                        arcdarklist[i][1] = 0
                        logging.info(arcdarklist[i][0])
                        count += 1
                        path = objDir+'/Calibrations_'+grating+'/'
                        # Create an arcdarklist in the relevant directory.
                        writeList(arcdarklist[i][0], 'arcdarklist', path)

    # Check that each file in flatlist was copied.
    for i in range(len(flatlist)):
        if flatlist[i][1] == 1:
            logging.info(str(flatlist[i][0])+ " was not copied.")


    # ---------------------------- Tests ------------------------------------- #

    # Check to see how many calibrations were copied.
    if expected_count - count == 0:
        logging.info("\nI sorted the " + str(expected_count) + " expected calibrations.\n")
    else:
        logging.info("\nI did not copy " + str(expected_count - count) + " calibration file(s).\n")

    # Check each calibration file list to see which ones were not copied.
    # Check that each file in flatlist was copied.
    for i in range(len(flatlist)):
        if flatlist[i][1] == 1:
            logging.info(str(flatlist[i][0])+ " from flatlist was not copied.")

    # Check that each file in flatdarklist was copied.
    for i in range(len(flatdarklist)):
        if flatdarklist[i][1] == 1:
            logging.info(str(flatdarklist[i][0])+ " from flatdarklist was not copied.")

    # Check that each file in ronchilist was copied.
    for i in range(len(ronchilist)):
        if ronchilist[i][1] == 1:
            logging.info(str(ronchilist[i][0])+ " from ronchilist was not copied.")

    # Check that each file in arclist was copied.
    for i in range(len(arclist)):
        if arclist[i][1] == 1:
            logging.info(str(arclist[i][0])+ " from arclist was not copied.")

    # Check that each file in arcdarklist was copied.
    for i in range(len(arcdarklist)):
        if arcdarklist[i][1] == 1:
            logging.info(str(arcdarklist[i][0])+ " from arcdarklist was not copied.")


    # Change back to original working directory.
    os.chdir(path1)

    # Check that each science directory exists and has associated calibration data.
    # Pseudocode (repeated below with actual code):
    # For each science directory, make sure that:
    # a calibrations directory is present.
    # flatlist exists and has more than one file.
    # flatdarklist exists and has more than one file.
    # arclist exists and has more than one file.
    # arcdarklist exists and has more than one file.
    # ronchilist exists and has more than one file.


    # TODO(nat): This is horrifying. Good grief, wrap these repetitive calls in a function!
    logging.info("\nChecking that each science image has required calibration data. ")
    # For each science image, read its header data and try to change to the appropriate directory.
    # Check that:
    for i in range(len(sciImageList)):
        header = astropy.io.fits.open(rawPath+'/'+sciImageList[i])

        obstype = header[0].header['OBSTYPE'].strip()
        obsid = header[0].header['OBSID'][-3:].replace('-','')
        grat = header[0].header['GRATING'][0:1]
        date = header[0].header[ 'DATE'].replace('-','')
        obsclass = header[0].header['OBSCLASS']
        obj = header[0].header['OBJECT']
        obj = re.sub('[^a-zA-Z0-9\n\.]', '', obj)

        # a science and Calibrations directory are present.
        try:
            os.chdir(path1+'/'+obj+'/'+date+'/'+grat+'/obs'+obsid+'/')
            os.chdir('../../Calibrations_'+grat+'/')
        except OSError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no Calibrations directory found for ")
            logging.info("                      science frame "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")
            continue

        # flatlist exists and has more than one file.
        try:
            flatListFile = open('flatlist', "r").readlines()
            if len(flatListFile) <= 1:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: only 1 lamps on flat frame found for science")
                logging.info("                      frame "+str(sciImageList[i]))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
        except IOError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no flatlist found for science frame")
            logging.info("                      "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

            if not manualMode:
                # Sometimes flats can be taken a day after the observing night. First
                # look for these, and if they are not found, ask the user to provide some flats.
                foundflatFlag = False
                # Get date after the science observation
                t=time.strptime(date,'%Y%m%d')
                newdate=datetime.date(t.tm_year,t.tm_mon,t.tm_mday)+datetime.timedelta(1)
                # Loop through flatlist and see if there is an flat taken on this date
                for i in range(len(flatlist)):
                    header = astropy.io.fits.open(rawPath+'/'+flatlist[i][0])
                    date = header[0].header[ 'DATE'].replace('-','')
                    if str(date) == newdate.strftime('%Y%m%d'):
                        # If so, copy it to the appropriate calibrations directory and write an flatlist.
                        shutil.copy(rawPath + '/' + flatlist[i][0], './')
                        writeList(flatlist[i][0], 'flatlist', path)
                        logging.info("\n#####################################################################")
                        logging.info("#####################################################################")
                        logging.info("")
                        logging.info("     WARNING in sort: found a flat taken one day after a science frame.")
                        logging.info("                      "+str(sciImageList[i]))
                        logging.info("                       using that.")
                        logging.info("")
                        logging.info("#####################################################################")
                        logging.info("#####################################################################\n")
                        foundflatFlag = True
                        flatlist[i][1] = 0
                if not foundflatFlag:
                    # If that quick check fails, give user a chance to try and provide an flat file.
                    a = raw_input("\n Please provide a textfile called flatlist in " + str(os.getcwd()))


        # flatdarklist exists and has more than one file.
        try:
            flatDarkListFile = open('flatdarklist', "r").readlines()
            if len(flatDarkListFile) <= 1:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: only 1 lamps off flat frame found for science")
                logging.info("                      frame "+str(sciImageList[i]))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
        except IOError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no flatdarklist found for science frame")
            logging.info("                      "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")
            if not manualMode:
                # Sometimes flatdarks can be taken a day after the observing night. First
                # look for these, and if they are not found, ask the user to provide some flatdarks.
                foundflatdarkFlag = False
                # Get date after the science observation
                t=time.strptime(date,'%Y%m%d')
                newdate=datetime.date(t.tm_year,t.tm_mon,t.tm_mday)+datetime.timedelta(1)
                # Loop through flatdarklist and see if there is an flatdark taken on this date
                for i in range(len(flatdarklist)):
                    header = astropy.io.fits.open(rawPath+'/'+flatdarklist[i][0])
                    date = header[0].header[ 'DATE'].replace('-','')
                    if str(date) == newdate.strftime('%Y%m%d'):
                        # If so, copy it to the appropriate calibrations directory and write an flatdarklist.
                        shutil.copy(rawPath + '/' + flatdarklist[i][0], './')
                        writeList(flatdarklist[i][0], 'flatdarklist', path)
                        logging.info("\n#####################################################################")
                        logging.info("#####################################################################")
                        logging.info("")
                        logging.info("     WARNING in sort: found a flatdark taken one day after a science frame.")
                        logging.info("                      "+str(sciImageList[i]))
                        logging.info("                       using that.")
                        logging.info("")
                        logging.info("#####################################################################")
                        logging.info("#####################################################################\n")
                        foundflatdarkFlag = True
                        flatdarklist[i][1] = 0
                if not foundflatdarkFlag:
                    # If that quick check fails, give user a chance to try and provide an flatdark file.
                    a = raw_input("\n Please provide a textfile called flatdarklist in " + str(os.getcwd()) + \
                    " or be sure not to attempt a wavelength calibration for this directory.")
        # Make sure flatlist and flatdarklist are the same length. nsflat() complains otherwise.
        checkSameLengthFlatLists()

        # arclist exists.
        try:
            arcListFile = open('arclist', "r").readlines()
        except IOError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no arclist found for science frame")
            logging.info("                      "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

            if not manualMode:
                # Sometimes arcs can be taken a day after the observing night. First
                # look for these, and if they are not found, ask the user to provide some arcs.
                foundArcFlag = False
                # Get date after the science observation
                t=time.strptime(date,'%Y%m%d')
                newdate=datetime.date(t.tm_year,t.tm_mon,t.tm_mday)+datetime.timedelta(1)
                # Loop through arclist and see if there is an arc taken on this date
                for i in range(len(arclist)):
                    header = astropy.io.fits.open(rawPath+'/'+arclist[i][0])
                    date = header[0].header[ 'DATE'].replace('-','')
                    if str(date) == newdate.strftime('%Y%m%d'):
                        # If so, copy it to the appropriate calibrations directory and write an arclist.
                        shutil.copy(rawPath + '/' + arclist[i][0], './')
                        writeList(arclist[i][0], 'arclist', path)
                        logging.info("\n#####################################################################")
                        logging.info("#####################################################################")
                        logging.info("")
                        logging.info("     WARNING in sort: found an arc taken one day after a science frame.")
                        logging.info("                      "+str(sciImageList[i]))
                        logging.info("                       using that.")
                        logging.info("")
                        logging.info("#####################################################################")
                        logging.info("#####################################################################\n")
                        foundArcFlag = True
                        arclist[i][1] = 0
                if not foundArcFlag:
                    # If that quick check fails, give user a chance to try and provide an arc file.
                    a = raw_input("\n Please provide a textfile called arclist in " + str(os.getcwd()) + \
                    " or be sure not to attempt a wavelength calibration for this directory.")

        # arcdarklist exists.
        try:
            arcDarkListFile = open('arcdarklist', "r").readlines()
        except IOError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no arcdarklist found for science frame")
            logging.info("                      "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")
            if not manualMode:
                # Sometimes arcdarks can be taken a day after the observing night. First
                # look for these, and if they are not found, ask the user to provide some arcdarks.
                foundarcdarkFlag = False
                # Get date after the science observation
                t=time.strptime(date,'%Y%m%d')
                newdate=datetime.date(t.tm_year,t.tm_mon,t.tm_mday)+datetime.timedelta(1)
                # Loop through arcdarklist and see if there is an arcdark taken on this date
                for i in range(len(arcdarklist)):
                    header = astropy.io.fits.open(rawPath+'/'+arcdarklist[i][0])
                    date = header[0].header[ 'DATE'].replace('-','')
                    if str(date) == newdate.strftime('%Y%m%d'):
                        # If so, copy it to the appropriate calibrations directory and write an arcdarklist.
                        shutil.copy(rawPath + '/' + arcdarklist[i][0], './')
                        writeList(arcdarklist[i][0], 'arcdarklist', path)
                        logging.info("\n#####################################################################")
                        logging.info("#####################################################################")
                        logging.info("")
                        logging.info("     WARNING in sort: found an arcdark taken one day after a science frame.")
                        logging.info("                      "+str(sciImageList[i]))
                        logging.info("                       using that.")
                        logging.info("")
                        logging.info("#####################################################################")
                        logging.info("#####################################################################\n")
                        foundarcdarkFlag = True
                        arcdarklist[i][1] = 0
                if not foundarcdarkFlag:
                    # If that quick check fails, give user a chance to try and provide an arcdark file.
                    a = raw_input("\n Please provide a textfile called arcdarklist in " + str(os.getcwd()) + \
                    " or be sure not to attempt a wavelength calibration for this directory.")
        # ronchilist exists and has more than one file.
        try:
            ronchiListFile = open('ronchilist', "r").readlines()
            if len(ronchiListFile) <= 1:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: only 1 ronchi flat frame found for science frame")
                logging.info("                      "+str(sciImageList[i]))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
        except IOError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no ronchilist found for science frame")
            logging.info("                      "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")
            if not manualMode:
                # Sometimes ronchis can be taken a day after the observing night. First
                # look for these, and if they are not found, ask the user to provide some ronchis.
                foundronchiFlag = False
                # Get date after the science observation
                t=time.strptime(date,'%Y%m%d')
                newdate=datetime.date(t.tm_year,t.tm_mon,t.tm_mday)+datetime.timedelta(1)
                # Loop through ronchilist and see if there is an ronchi taken on this date
                for i in range(len(ronchilist)):
                    header = astropy.io.fits.open(rawPath+'/'+ronchilist[i][0])
                    date = header[0].header[ 'DATE'].replace('-','')
                    if str(date) == newdate.strftime('%Y%m%d'):
                        # If so, copy it to the appropriate calibrations directory and write an ronchilist.
                        shutil.copy(rawPath + '/' + ronchilist[i][0], './')
                        writeList(ronchilist[i][0], 'ronchilist', path)
                        logging.info("\n#####################################################################")
                        logging.info("#####################################################################")
                        logging.info("")
                        logging.info("     WARNING in sort: found a ronchi taken one day after a science frame.")
                        logging.info("                      "+str(sciImageList[i]))
                        logging.info("                       using that.")
                        logging.info("")
                        logging.info("#####################################################################")
                        logging.info("#####################################################################\n")
                        foundronchiFlag = True
                        ronchilist[i][1] = 0
                if not foundronchiFlag:
                    # If that quick check fails, give user a chance to try and provide an ronchi file.
                    a = raw_input("\n Please provide a textfile called ronchilist in " + str(os.getcwd()) + \
                    " or be sure not to attempt a wavelength calibration for this directory.")
        os.chdir(path1)

    # Change back to original working directory.
    os.chdir(path1)

    # ---------------------------- End Tests --------------------------------- #

    return calDirList

#----------------------------------------------------------------------------------------#

def matchTellurics(telDirList, obsDirList, telluricTimeThreshold):

    """Matches science images with the telluric frames that are closest in time.
    Creates a file in each telluric observation directory called scienceMatchedTellsList.
    scienceMatchedTellsList lists the obsid of the science images (ie. obs123) and then the
    science images with this obsid that match the telluric observation.

    EXAMPLE:    obs28
                N20130527S0264
                N20130527S0266
                obs30
                N201305727S0299

    """

    logging.info("\nI am matching science images with tellurics closest in time.\n")

    # Store current working directory for later use.
    path = os.getcwd()

    # Get a list of unique dates of telluric observations.
    dateList=[]
    for i in range(len(telDirList)):
        date = telDirList[i].split(os.sep)[-4]
        if i==0 or dateList[-1]!=date:
            dateList.append(date)

    # Make a 2D list; list of lists of telluric directory path, files in that directory, grating of those tellurics.
    # [['telluric_directory/', ['telluric1.fits, telluric2.fits, ...'], 'telluric_grating']]
    for date in dateList:
        tellist = []
        for telDir in telDirList:
            if date in telDir:

                os.chdir(telDir)
                telImageList = open(telDir + '/' + 'tellist', "r").readlines()
                telImageList = [image.strip() for image in telImageList]
                telluric_image = telImageList[0]
                telluric_header = astropy.io.fits.open(telDir +'/'+ telluric_image + '.fits')
                telluric_grating = telluric_header[0].header['GRATING'][0:1]

                timeList=[]
                if os.path.exists('./scienceMatchedTellsList'):
                    os.remove('./scienceMatchedTellsList')
                templist = []
                imageList=glob.glob('N*.fits')
                templist.append(telDir)
                templist.append(imageList)
                templist.append(telluric_grating)
                tellist.append(templist)

        # Create a list of the start and stop times for each observation called timeList.
        # timeList is of the form [[obsid1, start1, stop1], [obsid2, start2, stop2],...]
        for a in range(len(tellist)):
            templist=[]
            os.chdir(tellist[a][0])
            telheader = astropy.io.fits.open(tellist[a][1][0])
            start=timeCalc(tellist[a][1][0])
            stop=timeCalc(tellist[a][1][-1])
            templist.append(os.getcwd())
            templist.append(start)
            templist.append(stop)
            templist.append(tellist[a][2])
            timeList.append(templist)

        # Find a science image with the same date and grating.
        for obsDir in obsDirList:
            os.chdir(obsDir)
            if date in obsDir:
                try:
                    sciImageList = open('scienceFrameList', "r").readlines()
                except IOError:
                    sciImageList = open('skyFrameList', "r").readlines()
                sciImageList = [image.strip() for image in sciImageList]

                # Open image and get science image grating from header.

                science_image = sciImageList[0]
                science_header = astropy.io.fits.open('./'+ science_image + '.fits')
                science_grating = science_header[0].header['GRATING'][0:1]

                for image in sciImageList:
                    diffList=[]
                    imageTime = timeCalc(image+'.fits')
                    for b in range(len(timeList)):
                        # Check to make sure telluric grating and science grating match.
                        if timeList[b][3] == science_grating:
                            if abs(imageTime-timeList[b][1]) <= int(telluricTimeThreshold) or abs(imageTime-timeList[b][2]) <= int(telluricTimeThreshold):
                                if abs(imageTime-timeList[b][1]) < abs(imageTime-timeList[b][2]):
                                    diff = abs(imageTime-timeList[b][1])
                                else:
                                    diff = abs(imageTime-timeList[b][2])
                                diffList.append(timeList[b][0])
                                diffList.append(diff)

                    # Find and record the science observation that is closest in time to the telluric image.
                    # Store the science observation name in a textfile, scienceMatchedTellsList, for later use by the pipeline.
                    if diffList:
                        minDiff = min(diffList)
                        telobs = diffList[diffList.index(minDiff)-1]
                        sciheader = astropy.io.fits.open(image+'.fits')
                        sciObsid = 'obs'+ sciheader[0].header['OBSID'][-3:].replace('-','')
                        if not os.path.exists(telobs+'/scienceMatchedTellsList'):
                            writeList(sciObsid, 'scienceMatchedTellsList', telobs)
                        else:
                            scienceMatchedTellsList = open(telobs+'/scienceMatchedTellsList', 'r').readlines()
                            scienceMatchedTellsList = [item.strip() for item in scienceMatchedTellsList]
                            if sciObsid not in scienceMatchedTellsList:
                                writeList(sciObsid, 'scienceMatchedTellsList', telobs)
                        writeList(image, 'scienceMatchedTellsList', telobs)
    os.chdir(path)

    # ---------------------------- Tests ------------------------------------- #

    # Don't use tests if user doesn't want them
    tests = True
    if tests:
        # Check that each science observation has valid telluric data.

        # For each science observation:
        for science_directory in obsDirList:
            os.chdir(science_directory)
            # Store science observation name in science_observation_name
            science_observation_name = science_directory.split(os.sep)[-1]
            # Optional: store time of a science frame in science_time.
            try:
                sciImageList = open('scienceFrameList', "r").readlines()
            except IOError:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: science "+str(science_observation_name))
                logging.info("                      in " + str(os.getcwd()))
                logging.info("                      does not have a scienceFrameList.")
                logging.info("                      I am trying to rewrite it with zero point offsets.")
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")

                rewriteSciImageList(2.0, Science)
                try:
                    sciImageList = open('scienceFrameList', "r").readlines()
                    logging.info("\nSucceeded; a science frame list exists in " + str(os.getcwd()))
                except IOError:
                    logging.info("\nWARNING: no science frames found in " + str(os.getcwd()) + ". You may have to adjust the skyThreshold parameter.")
                    raise SystemExit

            sciImageList = [image.strip() for image in sciImageList]
            for science_image in sciImageList:
                scienceDirectory = os.getcwd()
                # Open image and get science image grating from header.
                science_header = astropy.io.fits.open('./'+ science_image + '.fits')
                science_time = timeCalc(science_image+'.fits')
                science_date = science_header[0].header[ 'DATE'].replace('-','')

                # Check that directory obsname matches header obsname.
                temp_obs_name = 'obs' + science_header[0].header['OBSID'][-3:].replace('-','')
                if science_observation_name != temp_obs_name:
                    logging.info("\n#####################################################################")
                    logging.info("#####################################################################")
                    logging.info("")
                    logging.info("     WARNING in sort: science "+str(science_observation_name)+ " :")
                    logging.info("                      observation name data in headers and directory")
                    logging.info("                      do not match.")
                    logging.info("")
                    logging.info("#####################################################################")
                    logging.info("#####################################################################\n")

                # Check that a tellurics directory exists.
                if os.path.exists('../Tellurics/'):
                    os.chdir('../Tellurics/')
                else:
                    logging.info("\n#####################################################################")
                    logging.info("#####################################################################")
                    logging.info("")
                    logging.info("     WARNING in sort: telluric directory for science "+str(science_observation_name))
                    logging.info("                      does not exist.")
                    logging.info("")
                    logging.info("#####################################################################")
                    logging.info("#####################################################################\n")
                    continue
                found_telluric_flag = False

                # Iterate through tellurics observation directories.
                for directory in list(glob.glob('obs*')):
                    os.chdir('./'+directory)
                    # Check that a file, scienceMatchedTellsList exists.
                    try:
                        scienceMatchedTellsList = open('scienceMatchedTellsList', "r").readlines()
                        # Check that the science observation name is in the file.
                        # Check that immediately after is at least one telluric image name.
                        # Do this by checking for the science date in the telluric name.
                        for i in range(len(scienceMatchedTellsList)):
                            telluric_observation_name = scienceMatchedTellsList[i].strip()
                            if telluric_observation_name == science_observation_name:
                                rest_list = [x.strip() for x in scienceMatchedTellsList]
                                if science_image in rest_list:
                                    found_telluric_flag = True
                                    break
                    except IOError:
                        pass

                    if found_telluric_flag:
                        os.chdir('../')
                        break
                    else:
                        os.chdir('../')

                if not found_telluric_flag:
                    os.chdir('../')
                    logging.info("\n#####################################################################")
                    logging.info("#####################################################################")
                    logging.info("")
                    logging.info("     WARNING in sort: no tellurics data found for science "+str(science_image))
                    logging.info("     in " + str(os.getcwd()))
                    logging.info("")
                    logging.info("#####################################################################")
                    logging.info("#####################################################################\n")
                os.chdir(scienceDirectory)
                # TO DO:
                # Optional: open that telluric image and store time in telluric_time
                # Check that abs(telluric_time - science_time) < 1.5 hours

    # ---------------------------- End Tests --------------------------------- #

    os.chdir(path)
    logging.info("\nI am finished matching science images with telluric frames.")
    return


#--------------------------- End of Functions ---------------------------------#

if __name__ == '__main__':
    # Set up logging if called as a standalone script.
    # Format logging options.
    FORMAT = '%(asctime)s %(message)s'
    DATEFMT = datefmt()

    # Set up the logging file.
    logging.basicConfig(filename='nifsSort.log',format=FORMAT,datefmt=DATEFMT,level=logging.DEBUG)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # This lets us logging.info(to stdout AND a logfile. Cool, huh?
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Start nifsSort from the beginning!
    start()
