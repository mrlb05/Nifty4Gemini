#!/usr/bin/env python

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

import sys, glob, shutil, getopt, os, time, logging, glob, sgmllib, urllib, re, traceback, pkg_resources
import pexpect as p
from pyraf import iraf, iraffunctions
import astropy.io.fits
from astropy.io.fits import getdata, getheader
import numpy as np
from scipy.interpolate import interp1d
from scipy import arange, array, exp
from scipy.ndimage.interpolation import shift
import pylab as pl
import matplotlib.pyplot as plt

# LOCAL

# Import config parsing.
from ..configobj.configobj import ConfigObj
# Import custom Nifty functions.
from ..nifsUtils import datefmt, listit, writeList, checkLists, makeSkyList, MEFarith, convertRAdec, copyResultsToScience

# Define constants
# Paths to Nifty data.
RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

def start(kind, telluricDirectoryList="", scienceDirectoryList=""):
    """

    start(kind): Do a full reduction of either Science or Telluric data.

    nifsReduce- for the telluric and science data reduction.

    Reduces NIFS telluric and science frames and attempts a flux calibration.

    Parameters are loaded from runtimeData/config.cfg. This script will
    automatically detect if it is being run on telluric data or science data.

    There are 6 steps.

    INPUT:
    + Raw files
        - Science frames
        - Sky frames
    + Calibration files
        - MDF shift file
        - Bad Pixel Mask (BPM)
        - Flat field frame
        - Reduced arc frame
        - Reduced ronchi mask frame
        - arc and ronchi database/ files

    OUTPUT:
        - If telluric reduction an efficiency spectrum used to telluric correct and absolute flux
          calibrate science frames
        - If science reduction a reduced science data cube.

    Args:
        kind (string): either 'Telluric' or 'Science'.
        telluricDirectoryList (string): Used by low memory pipeline.
        scienceDirectoryList (string): Used by low memory pipeline.

    """

    # TODO(nat): Right now the pipeline will crash if you decide to skip, say, doing a bad
    # pixel correction. This is because each step adds a prefix to the frame name, and most following
    # steps depend on that prefix being there.
    # One way to fix this is if a step is to be skipped, iraf.copy() is called instead to copy the frame and
    # add the needed prefix. Messy but it might work for now.

    ###########################################################################
    ##                                                                       ##
    ##                  BEGIN - GENERAL REDUCTION SETUP                      ##
    ##                                                                       ##
    ###########################################################################

    # Store current working directory for later use.
    path = os.getcwd()

    # Set up the logging file.
    log = os.getcwd()+'/Nifty.log'

    logging.info('\n#################################################')
    logging.info('#                                               #')
    logging.info('# Start the NIFS Science and Telluric Reduction #')
    logging.info('#                                               #')
    logging.info('#################################################\n')

    # Set up/prepare IRAF.
    iraf.gemini()
    iraf.gemtools()
    iraf.gnirs()
    iraf.nifs()

    # Reset to default parameters the used IRAF tasks.
    iraf.unlearn(iraf.gemini,iraf.gemtools,iraf.gnirs,iraf.nifs,iraf.imcopy)

    # From http://bishop.astro.pomona.edu/Penprase/webdocuments/iraf/beg/beg-image.html:
    # Before doing anything involving image display the environment variable
    # stdimage must be set to the correct frame buffer size for the display
    # servers (as described in the dev$graphcap file under the section "STDIMAGE
    # devices") or to the correct image display device. The task GDEVICES is
    # helpful for determining this information for the display servers.
    iraf.set(stdimage='imt2048')

    # Prepare the IRAF package for NIFS.
    # NSHEADERS lists the header parameters used by the various tasks in the
    # NIFS package (excluding headers values which have values fixed by IRAF or
    # FITS conventions).
    iraf.nsheaders("nifs",logfile=log)

    # Set clobber to 'yes' for the script. This still does not make the gemini
    # tasks overwrite files, so:
    # YOU WILL LIKELY HAVE TO REMOVE FILES IF YOU RE_RUN THE SCRIPT.
    user_clobber=iraf.envget("clobber")
    iraf.reset(clobber='yes')

    # This helps make sure all variables are initialized to prevent bugs.
    scienceSkySubtraction = None
    oneDExtraction = None
    extractionXC = None
    extractionYC = None
    extractionRadius = None
    telluricSkySubtraction = None

    # Load reduction parameters from runtimeData/config.cfg.
    with open('./config.cfg') as config_file:
        config = ConfigObj(config_file, unrepr=True)
        # Read general pipeline config.
        over = config['over']
        manualMode = config['manualMode']
        calDirList = config['calibrationDirectoryList']
        oneDExtraction = config['oneDExtraction']
        extractionXC = config['extractionXC']
        extractionYC = config['extractionYC']
        extractionRadius = config['extractionRadius']

        if kind == 'Telluric':
            # Telluric reduction specific config.
            telluricReductionConfig = config['telluricReductionConfig']
            if telluricDirectoryList:
                observationDirectoryList = telluricDirectoryList
            elif not telluricDirectoryList:
                observationDirectoryList = config['telluricDirectoryList']
            start = telluricReductionConfig['telStart']
            stop = telluricReductionConfig['telStop']
            telluricSkySubtraction = telluricReductionConfig['telluricSkySubtraction']

        if kind == 'Science':
            # Science reduction specific config.
            scienceReductionConfig = config['scienceReductionConfig']
            if scienceDirectoryList:
                observationDirectoryList = scienceDirectoryList
            elif not scienceDirectoryList:
                observationDirectoryList = config['scienceDirectoryList']
            start = scienceReductionConfig['sciStart']
            stop = scienceReductionConfig['sciStop']
            scienceSkySubtraction = scienceReductionConfig['scienceSkySubtraction']

    ###########################################################################
    ##                                                                       ##
    ##                 COMPLETE - GENERAL REDUCTION SETUP                    ##
    ##                                                                       ##
    ###########################################################################

    # nifsReduce has two nested loops that reduced data.
    # It loops through each science (or telluric) directory, and
    # runs through a series of calibrations steps on the data in that directory.

    # Loop through all the observation (telluric or science) directories to perform a reduction on each one.
    for observationDirectory in observationDirectoryList:

        ###########################################################################
        ##                                                                       ##
        ##                  BEGIN - OBSERVATION SPECIFIC SETUP                   ##
        ##                                                                       ##
        ###########################################################################

        # Print the current directory of data being reduced.
        logging.info("\n#################################################################################")
        logging.info("                                   ")
        logging.info("  Currently working on reductions in")
        logging.info("  in "+ str(observationDirectory))
        logging.info("                                   ")
        logging.info("#################################################################################\n")

        os.chdir(observationDirectory)
        tempObs = observationDirectory.split(os.sep)
        obsid = tempObs[-1]

        # Change the iraf directory to the current directory.
        pwd = os.getcwd()
        iraffunctions.chdir(pwd)

        # Copy relevant calibrations over to the science directory.
        # Open and store the name of the MDF shift reference file from shiftfile into shift.
        shift = 'calibrations/shiftFile'
        # Open and store the name of the flat frame
        flat = 'calibrations/finalFlat'
        # Open and store the bad pixel mask
        finalBadPixelMask = 'calibrations/finalBadPixelMask'
        # Ronchi, arc and database must all be in local calibrations directory
        # Open and store the name of the reduced spatial correction ronchi flat frame name from ronchifile in ronchi.
        ronchi = 'finalRonchi'
        # Open and store the name of the reduced wavelength calibration arc frame from arclist in arc.
        arc = 'finalArc'

        if os.path.exists(os.getcwd()+'/'+ronchi+".fits"):
            if over:
                iraf.delete(os.getcwd()+'/calibrations/finalRonchi.fits')
                # Copy the spatial calibration ronchi flat frame from Calibrations_grating to the observation directory.
                shutil.copy(os.getcwd()+'/calibrations/finalRonchi.fits', ronchi+'.fits')
            else:
                print "\nOutput exists and -over not set - skipping copy of reduced ronchi"
        else:
            shutil.copy(os.getcwd()+'/calibrations/finalRonchi.fits', ronchi+'.fits')

        if os.path.exists(os.getcwd()+'/'+arc+".fits"):
            if over:
                iraf.delete(os.getcwd()+'/calibrations/finalArc.fits')
                # Copy the spatial calibration arc flat frame from Calibrations_grating to the observation directory.
                shutil.copy(os.getcwd()+'/calibrations/finalArc.fits', arc+'.fits')
            else:
                print "\nOutput exists and -over not set - skipping copy of reduced arc"
        else:
            shutil.copy(os.getcwd()+'/calibrations/finalArc.fits', arc+'.fits')
        # Make sure the database files are in place. Current understanding is that
        # these should be local to the reduction directory, so need to be copied from
        # the calDir.
        if os.path.isdir("./database"):
            if over:
                shutil.rmtree("./database")
                os.mkdir("./database")
                for item in glob.glob("calibrations/database/*"):
                    shutil.copy(item, "./database/")
            else:
                print "\nOutput exists and -over not set - skipping copy of database directory"
        else:
            os.mkdir('./database/')
            for item in glob.glob("calibrations/database/*"):
                shutil.copy(item, "./database/")

        if telluricSkySubtraction or scienceSkySubtraction:
            # Read the list of sky frames in the observation directory.
            try:
                skyFrameList = open("skyFrameList", "r").readlines()
                skyFrameList = [frame.strip() for frame in skyFrameList]
            except:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in reduce: No sky frames were found in a directory.")
                logging.info("              Please make a skyFrameList in: " + str(os.getcwd()))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
                raise SystemExit
            sky = skyFrameList[0]

        # If we are doing a telluric reduction, open the list of telluric frames in the observation directory.
        # If we are doing a science reduction, open the list of science frames in the observation directory.
        if kind == 'Telluric':
            tellist = open('tellist', 'r').readlines()
            tellist = [frame.strip() for frame in tellist]
        elif kind == 'Science':
            scienceFrameList = open("scienceFrameList", "r").readlines()
            scienceFrameList = [frame.strip() for frame in scienceFrameList]
            # For science frames, check to see if the number of sky frames matches the number of science frames.
            # IF NOT duplicate the sky frames and rewrite the sky file and skyFrameList.
            if scienceSkySubtraction:
                if not len(skyFrameList)==len(scienceFrameList):
                    skyFrameList = makeSkyList(skyFrameList, scienceFrameList, observationDirectory)

        ###########################################################################
        ##                                                                       ##
        ##                 COMPLETE - OBSERVATION SPECIFIC SETUP                 ##
        ##                BEGIN DATA REDUCTION FOR AN OBSERVATION                ##
        ##                                                                       ##
        ###########################################################################

        # Check start and stop values for reduction steps. Ask user for a correction if
        # input is not valid.
        valindex = start
        while valindex > stop  or valindex < 1 or stop > 6:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in reduce: invalid start/stop values of observation")
            logging.info("                           reduction steps.")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

            valindex = int(raw_input("\nPlease enter a valid start value (1 to 7, default 1): "))
            stop = int(raw_input("\nPlease enter a valid stop value (1 to 7, default 7): "))

        while valindex <= stop :

            ###########################################################################
            ##  STEP 1: Prepare raw data; science, telluric and sky frames ->n       ##
            ###########################################################################

            if valindex == 1:
                if manualMode:
                    a = raw_input("About to enter step 1: locate the spectrum.")
                if kind=='Telluric':
                    tellist = prepare(tellist, shift, finalBadPixelMask, log, over)
                elif kind=='Science':
                    scienceFrameList = prepare(scienceFrameList, shift, finalBadPixelMask, log, over)
                if telluricSkySubtraction or scienceSkySubtraction:
                    skyFrameList = prepare(skyFrameList, shift, finalBadPixelMask, log, over)
                logging.info("\n##############################################################################")
                logging.info("")
                logging.info("  STEP 1: Locate the Spectrum (and prepare raw data) ->n - COMPLETED ")
                logging.info("")
                logging.info("##############################################################################\n")

            ###########################################################################
            ##  STEP 2: Sky Subtraction ->sn                                         ##
            ###########################################################################

            elif valindex == 2:
                if manualMode:
                    a = raw_input("About to enter step 2: sky subtraction.")
                # Combine telluric sky frames.
                if kind=='Telluric':
                    if telluricSkySubtraction:
                        if len(skyFrameList)>1:
                            combineImages(skyFrameList, "gn"+sky, log, over)
                        else:
                            copyImage(skyFrameList, 'gn'+sky+'.fits', over)
                        skySubtractTel(tellist, "gn"+sky, log, over)
                    else:
                        for image in tellist:
                            iraf.copy('n'+image+'.fits', 'sn'+image+'.fits')

                if kind=='Science':
                    if scienceSkySubtraction:
                        skySubtractObj(scienceFrameList, skyFrameList, log, over)
                    else:
                        for image in scienceFrameList:
                            iraf.copy('n'+image+'.fits', 'sn'+image+'.fits')

                logging.info("\n##############################################################################")
                logging.info("")
                logging.info("  STEP 2: Sky Subtraction ->sn - COMPLETED ")
                logging.info("")
                logging.info("##############################################################################\n")

            ##############################################################################
            ##  STEP 3: Flat field, slice, subtract dark and correct bad pixels ->brsn  ##
            ##############################################################################

            elif valindex == 3:
                if manualMode:
                    a = raw_input("About to enter step 3: flat fielding and bad pixels correction.")
                if kind=='Telluric':
                    applyFlat(tellist, flat, log, over, kind)
                    fixBad(tellist, log, over)
                elif kind=='Science':
                    applyFlat(scienceFrameList, flat, log, over, kind)
                    fixBad(scienceFrameList, log, over)
                logging.info("\n##############################################################################")
                logging.info("")
                logging.info("  STEP 3: Flat fielding and Bad Pixels Correction ->brsn - COMPLETED ")
                logging.info("")
                logging.info("##############################################################################\n")


            ###########################################################################
            ##  STEP 4: Derive and apply 2D to 3D transformation ->tfbrsn            ##
            ###########################################################################

            elif valindex == 4:
                if manualMode:
                    a = raw_input("About to enter step 4: 2D to 3D transformation and Wavelength Calibration.")
                if kind=='Telluric':
                    fitCoords(tellist, arc, ronchi, log, over, kind)
                    transform(tellist, log, over)
                elif kind=='Science':
                    fitCoords(scienceFrameList, arc, ronchi, log, over, kind)
                    transform(scienceFrameList, log, over)
                logging.info("\n##############################################################################")
                logging.info("")
                logging.info("  STEP 4: 2D to 3D transformation and Wavelength Calibration ->tfbrsn - COMPLETED ")
                logging.info("")
                logging.info("##############################################################################\n")

            ############################################################################
            ##  STEP 5 (tellurics): For telluric data derive a telluric               ##
            ##                     correction ->gxtfbrsn                              ##
            ##  STEP 5 (science): For science apply an efficiency correction and make ##
            ##           a data cube (not necessarily in that order).                 ##
            ##           (i) Python method applies correction to nftransformed cube.  ##
            ##           Good for faint objects.                        ->cptfbrsn    ##
            ##           (ii) iraf.telluric method applies correction to              ##
            ##           nftransformed result (not quite a data cube) then            ##
            ##           nftransforms cube.                             ->catfbrsn    ##
            ##           (iii) If no telluric correction/flux calibration to be       ##
            ##           applied make a plain data cube.                ->ctfbrsn     ##
            ############################################################################

            elif valindex == 5:
                if manualMode:
                    a = raw_input("About to enter step 5.")
                # For telluric data:
                # Make a combined extracted 1D standard star spectrum.
                if kind=='Telluric':
                    extractOneD(tellist, kind, log, over, extractionXC, extractionYC, extractionRadius)

                    # TODO(nat): add this as a parameter; encapsulate this.
                    copyToScience = True
                    if copyToScience:
                        # Copy final extracted results to science directory.
                        try:
                            with open("scienceMatchedTellsList", "r") as f:
                                lines = f.readlines()
                            lines = [x.strip() for x in lines]

                            for i in range(len(lines)):
                                if "obs" in lines[i]:
                                    k = 1
                                    while i+k != len(lines) and "obs" not in lines[i+k]:
                                        copyResultsToScience("gxtfbrsn"+tellist[0]+".fits", "0_tel"+lines[i+k]+".fits", over)
                                        k+=1
                        except IOError:
                            logging.info("\nNo scienceMatchedTellsList found in "+ os.getcwd() +" . Skipping copy of extracted spectra to science directory.")

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 5a: Extract 1D Spectra and Make Combined 1D Standard Star Spectrum")
                    logging.info("           ->gxtfbrsn - COMPLETED")
                    logging.info("")
                    logging.info("##############################################################################\n")
                    #TODO(nat): add this as a parameter.
                    makeTelluricCube = True
                    if makeTelluricCube:
                        makeCube('tfbrsn', tellist, log, over)
                        logging.info("\n##############################################################################")
                        logging.info("")
                        logging.info("  STEP 5b: Make uncorrected standard star data cubes, ->ctfbrsn  - COMPLETED")
                        logging.info("")
                        logging.info("##############################################################################\n")

                # For Science data:
                # Possibly extract 1D spectra, and make uncorrected cubes.
                elif kind=='Science':
                    if oneDExtraction:
                        extractOneD(scienceFrameList, kind, log, over, extractionXC, extractionYC, extractionRadius)
                        copyExtracted(scienceFrameList, over)
                        logging.info("\n##############################################################################")
                        logging.info("")
                        logging.info("  STEP 5a: Make extracted 1D Science spectra, ->ctgbrsn  - COMPLETED")
                        logging.info("")
                        logging.info("##############################################################################\n")
                    makeCube('tfbrsn', scienceFrameList, log, over)

                    # TODO(nat): encapsulate this inside a function.
                    if os.path.exists('products_uncorrected'):
                        if over:
                            shutil.rmtree('products_uncorrected')
                            os.mkdir('products_uncorrected')
                        else:
                            logging.info("\nOutput exists and -over not set - skipping creating of products_uncorrected directory")
                    else:
                        os.mkdir('products_uncorrected')
                    for item in scienceFrameList:
                        if os.path.exists('products_uncorrected/ctfbrsn'+item+'.fits'):
                            if over:
                                os.remove('products_uncorrected/ctfbrsn'+item+'.fits')
                                shutil.copy('ctfbrsn'+item+'.fits', 'products_uncorrected/ctfbrsn'+item+'.fits')
                            else:
                                logging.info("\nOutput exists and -over not set - skipping copy of uncorrected cube")
                        else:
                            shutil.copy('ctfbrsn'+item+'.fits', 'products_uncorrected/ctfbrsn'+item+'.fits')

                    if os.path.exists('products_telluric_corrected'):
                        if over:
                            shutil.rmtree('products_telluric_corrected')
                            os.mkdir('products_telluric_corrected')
                        else:
                            logging.info("\nOutput exists and -over not set - skipping creating of products_telluric_corrected directory")
                    else:
                        os.mkdir('products_telluric_corrected')
                    for item in scienceFrameList:
                        if os.path.exists('products_telluric_corrected/ctfbrsn'+item+'.fits'):
                            if over:
                                os.remove('products_telluric_corrected/ctfbrsn'+item+'.fits')
                                shutil.copy('ctfbrsn'+item+'.fits', 'products_telluric_corrected/ctfbrsn'+item+'.fits')
                            else:
                                logging.info("\nOutput exists and -over not set - skipping copy of uncorrected cube")
                        else:
                            shutil.copy('ctfbrsn'+item+'.fits', 'products_telluric_corrected/ctfbrsn'+item+'.fits')


                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 5b: Make uncorrected science data cubes, ->ctfbrsn  - COMPLETED")
                    logging.info("")
                    logging.info("##############################################################################\n")

            valindex += 1

        logging.info("\n##############################################################################")
        logging.info("")
        logging.info("  COMPLETE - Reductions completed for " + str(observationDirectory))
        logging.info("")
        logging.info("##############################################################################\n")

    # Return to directory script was begun from.
    os.chdir(path)

