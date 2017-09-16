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

import time, sys, calendar, astropy.io.fits, urllib, shutil, glob, os, fileinput, logging, smtplib, pkg_resources, math
import numpy as np
from xml.dom.minidom import parseString
from pyraf import iraf

# LOCAL

# Import config parsing.
from configobj.configobj import ConfigObj

# Define constants
# Paths to Nifty data.
RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

# Let us print colors to the terminal!
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#--------------------------------------------------------------------#
#                                                                    #
#     DEFS                                                           #
#                                                                    #
#    Library of non reduction or sorting specific functions          #
#                                                                    #
#    The following functions were taken from the IPM scripts from    #
#    globaldefs.py:                                                  #
#    datefmt, getFitsHeader, FitsKeyEntry, stripString               #
#    stripNumber, getURLFiles                                        #
#                                                                    #
#--------------------------------------------------------------------#


#-----------------------------------------------------------------------------#

def interactiveNIFSInput():
    """
    Get NIFS configuration interactively. This is based on Sphinx's interactive input session.

    """

    logging.info("\nWelcome to Nifty! The current mode is NIFS data reduction.\n\nPress enter to accept default data reduction options.")

    fullReduction = getParam(
                "Do a full data reduction with default parameters loaded from recipes/defaultConfig.cfg? [no]: ",
                False,
                "Type yes to start Nifty with data reduction input parameters loaded from recipes/defaultConfig.cfg file."
    )
    if fullReduction == False:
        # "Select in". User has to turn individual steps on.
        # TODO(nat): Implement these steps.
        date = ""
        program = ""
        copy = ""

        # Get sort params.
        sort = getParam(
        "Sort raw data? [yes]: ",
        'yes',
        "Nifty needs raw data to be in a specific directory structure with text files helping it. " + \
        "You can have it build a structure automatically."
        )
        program = getParam(
        "Gemini Program ID? []: ",
        "",
        "Nifty can either download raw data from the Gemini Public archive (to ./rawData) or copy it from " + \
        "a local directory. An example of a valid program string: \"GN-2013A-Q-62\". "
        )
        rawPath = getParam(
        "Path to raw files directory? []: ",
        "",
        "An example of a valid raw files path string: \"/Users/nat/data/spaceMonster\""
        )
        #
        oneDExtraction = getParam(
        "Do a one D extraction from uncorrected cubes? [yes]: ",
        True,
        "Not implemeted yet"
        )
        extractionXC = getParam(
        "Extraction x coordinate? [15.0]: ",
        15.0,
        "Not implemeted yet"
        )
        extractionYC = getParam(
        "Extraction y coordinate? [33.0]: ",
        33.0,
        "Not implemeted yet"
        )
        extractionRadius = getParam(
        "Extraction y coordinate? [2.5]: ",
        2.5,
        "Not implemeted yet"
        )
        telluricTimeThreshold = getParam(
        "Max time between matched science and standard star frames? [5400]",
        5400,
        "Nifty will try to match science frames with the telluric frame closest to it in UT start time, " + \
        "within a certain threshold (in seconds). The default is 5400 seconds (1.5 hours)."
        )
        skyThreshold = getParam(
        "Sky threshold? [2.0]: ",
        2.0,
        "Nifty differentiates between sky and science frames from the telescope P and Q offsets. " + \
        "If sqrt(Poffset^2 + Qoffset^2) is more than the given threshold, a frame is marked as a science frame. " + \
        "Nifty also tries to take the telescope P and Q offset zero point into account if the first past seems to only identify sky frames."
        )
        # See if we want to reduce the baseline calibrations. And if so, which substeps
        # to perform.
        calibrationReduction = getParam(
        "Reduce baseline calibrations? [yes]: ",
        'yes',
        "NIFS data comes with a set of calibrations that should be reduced and used."
        )
        # By default do all of them.
        baselineCalibrationStart = getParam(
        "Starting point of baseline calibration reductions? [1]: ",
        1,
        "Specify the start step for the reduction of calibrations here."
        )
        baselineCalibrationStop = getParam(
        "Stopping point of baseline calibration reductions? [4]: ",
        4,
        "Specify the stop step for the reduction of calibrations here."
        )
        # Check and get params for a telluric data reduction.
        telluricReduction = getParam(
        "Reduce telluric data? [yes]: ",
        'yes',
        "You can specify to do a telluric data reduction."
        )
        telStart = getParam(
        "Start point? [1]: ",
        1,
        "Starting point of science and telluric reductions."
        )
        telStop = getParam(
        "Stop point? [6]: ",
        6,
        "Stopping point of science and telluric reductions"
        )
        telluricSkySubtraction = getParam(
        "Do a telluric sky subtraction? [yes]: ",
        'yes',
        "Specify to subtract sky frames from telluric frames."
        )
        # Set the telluric application correction method. Choices are iraf.telluric and a python variant.
        # Set the h-line removal method with the vega() function in nifsReduce as default.
        hline_method = getParam(
        "H-line removal method? [vega]: ",
        "none",
        "Nifty can attempt to remove H-lines from a telluric correction spectrum. The available options are \"vega\" and \"none\"."
        )
        # Set yes or no for interactive the h line removal, telluric correction, and continuum fitting

        # Disabled (for now!) because of bugs in interactive Pyraf tasks.
        # TODO(nat): when interactive is fixed re-enable this.
        # Temp fix:
        hlineinter = False
        """hlineinter = getParam(
        "Interative H-line removal? [no]: ",
        False
        )"""
        continuuminter = False
        """continuuminter = getParam(
        "Interative telluric continuum fitting? [no]: ",
        False
        )"""

        telluricCorrectionMethod = getParam(
        "Telluric correction method? [gnirs]: ",
        "gnirs",
        "Specify a telluric correction method or not to apply one. The options are \"gnirs\", \"none\" and \"iraf\"."
        )

        # TODO(nat): disabled for now because of that interactive task bug.
        telinter = False
        """
        telinter = getParam(
        "Interactive telluric correction? [no]: ",
        False
        )"""

        # Check for science as well.
        scienceReduction = getParam(
        "Reduce science data? [yes]: ",
        'yes',
        "Nifty can reduce science data producing UNMERGED 3D data cubes."
        )
        sciStart = getParam(
        "Starting point of science and telluric reductions? [1]: ",
        1,
        "Starting point of science reduction."
        )
        sciStop = getParam(
        "Stopping point of science and telluric reductions? [6]: ",
        6,
        "Stopping point of science reduction."
        )
        scienceSkySubtraction = getParam(
        "Subtract sky frames from science frames? [yes]: ",
        'yes',
        "Nifty can subtract a sky frame of the same exposure duration from each science frame."
        )
        fluxCalibrationMethod = getParam(
        "Flux calibration method? [no]: ",
        "gnirs",
        "Nifty can do a flux calibration. The available options are \"gnirs\" and \"none\"."
        )
        spectemp = getParam(
        "Effective temperature in kelvin of telluric standard star? [""]: ",
        "",
        "You can specify the temperature of the telluric standard star; if not Nifty will attempt " + \
        "a SIMBAD query to find Teff."
        )
        mag = getParam(
        "Magnitude of standard star? [""]: ",
        "",
        "You can specify the magnitude of the telluric standard star. If not Nifty will attempt "+ \
        "a SIMBAD query to look it up."
        )
        mergeUncorrectedCubes = getParam(
        "Merge uncorrected data cubes? [yes]: ",
        'yes',
        "Nifty can also merge cubes in a unique observations to make one final cube per object, per grating."
        )
        mergeTelluricCorrectedCubes = getParam(
        "Merge TELLURIC CORRECTED data cubes? [yes]: ",
        'yes',
        "Nifty can also merge cubes in a unique observations to make one final cube per object, per grating."
        )
        mergeTelCorAndFluxCalibratedCubes = getParam(
        "Merge FLUX CALIBRATED AND TELLURIC CORRECTED data cubes? [yes]: ",
        'yes',
        "Nifty can also merge cubes in a unique observations to make one final cube per object, per grating."
        )
        use_pq_offsets = getParam(
        "Use pq offsets to merge data cubes? [yes]: ",
        "yes",
        "Nifty can merge cubes blindly using telescope P and Q offsets. If not, Nifty will pause and "+ \
        "ask you to first shift cubes by hand (say, in QFitsView) before merging cubes."
        )
        im3dtran = getParam(
        "Transpose cubes for faster merging? [yes]: ",
        'yes',
        "Nifty can transpose cubes to work around a bug in iraf.imcombine(). If not using this, note Nifty " + \
        "will take over 25 minutes to merge each cube."
        )
        over = getParam(
        "Overwrite old files? [no]: ",
        False,
        "Nifty can attempt to overwrite old files. Use with caution; this is very lightly tested."
        )
        manualMode = getParam(
        "Pause after each data reduction step? [no]: ",
        False,
        "Nifty can pause before each major step and routine to make it easier to follow what it is doing."
        )

        # Save the options as a .cfg file.
        config = ConfigObj(RECIPES_PATH+'defaultConfig.cfg', unrepr=True)

        # General config used by all scripts.
        config['over'] = over
        config['manualMode'] = manualMode
        config['oneDExtraction'] = oneDExtraction
        config['extractionXC'] = extractionXC
        config['extractionYC'] = extractionYC
        config['extractionRadius'] = extractionRadius

        config['nifsPipelineConfig'] = {}
        config['nifsPipelineConfig']['sort'] = sort
        config['nifsPipelineConfig']['calibrationReduction'] = calibrationReduction
        config['nifsPipelineConfig']['telluricReduction'] = telluricReduction
        config['nifsPipelineConfig']['scienceReduction'] = scienceReduction

        config['sortConfig'] = {}
        config['sortConfig']['rawPath'] = rawPath
        config['sortConfig']['program'] = program
        config['sortConfig']['skyThreshold'] = skyThreshold
        config['sortConfig']['sortTellurics'] = telluricReduction
        config['sortConfig']['telluricTimeThreshold'] = telluricTimeThreshold
        config['sortConfig']['date'] = date
        config['sortConfig']['copy'] = copy

        config['calibrationReductionConfig'] = {}
        config['calibrationReductionConfig']['baselineCalibrationStart']= baselineCalibrationStart
        config['calibrationReductionConfig']['baselineCalibrationStop'] = baselineCalibrationStop

        config['telluricReductionConfig'] = {}
        config['telluricReductionConfig']['telStart'] = telStart
        config['telluricReductionConfig']['telStop'] = telStop
        config['telluricReductionConfig']['telluricSkySubtraction'] = telluricSkySubtraction
        config['telluricReductionConfig']['spectemp'] = spectemp
        config['telluricReductionConfig']['mag'] = mag
        config['telluricReductionConfig']['hline_method'] = hline_method
        config['telluricReductionConfig']['hlineinter'] = hlineinter
        config['telluricReductionConfig']['continuuminter'] = continuuminter

        config['scienceReductionConfig'] = {}
        config['scienceReductionConfig']['sciStart'] = sciStart
        config['scienceReductionConfig']['sciStop'] = sciStop
        config['scienceReductionConfig']['scienceSkySubtraction'] = scienceSkySubtraction
        config['scienceReductionConfig']['telluricCorrectionMethod'] = telluricCorrectionMethod
        config['scienceReductionConfig']['telinter'] = telinter
        config['scienceReductionConfig']['fluxCalibrationMethod'] = fluxCalibrationMethod
        config['scienceReductionConfig']['mergeUncorrectedCubes'] = mergeUncorrectedCubes
        config['scienceReductionConfig']['mergeTelluricCorrectedCubes'] = mergeTelluricCorrectedCubes
        config['scienceReductionConfig']['mergeTelCorAndFluxCalibratedCubes'] = mergeTelCorAndFluxCalibratedCubes
        config['scienceReductionConfig']['use_pq_offsets'] = use_pq_offsets
        config['scienceReductionConfig']['im3dtran'] = im3dtran

        with open('./config.cfg', 'w') as outfile:
            config.write(outfile)

    return fullReduction

