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

import logging, os, pkg_resources, glob, shutil
import astropy.io.fits
from pyraf import iraf, iraffunctions

# LOCAL

# Import config parsing.
from ..configobj.configobj import ConfigObj

# Import custom Nifty functions.
from ..nifsUtils import datefmt, listit, checkLists, copyCalibration, copyCalibrationDatabase

# Define constants.
# Paths to Nifty data.
RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

def start(calibrationDirectoryList=""):
    """
         nifsBaselineCalibration

         This module contains all the functions needed to reduce
         NIFS GENERAL BASELINE CALIBRATIONS

         INPUT FILES FOR EACH BASELINE CALIBRATION:

         Raw files:
           - Flat frames (lamps on)
           - Flat frames (lamps off)
           - Arc frames
           - Arc dark frames
           - Ronchi mask flat frames

         OUTPUT FILES:
         - Shift file. Eg: sCALFLAT.fits
         - Bad Pixel Mask. Eg: rgnCALFLAT_sflat_bmp.pl
         - Flat field. Eg: rgnCALFLAT_flat.fits
         - Reduced arc frame. Eg: wrgnARC.fits
         - Reduced ronchi mask. Eg: rgnRONCHI.fits
         - Reduced dark frame. Eg: rgnARCDARK.fits

    Args:
        # Loaded from runtimeData/config.cfg
        calibrationDirectoryList:      list of paths to calibrations. ['path/obj/date/Calibrations_grating']
        over (boolean):  overwrite old files. Default: False.
        start (int):     starting step of daycal reduction. Specified at command line with -a. Default: 1.
        stop (int):      stopping step of daycal reduction. Specified at command line with -z. Default: 6.
        manualMode (boolean): enable optional manualModeging pauses. Default: False.

    """

    # TODO(nat): stop using first frame from list as name for combined frames. Find better names and implement
    # them in pipeline and docs.
    # TODO(nat): Finish converting the print statements to logging.info() statements.

    # Store current working directory for later use.
    path = os.getcwd()

    # Set up the logging file.
    log = os.getcwd()+'/Nifty.log'

    logging.info('\n#################################################')
    logging.info('#                                               #')
    logging.info('# Start the NIFS Baseline Calibration Reduction #')
    logging.info('#                                               #')
    logging.info('#################################################\n')

    # Set up/prepare IRAF.
    iraf.gemini()
    iraf.nifs()
    iraf.gnirs()
    iraf.gemtools()

    # Reset to default parameters the used IRAF tasks.
    iraf.unlearn(iraf.gemini,iraf.gemtools,iraf.gnirs,iraf.nifs)

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

    # Load reduction parameters from ./config.cfg.
    with open('./config.cfg') as config_file:
        config = ConfigObj(config_file, unrepr=True)
        # Read general pipeline config.
        manualMode = config['manualMode']
        over = config['over']
        if not calibrationDirectoryList:
            calibrationDirectoryList = config['calibrationDirectoryList']
        # Read baselineCalibrationReduction specfic config.
        calibrationReductionConfig = config['calibrationReductionConfig']
        start = calibrationReductionConfig['baselineCalibrationStart']
        stop = calibrationReductionConfig['baselineCalibrationStop']

    ################################################################################
    # Define Variables, Reduction Lists AND identify/run number of reduction steps #
    ################################################################################

    # Loop over the Calibrations directories and reduce the day calibrations in each one.
    for calpath in calibrationDirectoryList:
        os.chdir(calpath)
        pwdDir = os.getcwd()+"/"
        iraffunctions.chdir(pwdDir)

        # However, don't do the reduction for a Calibration_"grating" directory without associated telluric or science data.
        # Check that a "grating" directory exists at the same level as the Calibrations_"grating" directory.
        # If not, skip the reduction of calibrations in that Calibrations_grating directory.
        # "grating" should be the last letter of calpath.
        grating = calpath[-1]
        if not os.path.exists("../"+grating):

            print "\n##############################################################################"
            print ""
            print "  No grating directory (including science or telluric data) found for  "
            print "  ", calpath
            print "  Skipping reduction of calibrations in that directory."
            print ""
            print "##############################################################################\n"

            continue

        # Create lists of each type of calibration from textfiles in Calibrations directory.
        flatlist = open('flatlist', "r").readlines()
        flatdarklist = open("flatdarklist", "r").readlines()
        arcdarklist = open("arcdarklist", "r").readlines()
        arclist = open("arclist", "r").readlines()
        ronchilist = open("ronchilist", "r").readlines()

        # Store the name of the first image of each calibration-type-list in
        # a variable for later use (Eg: calflat). This is because gemcombine will
        # merge a list of files (Eg: "n"+flatlist) and the output file will have the same
        # name as the first file in the list (Eg: calflat). These first file names are used
        # later in the pipeline.
        calflat = (flatlist[0].strip()).rstrip('.fits')
        flatdark = (flatdarklist[0].strip()).rstrip('.fits')
        arcdark = (arcdarklist[0].strip()).rstrip('.fits')
        arc = (arclist[0].strip()).rstrip('.fits')
        ronchiflat = (ronchilist[0].strip()).rstrip('.fits')

        # Check start and stop values for reduction steps. Ask user for a correction if
        # input is not valid.
        valindex = start
        while valindex > stop  or valindex < 1 or stop > 4:
            print "\n#####################################################################"
            print "#####################################################################"
            print ""
            print "     WARNING in calibrate: invalid start/stop values of calibration "
            print "                           reduction steps."
            print ""
            print "#####################################################################"
            print "#####################################################################\n"

            valindex = int(raw_input("\nPlease enter a valid start value (1 to 4, default 1): "))
            stop = int(raw_input("\nPlease enter a valid stop value (1 to 4, default 4): "))

        # Print the current directory of calibrations being processed.
        print "\n#################################################################################"
        print "                                   "
        print "  Currently working on calibrations "
        print "  in ", calpath
        print "                                   "
        print "#################################################################################\n"


        while valindex <= stop:

            #############################################################################
            ##  STEP 1: Determine the shift to the MDF (mask definition file)          ##
            ##          using nfprepare (nsoffset). Ie: locate the spectra.            ##
            ##  Output: First image in flatlist with "s" prefix.                       ##
            #############################################################################

            if valindex == 1:
                if manualMode:
                    a = raw_input("About to enter step 1: locate the spectrum.")
                getShift(calflat, grating, over, log)
                print "\n###################################################################"
                print ""
                print "    STEP 1: Locate the Spectrum (Determine the shift to the MDF) - COMPLETED"
                print ""
                print "###################################################################\n"

            #############################################################################
            ##  STEP 2: Create Flat Field frame and BPM (Bad Pixel Mask)               ##
            ##  Output: Flat Field image with spatial and spectral information.        ##
            ##          First image in flatlist with  "rgn" prefix and "_flat" suffix. ##
            #############################################################################

            elif valindex == 2:
                if manualMode:
                    a = raw_input("About to enter step 2: flat field.")
                makeFlat(flatlist, flatdarklist, calflat, flatdark, grating, over, log)
                print "\n###################################################################"
                print ""
                print "    STEP 2: Flat Field (Create Flat Field image and BPM image) - COMPLETED       "
                print ""
                print "###################################################################\n"

            ############################################################################
            ##  STEP 3: NFPREPARE and Combine arc darks.                              ##
            ##          NFPREPARE, Combine and flat field arcs.                       ##
            ##          Determine the wavelength solution and create the wavelength   ##
            ##          referenced arc.                                               ##
            ############################################################################

            elif valindex == 3:
                if manualMode:
                    a = raw_input("About to enter step 3: wavelength solution.")
                makeWaveCal(arclist, arc, arcdarklist, arcdark, grating, log, over, path)
                print "\n###################################################################"
                print ""
                print "         STEP 3: Wavelength Solution (NFPREPARE and Combine arc darks.  "
                print "                 NFPREPARE, Combine and flat field arcs."
                print "                 Determine the wavelength solution and create the"
                print "                 wavelength referenced arc) - COMPLETED"
                print ""
                print "###################################################################\n"

            ######################################################################################
            ##  Step 4: Trace the spatial curvature and spectral distortion in the Ronchi flat. ##
            ######################################################################################

            elif valindex == 4:
                if manualMode:
                    a = raw_input("About to enter step 4: spatial distortion.")
                makeRonchi(ronchilist, ronchiflat, calflat, grating, over, flatdark, log)
                print "\n###################################################################"
                print ""
                print "     Step 4: Spatial Distortion (Trace the spatial curvature and spectral distortion "
                print "             in the Ronchi flat) - COMPLETED"
                print ""
                print "###################################################################\n"

            else:
                print "\nERROR in nifs_baseline_calibration: step ", valindex, " is not valid.\n"
                raise SystemExit

            valindex += 1

        print "\n##############################################################################"
        print ""
        print "  COMPLETE - Calibration reductions completed for "
        print "  ", calpath
        print ""
        print "##############################################################################\n"


    # Return to directory script was begun from.
    os.chdir(path)
    return