##################################################################################################################
#                                                     ROUTINES                                                   #
##################################################################################################################

def prepare(inlist, shiftima, finalBadPixelMask, log, over):
    """Prepare list of frames using iraf.nfprepare. Output: -->n.

    Processing with NFPREPARE (this task is used only for NIFS data
    but other instruments have their own preparation tasks
    with similar actions) will rename the data extension and add
    variance and data quality extensions. By default (see NSHEADERS)
    the extension names are SCI for science data, VAR for variance, and
    DQ for data quality (0 = good). Generation of the data quality
    plane (DQ) is important in order to fix hot and dark pixels on the
    NIFS detector in subsequent steps in the data reduction process.
    Various header keywords (used later) are also added in NFPREPARE.
    NFPREPARE will also add an MDF file (extension MDF) describing the
    NIFS image slicer pattern and how the IFU maps to the sky field.

    """

    # Update frames with mdf offset value and generate variance and data quality extensions.
    for frame in inlist:
        if os.path.exists("n"+frame+".fits"):
            if over:
                os.remove("n"+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping prepare_list")
                continue
        iraf.nfprepare(frame, rawpath="", shiftimage=shiftima, fl_vardq="yes", bpm=finalBadPixelMask, fl_int='yes', fl_corr='no', fl_nonl='no', logfile=log)
    inlist = checkLists(inlist, '.', 'n', '.fits')
    return inlist

#--------------------------------------------------------------------------------------------------------------------------------#

def combineImages(inlist, out, log, over):
    """Gemcombine multiple frames. Output: -->gn."""

    if os.path.exists(out+".fits"):
        if over:
            iraf.delete(out+".fits")
        else:
            logging.info("Output file exists and -over not set - skipping combine_ima")
            return

    iraf.gemcombine(listit(inlist,"n"),output=out,fl_dqpr='yes', fl_vardq='yes',masktype="none", combine="median", logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def copyImage(input, output, over):
    """Copy a frame (used to add the correct prefix when skipping steps)."""

    if os.path.exists(output):
        if over:
            iraf.delete(output)
        else:
            logging.info("Output file exists and -over not set - skipping copy_ima")
            return

    iraf.copy('n'+input[0]+'.fits', output)

#--------------------------------------------------------------------------------------------------------------------------------#

def skySubtractObj(objlist, skyFrameList, log, over):
    """"Sky subtraction for science using iraf.gemarith. Output: ->sgn"""

    for i in range(len(objlist)):
        frame = str(objlist[i])
        sky = str(skyFrameList[i])
        if os.path.exists("sn"+frame+".fits"):
           if over:
               os.remove("sn"+frame+".fits")
           else:
               logging.info("Output file exists and -over not set - skipping skysub_list")
               continue
        iraf.gemarith ("n"+frame, "-", "n"+sky, "sn"+frame, fl_vardq="yes", logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def skySubtractTel(tellist, sky, log, over):
    """Sky subtraction for telluric using iraf.gemarith. Output: ->sgn"""

    for frame in tellist:
        if os.path.exists("sn"+frame+".fits"):
            if over:
                os.remove("sn"+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping skySubtractTel.")
                continue
        iraf.gemarith ("n"+frame, "-", sky, "sn"+frame, fl_vardq="yes", logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def applyFlat(objlist, flat, log, over, kind, dark=""):
    """Flat field and cut the data with iraf.nsreduce. Output: ->rsgn.

    NSREDUCE is used for basic reduction of raw data - it provides a
    single, unified interface to several tasks and also allows for
    the subtraction of dark frames and dividing by the flat. For
    NIFS reduction, NSREDUCE is used to call the NSCUT and NSAPPWAVE
    routines.

    """

    # By default don't subtract darks from tellurics.
    fl_dark = "no"
    if dark != "":
        fl_dark = "yes"

    for frame in objlist:
        frame = str(frame).strip()
        if os.path.exists("rsn"+frame+".fits"):
            if over:
                os.remove("rsn"+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping apply_flat_list")
                continue
        iraf.nsreduce("sn"+frame, fl_cut="yes", fl_nsappw="yes", fl_dark="no", fl_sky="no", fl_flat="yes", flatimage=flat, fl_vardq="yes",logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def fixBad(objlist, log, over):
    """Interpolate over bad pixels flagged in the DQ plane with iraf.nffixbad. Output: -->brsn.

    NFFIXBAD - Fix Hot/Cold pixels on the NIFS detector.

    This routine uses the information in the Data Quality
    extensions to fix hot and cold pixels in the NIFS science
    fields. NFFIXBAD is a wrapper script which calls the task
    FIXPIX, using the DQ plane to define the pixels to be corrected.

    """

    for frame in objlist:
        frame = str(frame).strip()
        if os.path.exists("brsn"+frame+".fits"):
            if over:
                os.remove("brsn"+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping fixbad_list")
                continue
        iraf.nffixbad("rsn"+frame,logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def fitCoords(objlist, arc, ronchi, log, over, kind):
    """Derive the 2D to 3D spatial/spectral transformation with iraf.nsfitcoords.
    Output: -->fbrsn

    NFFITCOORDS - Compute 2D dispersion and distortion maps.

    This routine uses as inputs the output from the NSWAVELENGTH
    and NFSDIST routines. NFFITCOORDS takes the spatial and
    spectral rectification information from NSWAVELENGTH and
    NFSDIST and converts this into a calculation of where the data
    information should map to in a final IFU dataset.

    """

    for frame in objlist:
        frame = str(frame).strip()
        if os.path.exists("fbrsn"+frame+".fits"):
            if over:
                os.remove("fbrsn"+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping fitcoord_list")
                continue
        iraf.nsfitcoords("brsn"+frame, lamptransf=arc, sdisttransf=ronchi, database="database", lxorder=3, lyorder=2, sxorder=3, syorder=3, logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def transform(objlist, log, over):
    """Apply the transformation determined in iraf.nffitcoords with
    iraf.nstransform. Output: -->tfbrsgn

    NSTRANSFORM - Spatially rectify and wavelength calibrate data.

    NFTRANSFORM applies the wavelength solution found by
    NSWAVELENGTH and the spatial correction found by NFSDIST,
    aligning all the IFU extensions consistently onto a common
    coordinate system. The output of this routine is still in 2D
    format, with each of the IFU slices represented by its own data
    extension.

    """

    for frame in objlist:
        frame = str(frame).strip()
        if os.path.exists("tfbrsn"+frame+".fits"):
            if over:
                iraf.delete("tfbrsn"+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping transform_list")
                continue
        iraf.nstransform("fbrsn"+frame, logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def makeCube(pre, scienceFrameList, log, over):
    """ Reformat the data into a 3-D datacube using iraf.nifcube. Output: -->ctfbrsgn.

    NIFCUBE - Construct 3D NIFS datacubes.

    NIFCUBE takes input from data output by either NFFITCOORDS or
    NFTRANSFORM and converts the 2D data images into data cubes
    that have coordinates of x, y, lambda.

    """
    for frame in scienceFrameList:
        if os.path.exists("c"+pre+frame+".fits"):
            if over:
                iraf.delete("c"+pre+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping make_cube_list")
                continue
        iraf.nifcube (pre+frame, outcubes = 'c'+pre+frame, logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def extractOneD(inputList, kind, log, over, extractionXC=15.0, extractionYC=33.0, extractionRadius=2.5):
    """Extracts 1-D spectra with iraf.nfextract and combines them with iraf.gemcombine.
    iraf.nfextract is currently only done interactively. Output: -->xtfbrsn and gxtfbrsn

    NFEXTRACT - Extract NIFS spectra.

    This could be used to extract a 1D spectra from IFU data and is
    particularly useful for extracting the bright spectra of
    telluric calibrator stars. Note that this routine only works
    on data that has been run through NFTRANSFORM.

    """

    for frame in inputList:
        frame = str(frame).strip()
        if os.path.exists("xtfbrsn"+frame+".fits"):
            if over:
                iraf.delete("xtfbrsn"+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping nfextract in extract1D")
                continue

        iraf.nfextract("tfbrsn"+frame, outpref="x", xc=extractionXC, yc=extractionYC, diameter=extractionRadius, fl_int='no', logfile=log)

    # Combine all the 1D spectra to one final output file with the name of the first input file.
    combined = str(inputList[0]).strip()
    if len(inputList) > 1:
        if os.path.exists("gxtfbrsn"+combined+".fits"):
            if over:
                iraf.delete("gxtfbrsn"+combined+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping gemcombine in extract1D")
                return
        iraf.gemcombine(listit(inputList,"xtfbrsn"),output="gxtfbrsn"+combined, statsec="[*]", combine="median",masktype="none",fl_vardq="yes", logfile=log)
    else:
        if over:
            iraf.delete("gxtfbrsn"+combined+".fits")
        iraf.copy(input="xtfbrsn"+combined+".fits", output="gxtfbrsn"+combined+".fits")

    if kind == 'Telluric':
        # Put the name of the final combined file into a text file called
        # telluricfile to be used by the pipeline later.
        open("telluricfile", "w").write("gxtfbrsn"+combined)
    elif kind == 'Science':
        open("combinedOneD", "w").write("gxtfbrsn"+combined)

#--------------------------------------------------------------------------------------------------------------------------------#

def copyExtracted(scienceFrameList, over):
    """
    Copy all extracted 1D spectra to objectname/ExtractedOneD/date_obsname/,
    and combined 1D spectra to objectname/ExtractedOneD
    """
    # TODO(nat): make this clearer.
    obsDir = os.getcwd()
    temp1 = os.path.split(obsDir)
    temp2 = os.path.split(temp1[0])
    temp3 = os.path.split(temp2[0])
    temp4 = os.path.split(temp3[0])
    objname = temp4[1]
    date = temp3[1]
    obsid = temp1[1]
    obsPath = temp3[0]
    os.chdir(obsDir)
    # Create a directory called ExtractedOneD and copy all the data cubes to this directory.
    if not os.path.exists(obsPath+'/ExtractedOneD/'):
        os.mkdir(obsPath+'/ExtractedOneD/')
        logging.info('I am creating a directory called ExtractedOneD')
    ExtractedOneD = obsPath+'/ExtractedOneD'
    # Make the appropriate directory structure.
    if not os.path.exists(ExtractedOneD+'/'+date+'_'+obsid):
        os.mkdir(ExtractedOneD+'/'+date+'_'+obsid)
        logging.info('I am creating a directory with date and abs ID inside ExtractedOneD ')
    # Get the filenames of the uncombined spectra.
    uncombinedSpectra = glob.glob('xtfbrsnN*.fits')
    # Copy the uncombined spectra to the appropriate directory.
    for spectra in uncombinedSpectra:
        if os.path.exists(ExtractedOneD+'/'+date+'_'+obsid+'/'+spectra):
            if over:
                os.remove(ExtractedOneD+'/'+date+'_'+obsid+'/'+spectra)
                shutil.copy(spectra, ExtractedOneD+'/'+date+'_'+obsid)
            else:
                logging.info("Output file exists and -over not set - skipping copy one D spectra")
        else:
            shutil.copy(spectra, ExtractedOneD+'/'+date+'_'+obsid)
    # Get the file name of the combined spectra
    combinedSpectrum = glob.glob('gxtfbrsnN*.fits')
    combinedSpectrum = combinedSpectrum[0]
    # Copy the combined spectrum to the appropriate directory.
    if os.path.exists(ExtractedOneD+'/'+combinedSpectrum):
        if over:
            os.remove(ExtractedOneD+'/'+combinedSpectrum)
            shutil.copy(combinedSpectrum, ExtractedOneD)
        else:
            logging.info("Output file exists and -over not set - skipping copy combined one D spectra")
    else:
        shutil.copy(spectra, ExtractedOneD+'/combined'+date+'_'+obsid+'.fits')

#--------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    a = raw_input('Enter <Science> for science reduction or <Telluric> for telluric reduction: ')
    start(a)