#-----------------------------------------------------------------------------#

def datefmt():
    datefmt = '%Y/%m/%d %H:%M:%S '
    return datefmt

#-----------------------------------------------------------------------------#

def copyCalibration(inputFile, outputFile, grating, over):
    """
    Copy calibrations over to science directories.

    Copies inputFile to outputFile in all ../grating/scienceObservation/obs*/calibrations/ directories.
    """
    # Also copy it over to the relevant science directories.
    for scienceDirectory in glob.glob('../'+grating+'/obs*'):
        # Make sure the cals directory exists.
        if not os.path.exists(scienceDirectory+'/calibrations'):
            os.mkdir(scienceDirectory+'/calibrations')
        # Check if the shift file exists; if not, copy it over.
        if os.path.exists(scienceDirectory+'/calibrations/'+outputFile):
            if over:
                os.remove(scienceDirectory+'/calibrations/'+outputFile)
                shutil.copy(inputFile, scienceDirectory+'/calibrations/'+outputFile)
            else:
                logging.info("\nOutput exists and -over not set - skipping copy of shift file to science directory")
        else:
            shutil.copy(inputFile, scienceDirectory+'/calibrations/'+outputFile)
    # Also copy to telluric directories.
    for telluricDirectory in glob.glob('../'+grating+'/Tellurics/obs*'):
        # Make sure the cals directory exists.
        if not os.path.exists(telluricDirectory+'/calibrations'):
            os.mkdir(telluricDirectory+'/calibrations')
        # Check if the shift file exists; if not, copy it over.
        if os.path.exists(telluricDirectory+'/calibrations/'+outputFile):
            if over:
                os.remove(telluricDirectory+'/calibrations/'+outputFile)
                shutil.copy(inputFile, telluricDirectory+'/calibrations/'+outputFile)
            else:
                logging.info("\nOutput exists and -over not set - skipping copy of shift file to science directory")
        else:
            shutil.copy(inputFile, telluricDirectory+'/calibrations/'+outputFile)