#####################################################################################
#                                        FUNCTIONS                                  #
#####################################################################################

def getShift(calflat, grating, over, log):
    """Determine the shift to the MDF file.

    Run NFPREPARE on a single "lamps on" flat to  determine  the
    shift  between IFU data and the definition of the Image Slicer
    position in the MDF file.  The output from this step  will  be  used
    in all subsequent calls to NFPREPARE as the "shiftimage".

    Args:
        calflat: the first lamps-on flat from flatlist

    """

    # This code structure checks if iraf output files already exist. If output files exist and
    # over (overwrite) is specified, iraf output is overwritten.
    if os.path.exists('s'+calflat+'.fits'):
        if over:
            os.remove('s'+calflat+'.fits')
            iraf.nfprepare(calflat,rawpath="",outpref="s", shiftx='INDEF', shifty='INDEF',fl_vardq='no',fl_corr='no',fl_nonl='no', fl_int='no', logfile=log)
        else:
            logging.info("\nOutput exists and -over not set - skipping find shift")
    else:
        iraf.nfprepare(calflat,rawpath="",outpref="s", shiftx='INDEF', shifty='INDEF',fl_vardq='no',fl_corr='no',fl_nonl='no', fl_int='no', logfile=log)

    # Put the name of the reference shift file into a text file called
    # shiftfile to be used by the pipeline later.
    open("shiftfile", "w").write("s"+calflat)

    copyCalibration('s'+calflat+'.fits', 'shiftFile.fits', grating, over)


