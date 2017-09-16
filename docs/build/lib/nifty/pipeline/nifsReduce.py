#!/usr/bin/env python
################################################################################
#                Import some useful Python utilities/modules                   #
################################################################################
import sys, glob, shutil, getopt, os, time, logging, glob, sgmllib, urllib, re, traceback, pkg_resources
import pexpect as p
from pyraf import iraf, iraffunctions
import astropy.io.fits
from astropy.io.fits import getdata, getheader
import numpy as np
from scipy.interpolate import interp1d
from scipy import arange, array, exp
import pylab as pl
import matplotlib.pyplot as plt
# Import config parsing.
from configobj.configobj import ConfigObj
# Import custom Nifty functions.
from nifsUtils import datefmt, listit, writeList, checkLists, makeSkyList, MEFarith, convertRAdec
# Import Nifty python data cube merging script.
import nifsMerge

# Define constants
# Paths to Nifty data.
RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

def start(kind):
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
        kind(string): either 'Telluric' or 'Science'.

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

    # Load reduction parameters from runtimeData/config.cfg.
    with open('./config.cfg') as config_file:
        options = ConfigObj(config_file, unrepr=True)
        if kind == 'Telluric':
            # Load telluricDirectoryList as observationDirectoryList
            observationDirectoryList = options['telluricDirectoryList']
            start = options['telStart']
            stop = options['telStop']
        elif kind == 'Science':
            # Load scienceDirectoryList as observationDirectoryList
            observationDirectoryList = options['scienceDirectoryList']
            start = options['sciStart']
            stop = options['sciStop']
        calDirList = options['calibrationDirectoryList']
        telinter = options['telinter']
        efficiencySpectrumCorrection = options['efficiencySpectrumCorrection']
        continuuminter = options['continuuminter']
        hlineinter = options['hlineinter']
        hline_method = options['hline_method']
        spectemp = options['spectemp']
        mag = options['mag']
        over = options['over']
        telluric_correction_method = options['telluric_correction_method']
        use_pq_offsets = options['use_pq_offsets']
        merge = options['merge']
        im3dtran = options['im3dtran']
        debug = options['debug']

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

        # Find the Calibrations_grating directory that corresponds to the observation date and grating.
        # The observation date and grating are found from directory paths.
        for calDir in calDirList:
            tempCal = calDir.split(os.sep)
            # Need two cases because science directory paths are shorter than telluric
            # directory paths.
            # For science observation directories:
            # IF dates in path names match AND gratings in path names match, break.
            if tempObs[-3]==tempCal[-2] and tempObs[-2] == tempCal[-1][-1]:
                calDir = calDir+'/'
                break
            # For telluric observation directories.
            # IF dates in path names match AND gratings in path names match, break.
            elif tempObs[-4]==tempCal[-2] and tempObs[-3] == tempCal[-1][-1]:
                calDir = calDir+'/'
                break

        obsid = tempObs[-1]

        # Change the iraf directory to the current directory.
        pwd = os.getcwd()
        iraffunctions.chdir(pwd)

        # Copy relevant calibrations over to the science directory.
        # Open and store the name of the MDF shift reference file from shiftfile into shift.
        shift = calDir+str(open(calDir+"shiftfile", "r").readlines()[0]).strip()
        # Open and store the name of the flat frame from flatfile in flat.
        flat = calDir+str(open(calDir+"flatfile", "r").readlines()[0]).strip()
        # Open and store the bad pixel mask name from sflat_bpmfile in sflat_bpm.
        sflat_bpm = calDir+str(open(calDir+"sflat_bpmfile", "r").readlines()[0]).strip()
        # Open and store the name of the reduced spatial correction ronchi flat frame name from ronchifile in ronchi.
        ronchi = open(calDir+"ronchifile", "r").readlines()[0].strip()
        # Copy the spatial calibration ronchi flat frame from Calibrations_grating to the observation directory.
        iraf.copy(calDir+ronchi+".fits", output="./")
        # Open and store the name of the reduced wavelength calibration arc frame from arclist in arc.
        arc = "wrgn"+str(open(calDir+"arclist", "r").readlines()[0]).strip()
        # Copy the wavelength calibration arc frame from Calibrations_grating to the observation directory.
        iraf.copy(calDir+arc+".fits", output="./")
        # Make sure the database files are in place. Current understanding is that
        # these should be local to the reduction directory, so need to be copied from
        # the calDir.
        if os.path.isdir("./database"):
            if over:
                shutil.rmtree("./database")
                os.mkdir("./database")
        elif not os.path.isdir("./database"):
            os.mkdir('./database/')
        iraf.copy(input=calDir+"database/*", output="./database/")

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
                if debug:
                    a = raw_input("About to enter step 1: locate the spectrum.")
                if kind=='Telluric':
                    tellist = prepare(tellist, shift, sflat_bpm, log, over)
                elif kind=='Science':
                    scienceFrameList = prepare(scienceFrameList, shift, sflat_bpm, log, over)
                skyFrameList = prepare(skyFrameList, shift, sflat_bpm, log, over)
                logging.info("\n##############################################################################")
                logging.info("")
                logging.info("  STEP 1: Locate the Spectrum (and prepare raw data) ->n - COMPLETED ")
                logging.info("")
                logging.info("##############################################################################\n")

            ###########################################################################
            ##  STEP 2: Sky Subtraction ->sn                                         ##
            ###########################################################################

            elif valindex == 2:
                if debug:
                    a = raw_input("About to enter step 2: sky subtraction.")
                # Combine telluric sky frames.
                if kind=='Telluric':
                    if len(skyFrameList)>1:
                        combineImages(skyFrameList, "gn"+sky, log, over)
                    else:
                        copyImage(skyFrameList, 'gn'+sky+'.fits', over)
                if kind=='Telluric':
                    skySubtractTel(tellist, "gn"+sky, log, over)
                elif kind=='Science':
                    # Temporary code to let us skip the sky subtraction.
                    if False:
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
                if debug:
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
                if debug:
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
                if debug:
                    a = raw_input("About to enter step 5.")
                # For telluric data:
                # Make a 1D telluric correction spectrum from reduced telluric data.
                if kind=='Telluric':
                    makeTelluric(tellist, log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 5: Extract 1D Spectra and Make Combined Telluric")
                    logging.info("          1D spectrum ->gxtfbrsn - COMPLETED")
                    logging.info("")
                    logging.info("##############################################################################\n")

                # For science data, either:
                # Apply the telluric correction and absolute flux calibration by dividing by efficiency spectrum with Python.
                elif kind=='Science' and telluric_correction_method == "python":
                    makeCube('tfbrsn', scienceFrameList, observationDirectory, log, over)
                    applyTelluricPython(over)

                # Apply the telluric correction and absolute flux calibration with iraf.nftelluric().
                elif kind=='Science' and telluric_correction_method == "iraf":
                    applyTelluricIraf(scienceFrameList, obsid, telinter, log, over)
                    makeCube('atfbrsn', scienceFrameList, observationDirectory, log, over)

                # DON'T apply the telluric correction and absolute flux calibration; just make a cube.
                elif kind=='Science' and telluric_correction_method == "none":
                    # Make cube without telluric correction.
                    makeCube('tfbrsn', scienceFrameList, observationDirectory, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 5: Possibly apply telluric correction and relative flux calibation and make")
                    logging.info("          a data cube ->catgbrsn, ->cptfbrsn or ->ctfbrsn - COMPLETED")
                    logging.info("")
                    logging.info("##############################################################################\n")

            ###########################################################################
            ##  STEP 6 (Tellurics): Create an efficiency spectrum ->cgxtfbrsn        ##
            ##  STEP 6 (Science): Create a final combined 3D data cube               ##
            ##    ->[date]_[obsid]_merged.fits (and ->TOTAL_merged[grating].fits, if ##
            ##    multiple observations to be merged).                               ##
            ###########################################################################

            elif valindex == 6:
                if debug:
                    a = raw_input("About to enter step 6.")
                if kind == 'Telluric' and efficiencySpectrumCorrection:
                    createEfficiencySpectrum(
                        observationDirectory, path, continuuminter, hlineinter,
                        hline_method, spectemp, mag, log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 6: Create Efficiency Spectrum ->fcatfbrsn or ->fctfbrsn - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")
                # After the last science reduction, possibly merge final cubes to a single cube.
                if kind == 'Science' and merge and os.getcwd() == observationDirectoryList[-1]:
                    nifsMerge.start(observationDirectoryList, use_pq_offsets, im3dtran, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 6: Create Combined Final 3D Cube - path/scienceObjectName/Merged/ - COMPLETED ")
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
    return

##################################################################################################################
#                                                     FUNCTIONS                                                 #
##################################################################################################################

def prepare(inlist, shiftima, sflat_bpm, log, over):
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
        iraf.nfprepare(frame, rawpath="", shiftimage=shiftima, fl_vardq="yes", bpm=sflat_bpm, fl_int='yes', fl_corr='no', fl_nonl='no', logfile=log)
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
        iraf.nsfitcoords("brsn"+frame, lamptransf=arc, sdisttransf=ronchi, lxorder=3, lyorder=2, sxorder=3, syorder=3, logfile=log)

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

def makeCube(pre, scienceFrameList, observationDirectory, log, over):
    """ Reformat the data into a 3-D datacube using iraf.nifcube. Output: If
    telluric correction to be applied, -->catfbrsgn. Else, -->ctfbrsgn.

    NIFCUBE - Construct 3D NIFS datacubes.

    NIFCUBE takes input from data output by either NFFITCOORDS or
    NFTRANSFORM and converts the 2D data images into data cubes
    that have coordinates of x, y, lambda.

    """

    os.chdir(observationDirectory)
    for frame in scienceFrameList:
        if os.path.exists("c"+pre+frame+".fits"):
            if over:
                iraf.delete("c"+pre+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping make_cube_list")
                continue
        iraf.nifcube (pre+frame, outcubes = 'c'+pre+frame, logfile=log)

#--------------------------------------------------------------------------------------------------------------------------------#

def makeTelluric(tellist, log, over):
    """Extracts 1-D spectra with iraf.nfextract and combines them with iraf.gemcombine.
    iraf.nfextract is currently only done interactively. Output: -->xtfbrsn and gxtfbrsn

    NFEXTRACT - Extract NIFS spectra.

    This could be used to extract a 1D spectra from IFU data and is
    particularly useful for extracting the bright spectra of
    telluric calibrator stars. Note that this routine only works
    on data that has been run through NFTRANSFORM.

    """

    for frame in tellist:
        frame = str(frame).strip()
        if os.path.exists("xtfbrsn"+frame+".fits"):
            if over:
                iraf.delete("xtfbrsn"+frame+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping extraction in make_telluric")
                continue

        iraf.nfextract("tfbrsn"+frame, outpref="x", xc=15.0, yc=33.0, diameter=2.5, fl_int='no', logfile=log)


    # Combine all the 1D spectra to one final output file with the name of the first input file.
    telluric = str(tellist[0]).strip()
    if len(tellist) > 1:
        if os.path.exists("gxtfbrsn"+telluric+".fits"):
            if over:
                iraf.delete("gxtfbrsn"+telluric+".fits")
            else:
                logging.info("Output file exists and -over not set - skipping gemcombine in make_telluric")
                return
        iraf.gemcombine(listit(tellist,"xtfbrsn"),output="gxtfbrsn"+telluric, statsec="[*]", combine="median",masktype="none",fl_vardq="yes", logfile=log)
    else:
        if over:
            iraf.delete("gxtfbrsn"+telluric+".fits")
        iraf.copy(input="xtfbrsn"+telluric+".fits", output="gxtfbrsn"+telluric+".fits")

    # Put the name of the final telluric correction file into a text file called
    # telluricfile to be used by the pipeline later.
    open("telluricfile", "w").write("gxtfbrsn"+telluric)

#--------------------------------------------------------------------------------------------------------------------------------#

def applyTelluricPython(over):
    """Python method to divide each spaxel by an efficiency spectrum.
    Assumes function is called from a science observation directory.
    Args:
        over(bool): overwite old files.
    """

    """TODO(nat): implement this old code from makeCube. I think it makes more
    sense to be placed somewhere in here.

    hdulist = astropy.io.fits.open('c'+pre+frame+'.fits', mode = 'update')
    #            hdulist.info()
    exptime = hdulist[0].header['EXPTIME']
    cube = hdulist[1].data
    gain = 2.8
    cube_calib = cube / (exptime * gain)
    hdulist[1].data = cube_calib
    hdulist.flush()
    """

    observationDirectory = os.getcwd()
    # Get the efficiency spectrum we will use to do a telluric correction and flux calibration at the same time.
    os.chdir('../Tellurics')
    # Find a list of all the telluric observation directories.
    telDirList_temp = glob.glob('*')
    tempDir = os.path.split(observationDirectory)
    telDirList = []
    for telDir in telDirList_temp:
        telDirList.append(tempDir[0]+'/Tellurics/'+telDir)
    for telDir in telDirList:
        # Change to the telluric directory.
        os.chdir(telDir)
        # Make sure an scienceMatchedTellsList is present.
        try:
            scienceMatchedTellsList = open('scienceMatchedTellsList', 'r').readlines()
            scienceMatchedTellsList = [item.strip() for item in scienceMatchedTellsList]
        except:
            os.chdir('..')
            continue

        # Open the correction efficiency spectrum.
        telluric = str(open('finalcorrectionspectrum', 'r').readlines()[0]).strip()
        logging.info("\nFound a finalcorrectionspectrum in\n"), telDir
        # Open the final correction spectrum file as "telluric". Create a numpy array the same length
        # as the telluric spectrum with each element a wavelength matching that of the telluric.

        # Open the final correction spectrum so that we use its data.
        telluric = astropy.io.fits.open(telluric+'.fits')
        # Find the starting wavelength and the wavelength increment from the science header.
        wstart = telluric[1].header['CRVAL1']
        wdelt = telluric[1].header['CD1_1']
        # Create a numpy array of zeros. We will use this to hold the efficiency spectrum.
        effwave = np.zeros(2040)
        # Create a wavelength array using the starting wavelength and the wavelength increment.
        for i in range(2040):
            effwave[i] = wstart+(wdelt*i)

        # Open the efficiency spectrum as a numpy array.
        effspec = telluric[1].data
        # Store the airmass of the correction spectrum in telairmass.
        telairmass = telluric[0].header['AIRMASS']

        tempDir = observationDirectory.split(os.sep)
        if tempDir[-1] in scienceMatchedTellsList:
            os.chdir(observationDirectory)
            logging.info("\nWorking to apply tellurics in:\n"+ str(observationDirectory))
            scilist = glob.glob('c*.fits')
            for frame in scilist:
                # TODO: this will break if for some reason we don't do something like the sky subtraction... Perhaps we should
                # make sure the prefix is correct before the function starts?
                if frame.replace('ctfbrsn','').replace('.fits', '') in scienceMatchedTellsList:
                    if os.path.exists(frame[0]+'p'+frame[1:]):
                        if not over:
                            logging.info('Output already exists and -over- not set - skipping telluric correction and flux calibration')
                            continue
                        if over:
                            os.remove(frame[0]+'p'+frame[1:])
                            pass
                    logging.info("\nApplying python telluric correction to: \n"+ str(frame))
                    np.set_printoptions(threshold=np.nan)

                    # Read in cube data and create a 1D array "cubewave" of the wavelengths found in the cube.
                    # Open a data cube with astropy.io.fits. Read the data header to find the starting wavelength and wavelength increment.
                    # From readCube docstring:
                    #       Create a 1D array with length equal to the spectral dimension of the cube.
                    #    For each element in array, element[i] = starting wavelength + (i * wavelength increment).
                    #    Returns:
                    #        cube (object reference):   Reference to the opened data cube.
                    #        cubewave (1D numpy array): array representing pixel-wavelength mapping of data cube.
                    cube, cubewave = readCube(frame)

                    # Interpolate a function using the telluric spectrum.
                    # From scipy.interp1d help:
                    #   interp1d(x,y)
                    efficiencySpectrumFunction = interp1d(effwave, effspec, bounds_error = None, fill_value=0.)
                    # Extend the function to allow extrapolation.
                    extendedEfficiencySpectrumFunction = extrap1d(efficiencySpectrumFunction)
                    # For each element of the cube wavelength array, a 1D numpy array holding wavelengths from a single spaxel of the cube, evaluate extrapolatedfunction(wavelength) and
                    # store the result in the element.
                    # Iterate over each element, ie, wavelength, of the cubes wavelength array.
                    # evaluate f(wavelength) and store the result in that element.
                    effspec = extendedEfficiencySpectrumFunction(cubewave)
                    # Optional: plot things out.
                    #plt.ion()
                    #plt.figure(1)
                    #plt.plot(effspec)

                    exptime = cube[0].header['EXPTIME']

                    # See if we should attempt an airmass correction.
                    try:
                        sciairmass = cube[0].header['AIRMASS']
                        airmcor = True
                    except:
                        logging.info("No airmass found in header. No airmass correction being performed on "+ str(frame)+ " .\n")
                        airmcor= False

                    if airmcor:
                        airmassCorrection = sciairmass/telairmass
                        logging.info("\nDoing an airmass correction; correction factor is "+ str(airmassCorrection)+".")
                        # If effspec[i] is between 0 and 1, apply an airmass correction by multiplying ln(effspec[i]) by the correction factor.
                        for i in range(len(effspec)):
                            if effspec[i]>0. and effspec[i]<1.:
                                effspec[i] = np.log(effspec[i])
                                effspec[i] *= airmassCorrection
                                effspec[i] = np.exp(effspec[i])

                    plt.plot(effspec,"r--")
                    # Divide each spectrum in the cubedata array by the efficiency spectrum*exptime.
                    for i in range(cube[1].header['NAXIS2']):         # NAXIS2 is the y axis of the final cube.
                        for j in range(cube[1].header['NAXIS1']):     # NAXIS1 is the x axis of the final cube.
                            cube[1].data[:,i,j] /= (effspec*exptime)  # For each y and x, divide entire spectrum by effspec*exptime.

                    # Write the corrected cube to a new file with a "cp" prefix, "p" for "python corrected".
                    cube.writeto('cp'+frame[1:], output_verify='ignore')

    # Make sure we exit in the right directory.
    os.chdir(observationDirectory)

#--------------------------------------------------------------------------------------------------------------------------------#

def applyTelluricIraf(scienceList, obsid, telinter, log, over):
    """Corrects the data for telluric absorption features with iraf.nftelluric.
    iraf.nftelluric is currently only run interactively. Output: -->atfbrsgn

    NFTELLURIC

    NFTELLURIC uses input science and a 1D spectrum of a telluric
    calibrator to correct atmospheric absorption features.
    """

    observationDirectory = os.getcwd()
    os.chdir('../Tellurics')
    telDirList = glob.glob('*')

    if telinter:
        telinter = 'yes'
    else:
        telinter = 'no'

    # Used for brighter objects.
    for telDir in telDirList:
        if 'obs' in telDir:
            os.chdir(telDir)
            if os.path.exists('scienceMatchedTellsList'):
                scienceMatchedTellsList = open("scienceMatchedTellsList", "r").readlines()
                scienceList = [frame.strip() for frame in scienceMatchedTellsList]
            else:
                os.chdir('..')
                continue
            try:
                telluric = str(open('finalcorrectionspectrum', 'r').readlines()[0]).strip()
            except:
                logging.info("No telluric spectrum found in "), telDir
                os.chdir('..')
                continue
            shutil.copy(telluric+'.fits', observationDirectory)

            '''
            continuum = str(open('continuumfile', 'r').readlines()[0]).strip()
            bblist = open('blackbodyfile', 'r').readlines()
            bblist = [frame.strip() for frame in bblist]
            '''

            os.chdir(observationDirectory)
            iraffunctions.chdir(observationDirectory)
            if obsid in scienceList:
                index = scienceList.index(obsid)
                i=index+1

                while i<len(scienceList) and 'obs' not in scienceList[i]:
                    if os.path.exists("atfbrsn"+scienceList[i]+".fits"):
                        if over:
                            iraf.delete("atfbrsgn"+scienceList[i]+".fits")
                            if telinter == "yes":
                                iraf.nftelluric('tfbrsn'+scienceList[i], outprefix='a', calspec=telluric, fl_inter = telinter, logfile=log)
                            else:
                                iraf.nftelluric('tfbrsn'+scienceList[i], outprefix='a', xc=15.0, yc=33.0, calspec=telluric, fl_inter = telinter, logfile=log)
                        else:
                            logging.info("Output file exists and -over not set - skipping nftelluric in applyTelluric")
                    elif not os.path.exists('atfbrsn'+scienceList[i]+'.fits'):
                        logging.info('\ntfbrsn'+scienceList[i])
                        logging.info(telluric)
                        logging.info(telinter)
                        if telinter == "yes":
                            iraf.nftelluric('tfbrsn'+scienceList[i], outprefix='a', calspec=telluric, fl_inter = telinter, logfile=log)
                        else:
                            iraf.nftelluric('tfbrsn'+scienceList[i], outprefix='a', xc=15.0, yc=33.0, calspec=telluric, fl_inter = telinter, logfile=log)

                    '''
                    # remove continuum fit from reduced science image
                    if over:
                        if os.path.exists("cont"+scienceList[i]+".fits"):
                            iraf.delete("cont"+scienceList[i]+".fits")
                        MEFarithpy('atfbrsgn'+scienceList[i], '../Tellurics/'+telDir+'/'+continuum, 'divide', 'cont'+scienceList[i]+'.fits')
                    elif not os.path.exists('cont'+scienceList[i]+'.fits'):
                        MEFarithpy('atfbrsgn'+scienceList[i], '../Tellurics/'+telDir+'/'+continuum, 'divide', 'cont'+scienceList[i]+'.fits')
                    else:
                        logging.info("Output file exists and -over not set - skipping continuum division in applyTelluric")

                    # multiply science by blackbody
                    for bb in bblist:
                        objheader = astropy.io.fits.open(observationDirectory+'/'+scienceList[i]+'.fits')
                        exptime = objheader[0].header['EXPTIME']
                        if str(int(exptime)) in bb:
                            if over:
                                if os.path.exists('bbatfbrsgn'+scienceList[i]+'.fits'):
                                    os.remove('bbatfbrsgn'+scienceList[i]+'.fits')
                                MEFarithpy('cont'+scienceList[i], '../Tellurics/'+telDir+'/'+bb, 'multiply', 'bbatfbrsgn'+scienceList[i]+'.fits')
                            elif not os.path.exists('bbatfbrsgn'+scienceList[i]+'.fits'):
                                MEFarithpy('cont'+scienceList[i], '../Tellurics/'+telDir+'/'+bb, 'multiply', 'bbatfbrsgn'+scienceList[i]+'.fits')
                            else:
                                logging.info("Output file exists and -over- not set - skipping blackbody calibration in applyTelluric")
                    '''
                    i+=1
        os.chdir('../Tellurics')

#--------------------------------------------------------------------------------------------------------------------------------#

def createEfficiencySpectrum(
    telluricDirectory, path, continuuminter, hlineinter, hline_method, spectemp,
    mag, log, over):
    """FLUX CALIBRATION

    Consists of this start function and six required functions at the end of
    this file.


    COMMAND LINE OPTIONS
    If you wish to skip this script enter -g in the command line
    Specify a spectral type or temperature with -e
    Specify a magnitude with -f
    Specify an H line fitting method with -l (default is vega)
    Specify interactive H line fitting with -i (default inter=no)
    Specify interactive continuum fitting with -y (def inter=no)

    INPUT:
    - reduced and combined standard star spectra

    OUTPUT:
    - reduced (H line and continuum fit) standard star spectra
    - flux calibrated blackbody spectrum

    Args:
        telDirList: list of telluric directories.
        continuuminter (boolean): Interactive continuum fitting. Specified with -y
                                  at command line. Default False.
        hlineinter (boolean):     Interactive H line fitting. Specified with -i at
                                  command line. Default False.
        hline_method (string):    Method for removing H lines from the telluric spectra.
                                  Specified with -l or --hline at command line. Default is
                                  vega and choices are vega, linefitAuto, linefitManual,
                                  vega_tweak, linefit_tweak, and none.
        spectemp:                 Spectral type or temperature. Specified at command line with -e or --stdspectemp.
        mag:                      The IR magnitude of the standard star.
                                  Specified at command line with -f or --stdmag.
        over:                     overwrite old files.
    """

    iraf.gemini(_doprint=0, motd="no")
    iraf.gnirs(_doprint=0)
    iraf.imutil(_doprint=0)
    iraf.onedspec(_doprint=0)
    iraf.nsheaders('nifs',Stdout='/dev/null')

    iraffunctions.chdir(telluricDirectory)

    logging.info(' I am starting to create telluric correction spectrum and blackbody spectrum')
    logging.info('I am starting to create telluric correction spectrum and blackbody spectrum ')

    # open and define standard star spectrum and its relevant header keywords
    try:
        combined_extracted_1d_spectra = str(open('telluricfile', 'r').readlines()[0]).strip()
    except:
        logging.info("No telluricfile found in "), telluricDirectory
        return
    if not os.path.exists('scienceMatchedTellsList'):
        logging.info("No scienceMatchedTellsList found in "), telluricDirectory
        return


    telheader = astropy.io.fits.open(combined_extracted_1d_spectra+'.fits')
    band = telheader[0].header['GRATING'][0]
    RA = telheader[0].header['RA']
    Dec = telheader[0].header['DEC']
    airmass_std = telheader[0].header['AIRMASS']
    temp1 = os.path.split(telluricDirectory)
    temp2 = os.path.split(temp1[0])
    # make directory PRODUCTS above the Telluric observation directory
    # telluric_hlines.txt is stored there
    if not os.path.exists(temp1[0]+'/PRODUCTS'):
        os.mkdir(temp1[0]+'/PRODUCTS')

    # defines 'name' that is passed to mag2mass
    if '-' in str(Dec):
        name = str(RA)+'d'+str(Dec)+'d'
    else:
        name = str(RA)+'d+'+str(Dec)+'d'

    # find standard star spectral type, temperature, and magnitude
    mag2mass(name, path, spectemp, mag, band)

    logging.info("\n##############################################################################")
    logging.info("")
    logging.info("  STEP 6a - Find standard star information - COMPLETED ")
    logging.info("")
    logging.info("##############################################################################\n")

    # File for recording shift/scale from calls to "telluric"
    telluric_shift_scale_record = open('telluric_hlines.txt', 'w')

    # Remove H lines from standard star
    no_hline = False
    if os.path.exists("final_tel_no_hlines_no_norm"+band+'.fits'):
        if over:
            iraf.delete("final_tel_no_hlines_no_norm"+band+'.fits')
        else:
            no_hline = True
            logging.info("Output file exists and -over- not set - skipping H line removal")

    if hline_method == "vega" and not no_hline:
        vega(combined_extracted_1d_spectra, band, path, hlineinter, airmass_std, telluric_shift_scale_record, log, over)

    if hline_method == "linefitAuto" and not no_hline:
        linefitAuto(combined_extracted_1d_spectra, band)

    if hline_method == "linefitManual" and not no_hline:
        linefitManual(combined_extracted_1d_spectra+'[sci,1]', band)

    if hline_method == "vega_tweak" and not no_hline:
        #run vega removal automatically first, then give user chance to interact with spectrum as well
        vega(combined_extracted_1d_spectra,band, path, hlineinter, airmass_std, telluric_shift_scale_record, log, over)
        linefitManual("final_tel_no_hlines_no_norm"+band, band)

    if hline_method == "linefit_tweak" and not no_hline:
        #run Lorentz removal automatically first, then give user chance to interact with spectrum as well
        linefitAuto(combined_extracted_1d_spectra,band)
        linefitManual("final_tel_no_hlines_no_norm"+band, band)

    if hline_method == "none":
        #need to copy files so have right names for later use
        iraf.imcopy(input=combined_extracted_1d_spectra+'[sci,'+str(1)+']', output="final_tel_no_hlines_no_norm"+band, verbose='no')

    logging.info("\n##############################################################################")
    logging.info("")
    logging.info("  STEP 6b - Apply or do not apply hline correction to standard star - COMPLETED ")
    logging.info("")
    logging.info("##############################################################################\n")

    # make a list of exposure times from the science images that use this standard star spectrum for the telluric correction
    # used to make flux calibrated blackbody spectra
    scienceMatchedTellsList = open('scienceMatchedTellsList', 'r').readlines()
    scienceMatchedTellsList = [frame.strip() for frame in scienceMatchedTellsList]
    exptimelist = []
    for item in scienceMatchedTellsList:
        if 'obs' in item:
            os.chdir(telluricDirectory)
            os.chdir('../../'+item)
        else:
            objheader = astropy.io.fits.open(item+'.fits')
            exptime = objheader[0].header['EXPTIME']
            if not exptimelist or exptime not in exptimelist:
                exptimelist.append(int(exptime))

    os.chdir(telluricDirectory)
    for tgt_exp in exptimelist:
        # Make blackbody spectrum to be used in nifsScience.py
        file = open('std_star.txt','r')
        lines = file.readlines()
        #Extract stellar temperature from std_star.txt file , for use in making blackbody
        star_kelvin = float(lines[0].replace('\n','').split()[3])
        #Extract mag from std_star.txt file and convert to erg/cm2/s/A, for a rough flux scaling
        #find out if a matching band mag exists in std_star.txt
        logging.info("Band = " + str(band))
        if band == 'K':
            star_mag = lines[0].replace('\n','').split()[2]
            star_mag = float(star_mag)
        elif band == 'H':
            star_mag = lines[1].replace('\n','').split()[2]
            star_mag = float(star_mag)
        elif band == 'J':
            star_mag = lines[2].replace('\n','').split()[2]
            star_mag = float(star_mag)
        else:
            #if not then just set to 1; no relative flux cal. attempted
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in nifsReduce: No " + str(band) + " band magnitude found for this star.")
            logging.info("                            No relative flux calibration will be performed.")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

            logging.info("star_kelvin="), star_kelvin
            star_mag = 1
            logging.info("star_mag="), star_mag

        effspec(telluricDirectory, combined_extracted_1d_spectra, \
                star_mag, star_kelvin, over)



##################################################################################################################
#                                               TELLURIC FUNCTIONS                                               #
##################################################################################################################


def extrap1d(interpolator):
    """Extrap1d takes an interpolation function and returns a function which can also extrapolate.
    From https://stackoverflow.com/questions/2745329/how-to-make-scipy-interpolate-give-an-extrapolated-result-beyond-the-input-range
    """
    xs = interpolator.x
    ys = interpolator.y
    def pointwise(x):
        if x < xs[0]:
            return ys[0]+(x-xs[0])*(ys[1]-ys[0])/(xs[1]-xs[0])
        elif x > xs[-1]:
            return ys[-1]+(x-xs[-1])*(ys[-1]-ys[-2])/(xs[-1]-xs[-2])
        else:
            return interpolator(x)
    def ufunclike(xs):
        return array(map(pointwise, array(xs)))
    return ufunclike

#--------------------------------------------------------------------------------------------------------------------------------#

def readCube(cube):
    """Open a data cube with astropy.io.fits. Read the data header to find the starting wavelength and wavelength increment.
        Create a 1D array with length equal to the spectral dimension of the cube.
        For each element in array, element[i] = starting wavelength + (i * wavelength increment).

        Returns:
            cube (object reference):   Reference to the opened data cube.
            cubewave (1D numpy array): array representing pixel-wavelength mapping of data cube.

    """
    # read cube into an HDU list
    cube = astropy.io.fits.open(cube)

    # find the starting wavelength and the wavelength increment from the science header of the cube
    wstart = cube[1].header['CRVAL3']
    wdelt = cube[1].header['CD3_3']

    # initialize a wavelength array
    cubewave = np.zeros(2040)

    # create a wavelength array using the starting wavelength and the wavelength increment
    for i in range(2040):
        cubewave[i] = wstart+(i*wdelt)

    return cube, cubewave


##################################################################################################################
#                                       FLUX CALIBRATION FUNCTIONS                                               #
##################################################################################################################

def mag2mass(name, path, spectemp, mag, band):
    """Find standard star spectral type, temperature, and magnitude. Write results
       to std_star.txt in cwd.

    Executes a SIMBAD query and parses the resulting html to find spectal type,
    temperature and/or magnitude.

        Args:
            name (string): RA, d, Dec, d (for negatives); RA, +d, Dec, d (for positives).
            path: current working directory (usually with Nifty files).
            spectemp: specified at command line with -e.
            mag: specified at command line with -f.
            band: from the telluric standard .fits file header. Eg 'J', 'K'.

    """

    starfile = 'std_star.txt'
    kelvinfile = RUNTIME_DATA_PATH+'new_starstemp.txt'

    sf = open(starfile,'w')
    klf = open (kelvinfile)
    Kmag = ''
    Jmag = ''
    Hmag = ''

    # check to see if a spectral type or temperature has been given
    if spectemp:
        if not isinstance(spectemp[0], int):
            spectral_type = spectemp
            specfind = False
            tempfind = True
        else:
            kelvin = spectemp
            tempfind = False
            specfind = False
    else:
        specfind = True
        tempfind = True
    if mag:
        magfind = False
        if band=='K':
            Kmag=mag
        if band=='H':
            Hmag=mag
        if band=='J':
            Jmag=mag
    else:
        magfind = True

    if specfind or tempfind or magfind:
        #Construct URL based on standard star coords, execute SIMBAD query to find spectral type
        name = name.replace("+","%2b")
        name = name.replace("-", "%2D")
        start_name='http://simbad.u-strasbg.fr/simbad/sim-coo?Coord='
        end_name = '&submit=submit%20query&Radius.unit=arcsec&Radius=10'
        www_page = start_name+name+end_name
        f = urllib.urlopen(www_page)
        html2 = f.read()
        html2 = html2.replace(' ','')
        search_error = str(html2.split('\n'))


        #Exit if the lookup found nothing.
        if 'Noastronomicalobjectfound' in search_error:
            logging.info("ERROR: no object was found at the coordinates you entered. You'll need to supply information in a file; see the manual for instructions.")

        #If >1 object found, decrease search radius and try again
        if 'Numberofrows:' in search_error:
            start_name='http://simbad.u-strasbg.fr/simbad/sim-coo?Coord='
            end_name = '&submit=submit%20query&Radius.unit=arcsec&Radius=1'
            www_page = start_name+name+end_name
            f = urllib.urlopen(www_page)
            html2 = f.read()
            html2 = html2.replace(' ','')
            search_error = str(html2.split('\n'))

        #If that didn't return anything, exit and let the user sort it out
        if 'Noastronomicalobjectfound' in search_error:
            logging.info("ERROR: didn't find a star at your coordinates within a search radius of 10 or 1 arcsec. You'll need to supply information in a file; see the manual for instructions.")
            sys.exit()


        # Split source by \n into a list
        html2 = html2.split('\n')

        if specfind:
            count = 0
            aux = 0
            for line in html2:
                if (line[0:13] == 'Spectraltype:') :
                    numi = aux + 5
                    count = 0
                    break
                else:
                    count += 1
                aux += 1
            logging.info(html2[aux:numi+1])
            spectral_type = str(html2[numi][0:3])
            if count > 0:
                logging.info("ERROR: problem with SIMBAD output. You'll need to supply the spectral type or temperature in the command line prompt.")
                sys.exit()


        if magfind:
            for line in html2:

                if 'Fluxes' in line:
                    i = html2.index(line)
                    break
            while 'IMGSRC' not in html2[i]:
                if all(s in html2[i] for s in ('K', '[', ']')):
                    if 'C' in html2[i+2]:
                        index = html2[i].index('[')
                        Kmag = html2[i][1:index]
                if all(s in html2[i] for s in ('H', '[', ']')):
                    if 'C' in html2[i+2]:
                        index = html2[i].index('[')
                        Hmag = html2[i][1:index]
                if all(s in html2[i] for s in ('J', '[', ']')):
                    if 'C' in html2[i+2]:
                        index = html2[i].index('[')
                        Jmag = html2[i][1:index]
                i+=1
                if i>len(html2):
                    logging.info("ERROR: problem with SIMBAD output. You'll need to supply the magniture in the command line prompt.")

        if not Kmag:
            Kmag = 'nothing'
        if not Jmag:
            Jmag = 'nothing'
        if not Hmag:
            Hmag = 'nothing'

        if tempfind:
            #Find temperature for this spectral type in kelvinfile
            count = 0
            for line in klf:
                if '#' in line:
                    continue
                else:
                    if	spectral_type in line.split()[0]:
                        kelvin = line.split()[1]
                        count = 0
                        break
                    else:
                        count+=1

            if count > 0:
                logging.info("ERROR: can't find a temperature for spectral type"+ str(spectral_type)+". You'll need to supply information in a file; see the manual for instructions.")
                sys.exit()


        # Write results to std_star.txt
        if (Kmag or Jmag or Hmag) and Kmag!='x' and magfind:
            logging.info("magnitudes retrieved OK")
            sf.write('k K '+Kmag+' '+kelvin+'\n')
            sf.write('h H '+Hmag+' '+kelvin+'\n')
            sf.write('j J '+Jmag+' '+kelvin+'\n')
            sf.write('j J '+Jmag+' '+kelvin+'\n')

        elif (Kmag or Jmag or Hmag) and Kmag!='x' and not magfind:
            sf.write('k K '+Kmag+' '+kelvin+'\n')
        elif Kmag=='x':
            logging.info("WARNING: no magnitudes found for standard star. Doing relative flux calibration only.")
            sf.write('k K N/A '+kelvin+' \n')
            sf.write('h H N/A '+kelvin+' \n')
            sf.write('j J N/A '+kelvin+' \n')
            sf.write('j J N/A '+kelvin+' \n')

    sf.close()
    klf.close()

#-------------------------------------------------------------------------------#

def write_line_positions(nextcur, var):
    """Write line x,y info to file containing Lorentz fitting commands for bplot

    """

    curfile = open(nextcur, 'w')
    i=-1
    for line in var:
        i+=1
        if i!=0:
            var[i]=var.split()
            var[i][2]=var[i][2].replace("',",'').replace("']", '')
        if not i%2 and i!=0:
            #even number, means RHS of H line
            #write x and y position to file, also "k" key
            curfile.write(var[i][0]+" "+var[i][2]+" 1 k \n")
            #LHS of line, write info + "l" key to file
            curfile.write(var[i-1][0]+" "+var[i-1][2]+" 1 l \n")
            #now repeat but writing the "-" key to subtract the fit
            curfile.write(var[i][0]+" "+var[i][2]+" 1 - \n")
            curfile.write(var[i-1][0]+" "+var[i-1][2]+" 1 - \n")
        curfile.write("0 0 1 i \n")
        curfile.write("0 0 q \n")
        curfile.close()

#-------------------------------------------------------------------------------#

def vega(spectrum, band, path, hlineinter, airmass, telluric_shift_scale_record, log, over):
    """Use iraf.telluric to remove H lines from standard star, then remove
    normalization added by telluric with iraf.imarith.

    The extension for vega_ext.fits is specified from band (from header of
    telluricfile.fits).

    Args:
        spectrum (string): filename from 'telluricfile'.
        band: from telluricfile .fits header. Eg 'K', 'H', 'J'.
        path: usually top directory with Nifty scripts.
        hlineinter (boolean): Interactive H line fitting. Specified with -i at
                              command line. Default False.
        airmass: from telluricfile .fits header.
        telluric_shift_scale_record: "pointer" to telluric_hlines.txt.
        log: path to logfile.
        over (boolean): overwrite old files. Specified at command line.

    """
    if band=='K':
        ext = '1'
    if band=='H':
        ext = '2'
    if band=='J':
        ext = '3'
    if band=='Z':
        ext = '4'
    if os.path.exists("tell_nolines"+band+".fits"):
            if over:
                os.remove("tell_nolines"+band+".fits")
                tell_info = iraf.telluric(input=spectrum+"[1]", output='tell_nolines'+band, cal=RUNTIME_DATA_PATH+'vega_ext.fits['+ext+']', answer='yes', ignoreaps='yes', xcorr='yes', airmass = airmass, tweakrms='yes', inter=hlineinter, threshold=0.1, lag=3, shift=0., dshift=0.05, scale=.75, dscale=0.05, offset=0., smooth=1, cursor='', mode='al', Stdout=1)
            else:
                logging.info("Output file exists and -over not set - skipping H line correction")
    else:
        tell_info = iraf.telluric(input=spectrum+"[1]", output='tell_nolines'+band, cal=RUNTIME_DATA_PATH+'vega_ext.fits['+ext+']', answer='yes', ignoreaps='yes', xcorr='yes', airmass = airmass, tweakrms='yes', inter=hlineinter, threshold=0.1, lag=3, shift=0., dshift=0.05, scale=1., dscale=0.05, offset=0, smooth=1, cursor='', mode='al', Stdout=1)

    # record shift and scale info for future reference
    telluric_shift_scale_record.write(str(tell_info)+'\n')
    # need this loop to identify telluric output containing warning about pix outside calibration limits (different formatting)
    if "limits" in tell_info[-1].split()[-1]:
        norm=tell_info[-2].split()[-1]
    else:
        norm=tell_info[-1].split()[-1]

    if os.path.exists("final_tel_no_hlines_no_norm"+band+".fits"):
        if over:
            os.remove("final_tel_no_hlines_no_norm"+band+".fits")
            iraf.imarith(operand1='tell_nolines'+band, op='/', operand2=norm, result='final_tel_no_hlines_no_norm'+band, title='', divzero=0.0, hparams='', pixtype='', calctype='', verbose='yes', noact='no', mode='al')
        else:
            logging.info("Output file exists and -over not set - skipping H line normalization")
    else:
        iraf.imarith(operand1='tell_nolines'+band, op='/', operand2=norm, result='final_tel_no_hlines_no_norm'+band, title='', divzero=0.0, hparams='', pixtype='', calctype='', verbose='yes', noact='no', mode='al')

#-------------------------------------------------------------------------------#

def linefitAuto(spectrum, band):
    """automatically fit Lorentz profiles to lines defined in existing cur* files
    Go to x position in cursor file and use space bar to find spectrum at each of those points
    """

    specpos = iraf.bplot(images=spectrum+'[SCI,1]', cursor='cur'+band, Stdout=1, StdoutG='/dev/null')
    specpose = str(specpos).split("'x,y,z(x):")
    nextcur = 'nextcur'+band+'.txt'
    # Write line x,y info to file containing Lorentz fitting commands for bplot
    write_line_positions(nextcur, specpos)
    iraf.delete('final_tel_no_hlines_no_norm'+band+'.fits,Lorentz'+band,ver="no",go_ahead='yes',Stderr='/dev/null')
    # Fit and subtract Lorentz profiles. Might as well write output to file.
    iraf.bplot(images=spectrum+'[sci,1]',cursor='nextcur'+band+'.txt', new_image='final_tel_no_hlines_no_norm'+band, overwrite="yes",StdoutG='/dev/null',Stdout='Lorentz'+band)

#-------------------------------------------------------------------------------#

def linefitManual(spectrum, band):
    """ Enter splot so the user can fit and subtract lorents (or, actually, any) profiles
    """

    iraf.splot(images=spectrum, new_image='final_tel_no_hlines_no_norm'+band, save_file='../PRODUCTS/lorentz_hlines.txt', overwrite='yes')
    # it's easy to forget to use the 'i' key to actually write out the line-free spectrum, so check that it exists:
    # with the 'tweak' options, the line-free spectrum will already exists, so this lets the user simply 'q' and move on w/o editing (too bad if they edit and forget to hit 'i'...)
    while True:
        try:
            with open("final_tel_no_hlines_no_norm"+band+".fits") as f: pass
            break
        except IOError as e:
            logging.info("It looks as if you didn't use the i key to write out the lineless spectrum. We'll have to try again. --> Re-entering splot")
            iraf.splot(images=spectrum, new_image='final_tel_no_hlines_no_norm'+band, save_file='../PRODUCTS/lorentz_hlines.txt', overwrite='yes')

#-------------------------------------------------------------------------------#

def effspec(telDir, combined_extracted_1d_spectra, mag, T, over):
    """This flux calibration method was adapted to NIFS.

    Args:
        telDir: telluric directory.
        combined_extracted_1d_spectra:
        final_tel_no_hlines_no_norm (string):
        mag:
        T: temperature in kelvin.
        over (boolean): overwrite old files.

    """

    # define constants
    c = 2.99792458e8
    h = 6.62618e-34
    k = 1.3807e-23

    logging.info('Input Standard spectrum for flux calibration is ' +  str(combined_extracted_1d_spectra))

    if os.path.exists('c'+combined_extracted_1d_spectra+'.fits'):
        if not over:
            logging.info('Output already exists and -over- not set - calculation of efficiency spectrum')
            return
        if over:
            os.remove('c'+combined_extracted_1d_spectra+'.fits')
            pass

    combined_spectra_file = astropy.io.fits.open(combined_extracted_1d_spectra+'.fits')
    band = combined_spectra_file[0].header['GRATING'][0]
    exptime = float(combined_spectra_file[0].header['EXPTIME'])
    telfilter = combined_spectra_file[0].header['FILTER']

    # Create a black body spectrum at a given temperature.
    # Create a 1D array equal in length to the nfextracted 1d spectrum. Eg: length == 2040
    bb_spectrum_wavelengths = np.zeros(combined_spectra_file[1].header['NAXIS1'])
    # Find the wavelength at the start of the nfextracted 1d spectrum.
    wstart = combined_spectra_file[1].header['CRVAL1']
    # Find the change in wavelength with each pixel of the nfextracted 1d spectrum.
    wdelt = combined_spectra_file[1].header['CD1_1']
    # Starting at wstart, at intervals of wdelt, write a wavelength into each element of bb_spectrum_wavelengths.
    for i in range(len(bb_spectrum_wavelengths)):
        bb_spectrum_wavelengths[i] = wstart+(i*wdelt)
    # Find the central wavelength of the original nfextracted and combined 1d spectra.
    # We will use this later to scale the ouput spectrum of dividing by the blackbody back to the units of
    # the original observed star spectrum.
    central_wavelength = combined_spectra_file[0].header['WAVELENG']
    # Find the index of of the blackbody spectrum array (and hence also the final efficiency
    # spectrum array) that corresponds to the central wavelength.
    central_wavelength_index = np.where(bb_spectrum_wavelengths==min(bb_spectrum_wavelengths, key=lambda x:abs(x-central_wavelength)))
    # Define a function of wavelength and T...
    blackbodyFunction = lambda x, T: (2.*h*(c**2)*(x**(-5))) / ( (np.exp((h*c)/(x*k*T))) - 1 )
    # Evaluate that function at each wavelength of the bb_spectrum_wavelengths array, at the temperature of the standard star.
    blackbodySpectrum = (blackbodyFunction(bb_spectrum_wavelengths*1e-10, T))*1e-7

    # Divide final telluric correction spectrum by blackbody spectrum.
    final_telluric = astropy.io.fits.open('final_tel_no_hlines_no_norm'+band+'.fits')
    # Multiply by the gain to go from ADU to counts.
    final_telluric[0].data *= 2.8
    tel_bb = final_telluric[0].data/blackbodySpectrum

    # Calculate the f0 constant.
    # Begin to create the function to calculate the f0 constant.
    f0FunctionIncomplete = lambda p, T: p[0]*(np.log(T)**2)+p[1]*np.log(T)+p[2]

    # Look up the coefficients for the appropriate grating and filter.
    if 'HK' in telfilter:
        coeff =[1.97547589e-02, -4.19035839e-01, -2.30083083e+01]
        central_wavelength = 22000.
    if 'JH' in telfilter:
        coeff = [1.97547589e-02, -4.19035839e-01,  -2.30083083e+01]
        central_wavelength = 15700.
    if 'ZJ' in telfilter:
        coeff = [0.14903624, -3.14636068, -9.32675924]
        central_wavelength = 11100.

    # Evaluate the function at the given temperature and coefficients to return a constant. Return e**result as the f0 constant.
    f0 = np.exp(f0FunctionIncomplete(coeff, T))

    logging.info(tel_bb)
    logging.info(exptime)
    logging.info((final_telluric[0].data[central_wavelength_index[0]]/tel_bb[central_wavelength_index[0]]))
    logging.info((10**(0.4*mag)))
    logging.info((f0)**-1)

    effspec =  (tel_bb/exptime)*(final_telluric[0].data[central_wavelength_index[0]]/tel_bb[central_wavelength_index[0]])*(10**(0.4*mag))*(f0)**-1

    # Modify our working copy of the original extracted 1d spectrum. Note though that we aren't permanently writing these changes to disk.
    combined_spectra_file[1].data = effspec
    # Don't write our changes to the original extracted 1d spectra; write them to a new file, 'c'+combined...+'.fits'.
    combined_spectra_file.writeto('c'+combined_extracted_1d_spectra+'.fits',  output_verify='ignore')
    writeList('c'+combined_extracted_1d_spectra, 'finalcorrectionspectrum', telDir)

#-------------------------------------------------------------------------------#

if __name__ == '__main__':
    a = raw_input('Enter <Science> for science reduction or <Telluric> for telluric reduction: ')
    start(a)