def copyCalibrationDatabase(inputPrefix, grating, over):
    """
    Copy calibrations over to science directories.

    Copies inputPrefix* to all ../grating/scienceObservation/obs*/calibrations/database directories.
    """
    # Also copy it over to the relevant science directories.
    for scienceDirectory in glob.glob('../'+grating+'/obs*'):
        # Make sure the cals directory exists.
        if not os.path.exists(scienceDirectory+'/calibrations'):
            os.mkdir(scienceDirectory+'/calibrations')
        # Make sure the database directory exists
        if os.path.isdir(scienceDirectory+"/calibrations/database"):
            if glob.glob(scienceDirectory+"/calibrations/database/*"):
                if glob.glob(scienceDirectory+"/calibrations/database/"+inputPrefix+"*"):
                    if over:
                        for item in glob.glob(scienceDirectory+"/calibrations/database/"+inputPrefix+"*"):
                            os.remove(item)
                        for item in glob.glob('database/'+inputPrefix+'*'):
                            shutil.copy(item, scienceDirectory+"/calibrations/"+item)
                    else:
                        print "\nOutput exists and -over not set - skipping copy of database directory"
                else:
                    for item in glob.glob('database/'+inputPrefix+'*'):
                        shutil.copy(item, scienceDirectory+"/calibrations/"+item)
            else:
                logging.info("\nWARNING: No database files found.")
                raise SystemExit
        else:
            os.mkdir(scienceDirectory+"/calibrations/database")
            for item in glob.glob('database/'+inputPrefix+'*'):
                shutil.copy(item, scienceDirectory+"/calibrations/"+item)
    # Also copy to telluric directories
    for telluricDirectory in glob.glob('../'+grating+'/Tellurics/obs*'):
        # Make sure the cals directory exists.
        if not os.path.exists(telluricDirectory+'/calibrations'):
            os.mkdir(telluricDirectory+'/calibrations')
        # Make sure the database directory exists
        if os.path.isdir(telluricDirectory+"/calibrations/database"):
            if glob.glob(telluricDirectory+"/calibrations/database/*"):
                if glob.glob(telluricDirectory+"/calibrations/database/"+inputPrefix+"*"):
                    if over:
                        for item in glob.glob(telluricDirectory+"/calibrations/database/"+inputPrefix+"*"):
                            os.remove(item)
                        for item in glob.glob('database/'+inputPrefix+'*'):
                            shutil.copy(item, telluricDirectory+"/calibrations/"+item)
                    else:
                        print "\nOutput exists and -over not set - skipping copy of database directory"
                else:
                    for item in glob.glob('database/'+inputPrefix+'*'):
                        shutil.copy(item, telluricDirectory+"/calibrations/"+item)
            else:
                logging.info("\nWARNING: No database files found.")
                raise SystemExit
        else:
            os.mkdir(telluricDirectory+"/calibrations/database")
            for item in glob.glob('database/'+inputPrefix+'*'):
                shutil.copy(item, telluricDirectory+"/calibrations/"+item)