#---------------------------------------------------------------------------------------------------------------------------------------#

def makeFlat(flatlist, flatdarklist, calflat, flatdark, grating, over, log):
    """Make flat and bad pixel mask.

    Use NFPREPARE on the lamps on/lamps off flats to update the
    raw data headers and attach the mask  definition  file  (MDF)  as  a
    binary  table  on all files.  Note that dark frames will not have an
    MDF attached by default.  Instead, the appropriate MDF is  added  in
    NSREDUCE or NSFLAT to match the data being reduced.

    Use  NSREDUCE to cut the calibration (flat/arc) spectra to
    the size specified by the  MDF,  placing  different  IFU  slices  in
    separate image extensions.

    Use  NSFLAT  to generate a normalized flat field (for each
    IFU slice or cross-dispersed order) from lamp flats.  A  mask  (BPM)
    will  also  be  generated by thresholding - this can be used to flag
    bad pixels in other data.

    Use NSSLITFUNCTION to produce the final flat.

    NSSLITFUNCTION extends the flatfield produced by correcting the
    NSFLAT normalization for inter-slice variations. The output
    from this task is used as the flatfield image for further
    reduction.

    """

    # Update lamps on flat frames with mdf offset value and generate variance and data quality extensions.
    for image in flatlist:
        image = str(image).strip()
        if os.path.exists('n'+image+'.fits'):
            if over:
                os.remove('n'+image+'.fits')
                iraf.nfprepare(image+'.fits',rawpath='.',shiftim="s"+calflat, fl_vardq='yes',fl_corr='no',fl_nonl='no', logfile=log)
            else:
                print "Output exists and -over- not set - skipping nfprepare of lamps on flats"
        else:
            iraf.nfprepare(image+'.fits',rawpath='.',shiftim="s"+calflat, fl_vardq='yes',fl_corr='no',fl_nonl='no', logfile=log)
    flatlist = checkLists(flatlist, '.', 'n', '.fits')

    # Update lamps off flat images with offset value and generate variance and data quality extensions.
    for image in flatdarklist:
        image = str(image).strip()
        if os.path.exists('n'+image+'.fits'):
            if over:
                iraf.delete('n'+image+'.fits')
                iraf.nfprepare(image+'.fits',rawpath='.',shiftim="s"+calflat, fl_vardq='yes',fl_corr='no',fl_nonl='no', logfile=log)
            else:
                print "\nOutput exists and -over- not set - skipping nfprepare of lamps off flats."
        else:
            iraf.nfprepare(image+'.fits',rawpath='.',shiftim="s"+calflat, fl_vardq='yes',fl_corr='no',fl_nonl='no', logfile=log)
    flatdarklist = checkLists(flatdarklist, '.', 'n', '.fits')

    # Combine lamps on flat images, "n"+image+".fits". Output combined file will have name of the first flat file with "gn" prefix.
    if os.path.exists('gn'+calflat+'.fits'):
        if over:
            iraf.delete("gn"+calflat+".fits")
            if len(flatlist) > 1:
                iraf.gemcombine(listit(flatlist,"n"),output="gn"+calflat,fl_dqpr='yes', fl_vardq='yes',masktype="none",logfile=log)
            else:
                iraf.copy('n'+calflat+'.fits', 'gn'+calflat+'.fits')
        else:
            print "\nOutput exists and -over- not set - skipping gemcombine of lamps on flats."
    else:
        if len(flatlist) > 1:
            iraf.gemcombine(listit(flatlist,"n"),output="gn"+calflat,fl_dqpr='yes', fl_vardq='yes',masktype="none",logfile=log)
        else:
            iraf.copy('n'+calflat+'.fits', 'gn'+calflat+'.fits')

    # Combine lamps off flat images, "n"+image+".fits". Output combined file will have name of the first darkflat file with "gn" prefix.
    if os.path.exists('gn'+flatdark+'.fits'):
        if over:
            iraf.delete("gn"+flatdark+".fits")
            if len(flatdarklist) > 1:
                iraf.gemcombine(listit(flatdarklist,"n"),output="gn"+flatdark,fl_dqpr='yes', fl_vardq='yes',masktype="none",logfile=log)
            else:
                iraf.copy('n'+flatdark+'.fits', 'gn'+flatdark+'.fits')
        else:
            print "\nOutput exists and -over- not set - skipping gemcombine of lamps on flats."
    else:
        if len(flatdarklist) > 1:
            iraf.gemcombine(listit(flatdarklist,"n"),output="gn"+flatdark,fl_dqpr='yes', fl_vardq='yes',masktype="none",logfile=log)
        else:
            iraf.copy('n'+flatdark+'.fits', 'gn'+flatdark+'.fits')

    # NSREDUCE on lamps on flat images, "gn"+calflat+".fits", to extract the slices and apply an approximate wavelength calibration.
    if os.path.exists('rgn'+calflat+'.fits'):
        if over:
            iraf.delete("rgn"+calflat+".fits")
            iraf.nsreduce ("gn"+calflat,fl_cut='yes',fl_nsappw='yes',fl_vardq='yes', fl_sky='no',fl_dark='no',fl_flat='no',logfile=log)
        else:
            print "\nOutput exists and -over- not set - skipping nsreduce of lamps on flats."
    else:
        iraf.nsreduce ("gn"+calflat,fl_cut='yes',fl_nsappw='yes',fl_vardq='yes', fl_sky='no',fl_dark='no',fl_flat='no',logfile=log)

    # NSREDUCE on lamps off flat frames, "gn"+flatdark+".fits", to extract the slices and apply an approximate wavelength calibration.
    if os.path.exists('rgn'+flatdark+'.fits'):
        if over:
            iraf.delete("rgn"+flatdark+".fits")
            iraf.nsreduce ("gn"+flatdark,fl_cut='yes',fl_nsappw='yes',fl_vardq='yes', fl_sky='no',fl_dark='no',fl_flat='no',logfile=log)
        else:
            print "\nOutput exists and -over- not set - skipping nsreduce of lamps off flats."
    else:
        iraf.nsreduce ("gn"+flatdark,fl_cut='yes',fl_nsappw='yes',fl_vardq='yes', fl_sky='no',fl_dark='no',fl_flat='no',logfile=log)

    # Create slice-by-slice flat field image and BPM image from the darkflats, using NSFLAT.
    # Lower and upper limit of bad pixels are 0.15 and 1.55.

    # Get the spectral band so we can fine tune thr_flo and thr_fup. This fine tunes the number of
    # bad pixels caught to an approximately constant level for each band. A few bad pixels will
    # not be caught, but it was found that catching them marked large portions of the top and bottom
    # rows of pixels of each slice as bad pixels.
    header = astropy.io.fits.open(calflat+'.fits')
    grat = header[0].header['GRATING'][0:1]
    if grat == 'Z' or grat == 'J':
        flo = 0.07
        fup = 1.55
        inter = 'no'
    elif grat == 'H' or grat == 'K':
        flo = 0.05
        fup = 1.55
        inter = 'no'
    else:
        print "\n#####################################################################"
        print "#####################################################################"
        print ""
        print "     WARNING in baselineCalibration: nsflat detected a non-standard wavelength "
        print "                                     configuration. Running interactively. "
        print ""
        print "#####################################################################"
        print "#####################################################################\n"
        # Arbitrary; not tested with non-standard configurations.
        flo = 0.15
        fup = 1.55
        inter = 'yes'

    if os.path.exists("rgn"+calflat+"_sflat.fits"):
        if over:
            iraf.delete("rgn"+flatdark+"_dark.fits")
            iraf.delete("rgn"+calflat+"_sflat.fits")
            iraf.delete("rgn"+calflat+"_sflat_bpm.pl")
            iraf.nsflat("rgn"+calflat,darks="rgn"+flatdark,flatfile="rgn"+calflat+"_sflat", \
                        darkfile="rgn"+flatdark+"_dark", fl_save_dark='yes',process="fit", \
                        thr_flo=flo,thr_fup=fup, fl_vardq='yes', fl_int=inter, logfile=log )
        else:
            print "\nOutput exists and -over- not set - skipping nsflat creation of preliminary flat"
    else:
        iraf.nsflat("rgn"+calflat,darks="rgn"+flatdark,flatfile="rgn"+calflat+"_sflat", \
                    darkfile="rgn"+flatdark+"_dark", fl_save_dark='yes',process="fit", \
                    thr_flo=flo,thr_fup=fup, fl_vardq='yes', fl_int=inter, logfile=log )

    # Renormalize the slices to account for slice-to-slice variations using NSSLITFUNCTION - make the final flat field image.

    if os.path.exists("rgn"+calflat+"_flat.fits"):
        if over:
            iraf.delete("rgn"+calflat+"_flat.fits")
            iraf.nsslitfunction("rgn"+calflat,"rgn"+calflat+"_flat", \
                                flat="rgn"+calflat+"_sflat",dark="rgn"+flatdark+"_dark",combine="median", \
                                order=3,fl_vary='no',logfile=log)
        else:
            print "\nOutput exists and -over- not set - skipping nsslitfunction flat rectification"
    else:
        iraf.nsslitfunction("rgn"+calflat,"rgn"+calflat+"_flat", \
                            flat="rgn"+calflat+"_sflat",dark="rgn"+flatdark+"_dark",combine="median", \
                            order=3,fl_vary='no',logfile=log)

    # Put the name of the final flat field and bad pixel mask (BPM) into text files of fixed name to be used by the pipeline later.

    open("flatfile", "w").write("rgn"+calflat+"_flat")              # Final flat field
    open("sflatfile", "w").write("rgn"+calflat+"_sflat")            # Flat field before renormalization (before nsslitfunction)
    open("sflat_bpmfile", "w").write("rgn"+calflat+"_sflat_bpm.pl") # Bad Pixel Mask

    # Copy to relevant science directory calibrations/ directories as well
    copyCalibration("rgn"+calflat+"_flat.fits", 'finalFlat.fits', grating, over)
    copyCalibration("rgn"+calflat+"_sflat.fits", 'preliminaryFlat.fits', grating, over)
    copyCalibration("rgn"+calflat+"_sflat_bpm.pl", 'finalBadPixelMask.pl', grating, over)