#-----------------------------------------------------------------------------#

def rewriteSciImageList(threshold, kind):
    """
    Find zero point from first image in skyFrameList
    calculate difference; if larger than threshold, append to new skyFrameList.
    Else append to new scienceFrameList.
    Write out both lists at end.
    """
    skyFrameList = open('skyFrameList', "r").readlines()
    skyFrameList = [image.strip() for image in skyFrameList]
    firstImage = astropy.io.fits.open(skyFrameList[0]+'.fits')
    p0 = firstImage[0].header['POFFSET']
    q0 = firstImage[0].header['QOFFSET']
    r0 = math.sqrt(((p0)**2) + ((q0)**2))
    newSkyFrameList = []
    newScienceFrameList = []
    for item in skyFrameList:
        image = astropy.io.fits.open(item+'.fits')
        poff = image[0].header['POFFSET']
        qoff = image[0].header['QOFFSET']
        pdiff = abs(p0 - poff)
        qdiff = abs(q0 - qoff)
        rdiff = math.sqrt(((pdiff)**2) + ((qdiff)**2))
        if rdiff >= threshold:
            newSkyFrameList.append(item)
        else:
            newScienceFrameList.append(item)
    os.remove("skyFrameList")
    for item in newSkyFrameList:
        writeList(item, 'skyFrameList', './')
        # Create a skyFrameList in the relevant directory.
    if kind == "Science":
        for item in newScienceFrameList:
            writeList(item, 'scienceFrameList', './')
    elif kind == "Telluric":
        for item in newScienceFrameList:
            writeList(item, 'tellist', './')

#-----------------------------------------------------------------------------#

def printDirectoryLists():
    """Print paths to science, telluric and calibration observations.

    Useful for:
        - Making sure sorting worked properly.
        - Making sure pipeline is loading runtimeData/scienceDirectoryList.txt,
          runtimeData/telluricDirectoryList.txt and runtimeData/calibrationDirectoryList.txt
          correctly.
    """
    # Print the current directory of data being reduced.
    logging.info("\nThe following values were found in ./config.cfg: ")

    with open('./config.cfg') as config_file:
        options = ConfigObj(config_file, unrepr=True)
    logging.info("\nScience Directory List: ")
    for i in range(len(options['scienceDirectoryList'])):
        logging.info(options['scienceDirectoryList'][i])
    logging.info("\nTelluric Directory List: ")
    for i in range(len(options['telluricDirectoryList'])):
        logging.info(options['telluricDirectoryList'][i])
    logging.info("\nCalibration Directory List: ")
    for i in range(len(options['calibrationDirectoryList'])):
        logging.info(options['calibrationDirectoryList'][i])

#-----------------------------------------------------------------------------#

def getParam(prompt, default, helpMessage="No help implemented yet!"):
    """Get a parameter from the user interactively. Also sets a default and
    displays a help message if a user types "h" or "help".
    """

    print "\n" + bcolors.OKBLUE + helpMessage + bcolors.ENDC + "\n"
    param = raw_input(prompt)
    if param == "no" or "No" or "N" or "n":
        param == False
    if param == "yes" or "Yes" or "Y" or "n":
        parm = True
    param = param or default

    return param

#-----------------------------------------------------------------------------#

def getFitsHeader(fitsFile, fitsKeyWords):
    """ imported from /astro/sos/da/scisoft/das/daLog/MakeDaDataCheckLogDefs.py """
    selection2 ="fullheader/"+fitsFile
    url2 ="http://fits/" + selection2
    u2 = urllib.urlopen(url2)
    xml2 = u2.read()
    u2.close()
    fitsHeaderList = [fitsFile[:-5]]
    for entry in fitsKeyWords:
        myOut = FitsKeyEntry(entry, xml2)
        fitsHeaderList.append(myOut)
    #
    return fitsHeaderList

#-----------------------------------------------------------------------------#

def FitsKeyEntry(fitsKeyWd, fullheader):
    """ imported from /astro/sos/da/scisoft/das/daLog/MakeDaDataCheckLogDefs.py """
    selectEntry ="none found"
    fullList = fullheader.splitlines()
    checkKeyWd = fitsKeyWd.ljust(8,' ')
    for index in range(len(fullList)):
        if fullList[index][:8] == checkKeyWd:
            if fullList[index][10] == "'":
                selectEntry = stripString(fullList[index])
            else:
                selectEntry = stripNumber(fullList[index])
    return selectEntry

#-----------------------------------------------------------------------------#

def stripString(inputString):
    """ imported from /astro/sos/da/scisoft/das/daLog/MakeDaDataCheckLogDefs.py """

    delimString ="'"
    delimList = []
    for index in range(len(inputString)):
        if inputString[index] == delimString:
            delimList.append(index)
    outFull = inputString[delimList[0]+1:delimList[-1]]
    outPut = outFull.replace(" ","")
    #
    return outPut

#-----------------------------------------------------------------------------#

def stripNumber(inputString):
    """ imported from /astro/sos/da/scisoft/das/daLog/MakeDaDataCheckLogDefs.py
    """
    delim1 ="="
    delim2 ="/"
    delimList = []
    for index in range(len(inputString)):
        if inputString[index] == delim1:
            delimList.append(index)
        if inputString[index] == delim2:
            delimList.append(index)
    if len(delimList) == 1:
        delimList.append(index)
    outFull = inputString[delimList[0]+1:delimList[1]]
    outPut = float(outFull)
    #
    return outPut

#-----------------------------------------------------------------------------#