#--------------------------------------------------------------------------------------------------------------------------------#

def makeWaveCal(arclist, arc, arcdarklist, arcdark, grating, log, over, path):
    """Determine the wavelength solution of each slice of the observation and
    set the arc coordinate file.

    If the user wishes to change the coordinate file to a different
    one, they need only to change the "clist" variable to their line list
    in the coordli= parameter in the nswavelength call.

    Uses  NSWAVELENGTH to calibrate arc data (after cutting and
    optionally applying a flatfield with NSREDUCE in a previous step).


    DATA REDUCTION HINT -
    For the nswavelength call, the different wavelength settings
    use different vaues for some of the parameters. For optimal auto
    results, use:

    K-band: thresho=50.0, cradius=8.0   -->  (gives rms of 0.1 to 0.3)
    H-band: thresho=100.0, cradius=8.0  -->  (gives rms of 0.05 to 0.15)
    J-band: thresho=100.0               -->  (gives rms of 0.03 to 0.09)
    Z-band: Currently not working very well for non-interactive mode

    Note that better RMS fits can be obtained by running the wavelength
    calibration interactively and identifying all of the lines
    manually.  Tedious, but will give more accurate results than the
    automatic mode (i.e., fl_inter-).  Use fl_inter+ for manual mode.

    """

    # Store the name of the shift image in "shiftima".
    shiftima = open("shiftfile", "r").readlines()[0].strip()
    # Store the name of the bad pixel mask in "sflat_bpm".
    sflat_bpm = open("sflat_bpmfile", "r").readlines()[0].strip()
    # Store the name of the final flat field frame in "flat".
    flat = open("flatfile", "r").readlines()[0].strip()

    # Update arc images with offset value and generate variance and data
    # quality extensions. Results in "n"+image+".fits"
    for image in arclist:
        image = str(image).strip()
        if os.path.exists("n"+image+".fits"):
            if over:
                iraf.delete("n"+image+".fits")
            else:
                print "\nOutput file exists and -over not set - skipping nfprepare of arcs."
                continue
        iraf.nfprepare(image, rawpath=".", shiftimage=shiftima,bpm=sflat_bpm,\
                       fl_vardq="yes",fl_corr='no',fl_nonl='no',logfile=log)

    # Check that output files for all arc images exists from nfprepare; if output does not
    # exist remove corresponding arc images from arclist.
    arclist = checkLists(arclist, '.', 'n', '.fits')

    # Update arc dark frames with mdf offset value and generate variance and data
    # quality extensions. Results in "n"+image+".fits"
    for image in arcdarklist:
        image = str(image).strip()
        if os.path.exists("n"+image+".fits"):
            if over:
                iraf.delete("n"+image+".fits")
            else:
                print "\nOutput file exists and -over not set - skipping nfprepare of arcdarks."
                continue
        iraf.nfprepare(image, rawpath=".", shiftimage=shiftima, bpm=sflat_bpm, \
                       fl_vardq='yes',fl_corr='no',fl_nonl='no',logfile=log)

    # Check that output files for all arc images exists from nfprepare; if output does not
    # exist remove corresponding arc images from arclist.
    arcdarklist = checkLists(arcdarklist, '.', 'n', '.fits')

    # Combine arc frames, "n"+image+".fits". Output combined file will have the name of the first arc file.
    if os.path.exists("gn"+arc+".fits"):
        if over:
            iraf.delete("gn"+arc+".fits")
            if len(arclist) > 1:
                iraf.gemcombine(listit(arclist,"n"),output="gn"+arc, fl_dqpr='yes',fl_vardq='yes',masktype="none",logfile=log)
            else:
                iraf.copy('n'+arc+'.fits', 'gn'+arc+'.fits')
        else:
            print "\nOutput file exists and -over not set - skipping gemcombine of arcs."
    else:
        if len(arclist) > 1:
            iraf.gemcombine(listit(arclist,"n"),output="gn"+arc, fl_dqpr='yes',fl_vardq='yes',masktype="none",logfile=log)
        else:
            iraf.copy('n'+arc+'.fits', 'gn'+arc+'.fits')

    # Combine arc dark frames, "n"+image+".fits". Output combined file will have the name of the first arc dark file.
    if os.path.exists("gn"+arcdark+".fits"):
        if over:
            iraf.delete("gn"+arcdark+".fits")
            if len(arcdarklist) > 1:
                iraf.gemcombine(listit(arcdarklist,"n"),output="gn"+arcdark, fl_dqpr='yes',fl_vardq='yes',masktype="none",logfile=log)
            else:
                iraf.copy('n'+arcdark+'.fits', 'gn'+arcdark+'.fits')
        else:
            print "\nOutput file exists and -over not set - skipping gemcombine of arcdarks."
    else:
        if len(arcdarklist) > 1:
            iraf.gemcombine(listit(arcdarklist,"n"),output="gn"+arcdark, fl_dqpr='yes',fl_vardq='yes',masktype="none",logfile=log)
        else:
            iraf.copy('n'+arcdark+'.fits', 'gn'+arcdark+'.fits')

    # Put the name of the combined and prepared arc dark frame "gn"+arcdark into a text
    # file called arcdarkfile to be used by the pipeline later.
    open("arcdarkfile", "w").write("gn"+arcdark)

    # NSREDUCE on arc images "gn"+arc+".fits" to extract the slices and apply an approximate
    # wavelength calibration. Results in "rgn"+image+".fits"
    if os.path.exists("rgn"+arc+".fits"):
        if over:
            iraf.delete("rgn"+arc+".fits")
            iraf.nsreduce("gn"+arc, darki="gn"+arcdark, flatimage=flat, \
                          fl_vardq="no", fl_cut="yes", fl_nsappw="yes", fl_sky="no", fl_dark="yes", fl_flat="yes", \
                          logfile=log)
        else:
            print "\nOutput file exists and -over not set - skipping apply_flat_arc."
    else:
        iraf.nsreduce("gn"+arc, darki="gn"+arcdark, flatimage=flat, \
                      fl_vardq="no", fl_cut="yes", fl_nsappw="yes", fl_sky="no", fl_dark="yes", fl_flat="yes", \
                      logfile=log)
    #fl_dark = "no"
    #if arcdark != "":
    #    fl_dark = "yes"
    #hdulist = astropy.io.fits.open(arc+'.fits')
    #if 'K_Long' in hdulist[0].header['GRATING']:
    #    iraf.nsreduce("gn"+arc, darki=arcdark, fl_cut="yes", fl_nsappw="yes", crval = 23000., fl_dark="yes", fl_sky="no", fl_flat="yes", flatimage=flat, fl_vardq="no",logfile=log)

    # Put the name of the combined and prepared arc dark frame "gn"+arcdark into a text
    # file called arcdarkfile to be used by the pipeline later.
    open("arcdarkfile", "w").write("gn"+arcdark)

    # Determine the wavelength setting.
    hdulist = astropy.io.fits.open("rgn"+arc+".fits")
    band = hdulist[0].header['GRATING'][0:1]
    central_wavelength = float(hdulist[0].header['GRATWAVE'])

    # Set interactive mode. Default False for standard configurations (and True for non-standard wavelength configurations ).
    pauseFlag = False

    if band == "K" and central_wavelength == 2.20:
        clist=RUNTIME_DATA_PATH+"k_ar.dat"
        my_thresh = 50.0
    elif band == "J":
        clist=RUNTIME_DATA_PATH+"j_ar.dat"
        my_thresh=100.0
    elif band == "H":
        clist=RUNTIME_DATA_PATH+"h_ar.dat"
        my_thresh=100.0
    elif band == "Z":
        clist="nifs$data/ArXe_Z.dat"
        my_thresh=100.0
    else:
        # Print a warning that the pipeline is being run with non-standard grating.
        print "\n#####################################################################"
        print "#####################################################################"
        print ""
        print "   WARNING in calibrate: found a non-standard (non Z, J, H or K) "
        print "                         wavelength configuration."
        print "                         NSWAVELENGTH will be run interactively."
        print ""
        print "#####################################################################"
        print "#####################################################################\n"

        clist="gnirs$data/argon.dat"
        my_thresh=100.0
        interactive = 'yes'

    # TODO(nat): I don't like this nesting at all
    if not pauseFlag:
        # Establish wavelength calibration for arclamp spectra. Output: A series of
        # files in a "database/" directory containing the wavelength solutions of
        # each slice and a reduced arc frame "wrgn"+ARC+".fits".
        if os.path.exists("wrgn"+arc+".fits"):
            if over:
                iraf.delete("wrgn"+arc+".fits")
                iraf.nswavelength("rgn"+arc, coordli=clist, nsum=10, thresho=my_thresh, \
                                  trace='yes', fwidth=2.0, match=-6,cradius=8.0,fl_inter='no',nfound=10,nlost=10, \
                                  logfile=log)
            else:
                print "\nOutput file exists and -over not set - ",\
                "not determining wavelength solution and recreating the wavelength reference arc.\n"
        else:
            iraf.nswavelength("rgn"+arc, coordli=clist, nsum=10, thresho=my_thresh, \
                              trace='yes', fwidth=2.0, match=-6,cradius=8.0,fl_inter='no',nfound=10,nlost=10, \
                              logfile=log)
    else:
        a = raw_input("For now, interactive Z or non-standard wavelength calibrations are unsupported. " + \
        "Bugs running IRAF tasks interactively from python mean iraf.nswavelength cannot be activated automatically. " + \
        "Therefore please run iraf.nswavelength() interactively from Pyraf to do a wavelength calibration by hand.")

    # Copy to relevant science observation/calibrations/ directories
    copyCalibration("wrgn"+arc+".fits", 'finalArc.fits', grating, over)
    copyCalibrationDatabase("idwrgn", grating, over)