def getUrlFiles(url,tag):
    """ imported from IPM scripts globaldefs.py """
    u = urllib.urlopen(url)
    xml = u.read()
    u.close()
    dom = parseString(xml)

    # Get file list:
    fileList = []
    previousFilename =""
    for fe in dom.getElementsByTagName(tag):
        fitsFile = str(fe.getElementsByTagName('filename')[0].childNodes[0].data)
        # exclude consecutive duplicates:
        if fitsFile != previousFilename:
            fileList.append(fitsFile)
            previousFilename = fitsFile

    #Return file list:
    return fileList

#-----------------------------------------------------------------------------#

def checkOverCopy(filelist, path, over):
    """ checks if over is True or False and copies files from /net/mko-nfs/sci/dataflo
    based on this.
    """

    rawfiles = []
    missingRaw = []

    raw = '/net/mko-nfs/sci/dataflo'


    for entry in filelist:
        if glob.glob(path+'/'+entry):
            rawfiles.append(glob.glob(path+'/'+entry))
        else:
            missingRaw.append(entry)

    if rawfiles:
        if over:
            for entry in rawfiles:
                if os.path.exists(entry[0]):
                    os.remove(entry[0])
            # copy all science images from a given night into ./Raw/
            for entry in filelist:
                if os.path.exists(raw+'/'+entry):
                    shutil.copy(raw+'/'+entry, path)
                else:
                    logging.info('SKIPPED ', entry)
        else:
            for entry in missingRaw:
                if os.path.exists(raw+'/'+entry):
                    shutil.copy(raw+'/'+entry, path)
                else:
                    logging.info('SKIPPED ', entry)

    else:
        for entry in filelist:
            if os.path.exists(raw+'/'+entry):
                shutil.copy(raw+'/'+entry, path)
            else:
                logging.info('SKIPPED ', entry)

    return

#-----------------------------------------------------------------------------#

def checkQAPIreq(alist):
    """ checks to make sure that the arcs meet the PI and QA requirements """

    blist = []
    for entry in alist:
        blist.append(entry)
    for i in range(len(alist)):
        fitsKeyWords = ['RAWPIREQ', 'RAWGEMQA']
        headerList = getFitsHeader(alist[i], fitsKeyWords)
        rawPIreq = headerList[1]
        rawGemQA = headerList[2]
        if rawPIreq in ["YES","UNKNOWN"] and rawGemQA in ["USABLE","UNKNOWN"]:
            logging.info(alist[i]+' added for processing')
        else:
            logging.info(alist[i]+' excluded, set to USABLE/FAIL')
            blist.remove(alist[i])

    return blist

#-----------------------------------------------------------------------------#

def listit(list, prefix):
    """ Returns a string where each element of list is prepended with prefix """

    l = []
    for x in list:
        l.append(prefix+(x.strip()).rstrip('.fits'))
    return ",".join(l)

#-----------------------------------------------------------------------------#

def checkDate(list):
    """ check the dates on all the telluric and acquisition files to make sure that
        there are science images on the same night
    """

    removelist = []
    datelist = []

    for entry in list:
        fitsKeyWords = ['DATE', 'OBSCLASS']
        header = getFitsHeader(entry, fitsKeyWords)
        date = header[1]
        obsclass = header[2]
        if obsclass=='science':
            if not datelist or not datelist[-1]==date:
                datelist.append(date)

    for entry in list:
        fitsKeyWords = ['DATE', 'OBSCLASS']
        header = getFitsHeader(entry, fitsKeyWords)
        date = header[1]
        obsclass = header[2]
        if not obsclass=='science' and date not in datelist:
            removelist.append(entry)

    return removelist

#-----------------------------------------------------------------------------#

def writeList(image, file, path):
    """ write image name into a file """
    homepath = os.getcwd()
    os.chdir(path)
    image = image.rstrip('.fits')
    if os.path.exists(file):
        filelist = open(file, 'r').readlines()
        if image+'\n' in filelist or not filelist:
            f = open(file, 'w')
            f.write(image+'\n')
        else:
            f = open(file, 'a')
            f.write(image+'\n')
    else:
        f = open(file, 'a')
        f.write(image+'\n')
    f.close()
    os.chdir(homepath)

#-----------------------------------------------------------------------------#

def checkEntry(entry, entryType, filelist):
    """ checks to see the that program ID given matches the OBSID in the science headers
        checks to see that the date given matches the date in the science headers
    """

    if entryType == 'program':
        header = getFitsHeader(filelist[0], ['OBSID'])
        if entry in header[1]:
            pass
        else:
            logging.info("\n Program number was entered incorrectly.\n")
            raise SystemExit

    if entryType == 'date':
        header = getFitsHeader(filelist[0], ['DATE'])
        if entry in header[1].replace('-',''):
            pass
        else:
            logging.info("\n Date was entered incorrectly or there is no NIFS data for the date given. Please make sure the date has been entered as such: YYYYDDMM.\n")
            raise SystemExit

#-----------------------------------------------------------------------------#

def checkLists(original_list, path, prefix, suffix):
    """Check that all files made it through an iraf step. """

    new_list = []
    for image in original_list:
        image = image.strip()
        if os.path.exists(path+'/'+prefix+image+suffix):
            new_list.append(image)
        else:
            logging.info('\n' +  str(image)+ '.fits not being processed due to error in image.\n')
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING: " + str(image) + " .fits was removed from a list after a checkLists call.")
            logging.info("               An iraf task may have failed. ")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")


            pass

    return new_list

#-----------------------------------------------------------------------------#

def checkSameLengthFlatLists():
    """Reads two textfile lists of filenames. If not the same length,
    removes last entry from longer list until they are. Prints loud warnings to
    tell people it is doing this.
    This is done because it was found nsflat() complains when the gain of Combined
    lamps-on flats does not match the gain of combined lamps-off flats.
    This is caused when different numbers of flats combined into one combined frame.
    It seemed simplest to exclude one of the darks. Feel free to attempt a more complicated
    fix!
    """
    # Read the flatlist into a python list.
    with open('./flatlist', 'r') as f:
        flatlist = f.readlines()
    # Read the flatdarklist into a python list.
    with open('./flatdarklist', 'r') as f:
        flatdarklist = f.readlines()
    # Check that both lists are the same length.
    if len(flatlist) != len(flatdarklist):
        # Print a nice loud warning.
        logging.info("\n#####################################################################")
        logging.info("#####################################################################")
        logging.info("")
        logging.info("     WARNING in sort: flatlist and flatdarklist are not the same ")
        logging.info("                      length. Removing extra entries from the")
        logging.info("                      longer list. Original lists can be found in")
        logging.info("                      original_flatlist and original_flatdarklist")
        logging.info("     in " + str(os.getcwd()))
        logging.info("")
        logging.info("#####################################################################")
        logging.info("#####################################################################\n")
        # Copy the original flatlist and flatdarklist to backup files.
        shutil.copy2('./flatlist', './original_flatlist')
        shutil.copy2('./flatdarklist', './original_flatdarklist')
        # while they are not the same length:
        while len(flatlist) != len(flatdarklist):
            # remove the last entry from the longer list.
            if len(flatlist) > len(flatdarklist):
                del flatlist[-1]
            else:
                del flatdarklist[-1]
        # Write the new flatlist to the flatlist textfile, overwriting anything already there.
        with open('./flatlist', 'w') as f:
            for item in flatlist:
                f.write(item)
        # Write the new flatdarklist to the flatdarklist textfile, overwriting anything already there.
        with open('./flatdarklist', 'w') as f:
            for item in flatdarklist:
                f.write(item)

#-----------------------------------------------------------------------------#