#--------------------------------------------------------------------------------------------------------------------------------#

def makeRonchi(ronchilist, ronchiflat, calflat, grating, over, flatdark, log):
    """Establish Spatial-distortion calibration with nfsdist.

    NFSDIST uses the information in the "Ronchi" Calibration images
    to calibrate the spatial dimension of the NIFS IFU field. The
    Ronchi frame is a dispersed flat field image with a slit-mask
    in the field so that the illumination on the IFU is in a
    pattern of ~10 different slitlets that are stacked in the
    y-dimension on the field. Proper alignment of the slits across
    the image slicer pattern can be used for spatial rectification
    of the on-sky science data. The spatial solution determined by
    NFSDIST is linked to the science data in NFFITCOORDS.

    """

    # Update ronchi flat frames with offset value and generate variance and data quality extensions.
    # Output: "n"+image+".fits".
    for image in ronchilist:
        image = str(image).strip()
        if os.path.exists("n"+image+'.fits'):
            if over:
                iraf.delete("n"+image+'.fits')
                iraf.nfprepare(image,rawpath=".", shiftimage="s"+calflat, \
                               bpm="rgn"+calflat+"_sflat_bpm.pl", fl_vardq="yes",fl_corr="no",fl_nonl="no", \
                               logfile=log)
            else:
                print "\nOutput file exists and -over not set - skipping prepare of ronchis"
        else:
            iraf.nfprepare(image,rawpath=".", shiftimage="s"+calflat, \
                           bpm="rgn"+calflat+"_sflat_bpm.pl", fl_vardq="yes",fl_corr="no",fl_nonl="no", \
                           logfile=log)
    ronchilist = checkLists(ronchilist, '.', 'n', '.fits')

    # Combine nfprepared ronchi flat images "n"+image+".fits". Output: combined file will
    # have the name of the first ronchi flat file, "gn"+ronchiflat+".fits".
    if os.path.exists("gn"+ronchiflat+".fits"):
        if over:
            iraf.delete("gn"+ronchiflat+".fits")
            if len(ronchilist) > 1:
                iraf.gemcombine(listit(ronchilist,"n"),output="gn"+ronchiflat,fl_dqpr="yes", \
                                       masktype="none",fl_vardq="yes",logfile=log)
            else:
                iraf.copy("n"+ronchiflat+".fits","gn"+ronchiflat+".fits")
        else:
            "\nOutput file exists and -over not set - skipping combine of ronchis"
    else:
        if len(ronchilist) > 1:
            iraf.gemcombine(listit(ronchilist,"n"),output="gn"+ronchiflat,fl_dqpr="yes", \
                                   masktype="none",fl_vardq="yes",logfile=log)
        else:
            iraf.copy("n"+ronchiflat+".fits","gn"+ronchiflat+".fits")

    # NSREDUCE combined ronchi frame, "gn"+ronchiflat+".fits", to extract the slices into unique MEF extensions and
    # apply an approximate wavelength calibration to each slice. Output: "rgn"+ronchiflat+".fits".
    if os.path.exists("rgn"+ronchiflat+".fits"):
        if over:
            iraf.delete("rgn"+ronchiflat+".fits")
            iraf.nsreduce("gn"+ronchiflat, outpref="r", dark="rgn"+flatdark+"_dark", flatimage="rgn"+calflat+"_flat", fl_cut="yes", fl_nsappw="yes", fl_flat="yes", fl_sky="no", fl_dark="yes", fl_vardq="no", logfile=log)
        else:
            "\nOutput file exists and -over not set - skipping nsreduce of ronchis"
    else:
        iraf.nsreduce("gn"+ronchiflat, outpref="r", dark="rgn"+flatdark+"_dark", flatimage="rgn"+calflat+"_flat", fl_cut="yes", fl_nsappw="yes", fl_flat="yes", fl_sky="no", fl_dark="yes", fl_vardq="no", logfile=log)

    if os.path.exists("ronchifile"):
        if over:
            iraf.delete("ronchifile")
            os.remove("rgn"+ronchiflat+".fits")
            iraf.nfsdist("rgn"+ronchiflat,fwidth=6.0, cradius=8.0, glshift=2.8, minsep=6.5, thresh=2000.0, nlost=3, fl_inter='no',logfile=log)
        else:
            print "\nOutput file exists and -over not set - ",\
            "not performing ronchi calibration with iraf.nfsdist.\n"
    else:
        # Determine the spatial distortion correction. Output: overwrites "rgn"+ronchiflat+".fits" and makes
        # changes to files in /database directory.
        iraf.nfsdist("rgn"+ronchiflat,fwidth=6.0, cradius=8.0, glshift=2.8, minsep=6.5, thresh=2000.0, nlost=3, fl_inter='no',logfile=log)

    # Put the name of the spatially referenced ronchi flat "rgn"+ronchiflat into a
    # text file called ronchifile to be used by the pipeline later. Also associated files
    # are in the "database/" directory.

    open("ronchifile", "w").write("rgn"+ronchiflat)
    # Copy to relevant science observation/calibrations/ directories
    copyCalibration("rgn"+ronchiflat+".fits", 'finalRonchi.fits', grating, over)
    copyCalibrationDatabase("idrgn", grating, over)

#---------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    start()