def makeSkyList(skyFrameList, sciencelist, obsDir):
    """ Makes a skyFrameList equal in length to object list with sky and object
    frames closest in time at equal indices.

    Writes the original skyFrameList to original_skyFrameList.

    Writes results to skyFrameList textfile.

    Returns:
        skyFrameList (list): list of sky frames organized so each science frame has subtracted
                        the sky frame closest in time.

    Eg:
        Observations had an ABA ABA pattern:
            obs1
            sky1
            obs2

            obs3
            sky2
            obs4

            obs5
            sky3
            obs6

        sciencelist was:    skyFrameList was:   Output skyFrameList will be:
            obs1                    sky1            sky1
            obs2                    sky2            sky1
            obs3                    sky3            sky2
            obs4                                    sky2
            obs5                                    sky3
            obs6                                    sky3

        Observations had an AB AB AB pattern:
            obs1
            sky1
            obs2
            sky2
            obs3
            sky3

        sciencelist was:    skyFrameList was:   Output skyFrameList will be:
            obs1                    sky1            sky1
            obs2                    sky2            sky1
            obs3                    sky3            sky2
    """
    logging.info("\n#############################################################")
    logging.info("#                                                           #")
    logging.info("#  Matching science frames with sky frames closest in time  #")
    logging.info("#                                                           #")
    logging.info("#############################################################\n")
    # Do some tests first.
    # Check that data is either:
    # ABA ABA ABA- one sky frame per two science frames.
    # AB AB AB- one sky frame per one two science frames.
    #
    # If it is neither warn user to verify that sky frames were matched with science frames correctly.
    if len(skyFrameList) != len(sciencelist)/2 and len(skyFrameList) != len(sciencelist):
        logging.info("\n#####################################################################")
        logging.info("#####################################################################")
        logging.info("")
        logging.info("     WARNING in reduce: it appears science frames and sky frames were not")
        logging.info("                        taken in an ABA ABA or AB AB pattern.")
        logging.info("")
        logging.info("#####################################################################")
        logging.info("#####################################################################\n")
    skytimes = []
    prepared_sky_list = []
    # Calculate time of each sky frame. Store the calculated time and the frame name in skytimes, a
    # 2D list of [skyframe_time, skyframe_name] pairs.
    # Eg: [[39049.3, 'N20130527S0241'], [39144.3, 'N20130527S0244'], [39328.8, 'N20130527S0247'], [39590.3, 'N20130527S0250']]
    for item in skyFrameList:
        # Strip off the trailing newline.
        item = str(item).strip()
        # Calculate the time of the sky frame.
        skytime = timeCalc(item+'.fits')
        # Store the sky frame time and corresponding sky frame name in skytimes.
        templist = [skytime, item]
        skytimes.append(templist)
    logging.info("scienceframelist:      skyFrameList:      time delta (between observation UT start times from .fits headers):")
    for item in sciencelist:
        # Calculate time of the science frame in seconds.
        item = str(item).strip()
        sciencetime = timeCalc(item+'.fits')
        # Sort the 2D list of [skyframe_time, skyframe_name] pairs by absolute science_frame_time - skyframe_time.
        # Eg: [[39049.3, 'N20130527S0241'], [39144.3, 'N20130527S0244'], [39328.8, 'N20130527S0247'], [39590.3, 'N20130527S0250']]
        sorted_by_closest_time = sorted(skytimes, key=lambda x: (abs(sciencetime - x[0])))
        # Append the name corresponding to the minimum time difference to prepared_sky_list.
        prepared_sky_list.append(sorted_by_closest_time[0][1])
        # Print the scienceframe, matching skyframe and time difference side by side for later comparison.
        logging.info("  "+ str(item)+ "       "+ str(sorted_by_closest_time[0][1])+ "        "+ str(abs(sciencetime - sorted_by_closest_time[0][0])))
    logging.info("\n")

    os.rename('skyFrameList', 'original_skyFrameList')

    f = open('skyFrameList', 'w')
    for image in prepared_sky_list:
        f.write(image+'\n')
    f.close()

    return prepared_sky_list

#-----------------------------------------------------------------------------#


def convertRAdec(ra, dec):
    """ converts RA from degrees to H:M:S and dec from degrees to degrees:arcmin:arcsec"""
    H = int(ra/15.)
    M = int((ra-(15*H))/.25)
    S = ((ra-(float(H)*15.))-(float(M)*.25))/(1./240.)

    ra = str(H)+'h'+str(M)+'m'+str(S)+'s'

    return ra

#-----------------------------------------------------------------------------#

def timeCalc(image):
    """Read time from .fits header. Convert to a float of seconds.
    """
    telheader = astropy.io.fits.open(image)
    UT = telheader[0].header['UT']
    secs = float(UT[6:10])
    mins = float(UT[3:5])
    hours = float(UT[0:2])
    time = secs+mins*60.+hours*(60.*60.)

    return time

#-----------------------------------------------------------------------------#

def MEFarithpy(MEF, image, op, result):

    if os.path.exists(result):
        os.remove(result)
    scimage = astropy.io.fits.open(MEF+'.fits')
    arithim = astropy.io.fits.open(image+'.fits')
    for i in range(88):
        if scimage[i].name=='SCI':
            if op=='multiply':
                scimage[i]=scimage[i]*arithim
            if op=='divide':
                scimage[i]=scimage[i]/arithim
    scimage.writeto(result, output_verify='ignore')
#-----------------------------------------------------------------------------#

def MEFarith(MEF, image, op, result):

    if os.path.exists(result):
        os.remove(result)
    iraf.fxcopy(input=MEF+'[0]', output=result)
    for i in range(1,88):
        iraf.fxinsert(input=MEF+'['+str(i)+']', output=result+'['+str(i)+']', groups='', verbose = 'no')
    for i in range(1,88):
        header = astropy.io.fits.open(result)
        extname = header[i].header['EXTNAME']
        if extname == 'SCI':
            iraf.imarith(operand1=result+'['+str(i)+']', op=op, operand2 = image, result = result+'['+str(i)+', overwrite]', divzero = 0.0)

#-----------------------------------------------------------------------------#
