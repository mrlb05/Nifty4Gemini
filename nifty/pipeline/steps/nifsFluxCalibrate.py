import os, logging,  pkg_resources
from pyraf import iraf, iraffunctions
import astropy.io.fits
import numpy as np
import matplotlib.pyplot as plt

# Import config parsing.
from ..configobj.configobj import ConfigObj

# Define constants
# Paths to Nifty data.
RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

def run():
    """
    Do a flux calibration.
    """
    # Store current working directory for later use.
    path = os.getcwd()

    # Set up iraf
    iraf.gemini()
    iraf.unlearn("gemini")
    #iraf.unlearn(iraf.gemini,iraf.gemtools,iraf.gnirs,iraf.nifs,iraf.imcopy)

    # Set up the logging file.
    log = os.getcwd()+'/Nifty.log'

    logging.info('\n#################################################')
    logging.info('#                                               #')
    logging.info('#       Start the NIFS Flux Calibration         #')
    logging.info('#                                               #')
    logging.info('#################################################\n')

    # Load reduction parameters from ./config.cfg.
    with open('./config.cfg') as config_file:
        config = ConfigObj(config_file, unrepr=True)
        # Read general pipeline config.
        manualMode = config['manualMode']
        over = config['over']
        scienceDirectoryList = config['scienceDirectoryList']
        # Read baselineCalibrationReduction specfic config.
        fluxCalbrationConfig = config['fluxCalbrationConfig']
        start = fluxCalbrationConfig['fluxCalibrationStart']
        stop = fluxCalbrationConfig['fluxCalibrationStop']

    for scienceDirectory in scienceDirectoryList:
        try:
            os.chdir(scienceDirectory + '/products_fluxcal_AND_telluric_corrected')
        except OSError:
            logging.info("\nWARNING: no products_fluxcal_AND_telluric_corrected/ directory found. Skipping this telluric correction.")
            continue

        scienceFrameList = open("../scienceFrameList", "r").readlines()
        scienceFrameList = [frame.strip() for frame in scienceFrameList]

        # Get grating from current directory.
        temp = os.path.split(os.getcwd()) # Looks like: ('/Users/nat/tests/core/linearPipelineTest/HD141004/20100401/K/obs107', 'products_telluric_corrected')
        temp2 = os.path.split(temp[0]) # Looks like: ('/Users/nat/tests/core/linearPipelineTest/HD141004/20100401/K', 'obs107')
        temp3 = os.path.split(temp2[0]) # Looks like: ('/Users/nat/tests/core/linearPipelineTest/HD141004/20100401', 'K')
        grating = temp3[1] # Looks like: 'K'

        for rawFrame in scienceFrameList:

            valindex = start
            while valindex <= stop:

                if valindex == 1:
                    divideByContinuum(rawFrame, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 1 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 2:
                    makeFLambda(rawFrame, grating, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 2 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 3:
                    makeBlackBody(rawFrame, grating, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 3 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")


                if valindex == 4:
                    makeBlackBodyScale(rawFrame, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 4 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 5:
                    scaleBlackBody(rawFrame, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 5 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 6:
                    multiplyByBlackBody(rawFrame, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 6 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                valindex += 1

        os.chdir(path)

def divideByContinuum(rawFrame, log, over):
    """
    - Multiply each slice of "actfbrsn"+scienceObjectName+".fits"[1].data
      by the fit to the telluric correction.

    """
    # Open the telluric corrected, un-fluxcalibrated data cube.
    cube = astropy.io.fits.open('0_telactfbrsn'+rawFrame+'.fits')
    # Open the scaled blackbody. We will multiply the cube by this.
    shiftedFit = astropy.io.fits.open("0_fit"+rawFrame+".fits")
    if os.path.exists('1_continuum'+rawFrame+'.fits'):
        if over:
            os.remove('1_continuum'+rawFrame+'.fits')
            # Divide each spectrum in the cubedata array by the
            for i in range(cube[1].header['NAXIS2']):         # NAXIS2 is the y axis of the final cube.
                for j in range(cube[1].header['NAXIS1']):     # NAXIS1 is the x axis of the final cube.
                    cube[1].data[:,i,j] /= (shiftedFit[0].data)
            # Write the corrected cube to a new file with new prefix
            cube.writeto('1_continuum'+rawFrame+'.fits', output_verify='ignore')
        else:
            logging.info("\nOutput exists and -over not set - skipping cube division by continuum")
    else:
        # Divide each spectrum in the cubedata array by the
        for i in range(cube[1].header['NAXIS2']):         # NAXIS2 is the y axis of the final cube.
            for j in range(cube[1].header['NAXIS1']):     # NAXIS1 is the x axis of the final cube.
                cube[1].data[:,i,j] /= (shiftedFit[0].data)
        # Write the corrected cube to a new file with new prefix
        cube.writeto('1_continuum'+rawFrame+'.fits', output_verify='ignore')

def makeFLambda(rawFrame, grating, log, over):
    """
    - Multiply magnitude expression by appropriate constant for grating.
    - Multiple by ratio of experiment times.
    - If no magnitude, set fLambda to 1. No absolute flux calibration performed.
    Returns:
        -fLambda: floating point constant.
    """
    # 2MASS doesn't have Z band magnitudes. Use J for rough absolute flux scaling.
    if grating == 'Z':
        grating = 'J'

    # Get standard star magnitude and exposure time
    try:
        with open("0_std_star"+rawFrame+".txt", "r") as f:
            lines = f.read()
        # Split into a list; it should then look something like this:
        # ['k', 'K', '7.615', '9700', 'h', 'H', '7.636', '9700', 'j', 'J', '7.686', '9700', 'j', 'J', '7.686', '9700']
        lines = lines.split()
        # Mag is entry after the grating, but may also be N/A. Check for that.
        for i in range(len(lines)):
            if grating in lines[i] and lines[i+1] != "N/A":
                standardStarMagnitude = lines[i+1]
                logging.info("Found standard star magnitude to be " + str(standardStarMagnitude))
        # Standard exposure time is the last thing in the list
        std_exp_time = lines[-1]
    except IOError:
        logging.info("No std_starRAWNAME.txt file found; no absolute flux cal will be attempted.")

    if grating == "K":
        constant = 4.283E-11
    elif grating == "H":
        constant = 1.33E-10
    elif grating == "J" or "Z":
        constant = 3.129E-10

    # Look up the target exposure time.
    target_header = astropy.io.fits.open('../ctfbrsn'+rawFrame+'.fits')
    tgt_exp_time = target_header[0].header['EXPTIME']

    # Try actually making fLambda!
    try:
        standardStarMagnitude = float(standardStarMagnitude)
        fLambda = (10**((-1*standardStarMagnitude)/2.5)) * constant * (float(std_exp_time) / float(tgt_exp_time))
        logging.info("\nMade fLambda; doing rough absolute flux cal")
    except:
        # If no magnitude set to 1; no absolute flux cal. attempted
        fLambda = 1
        logging.info("\nCouldn't make fLambda; doing relative flux cal")
    if os.path.exists("2_fLambda"+rawFrame+".txt"):
        if over:
            os.remove("2_fLambda"+rawFrame+".txt")
            with open("2_fLambda"+rawFrame+".txt", "w") as f:
                f.write("fLambda: {}".format(fLambda))
            logging.info("\nWrote a value of {} to 2_fLambda{}.txt".format(fLambda, rawFrame))
        else:
            logging.info("\nOutput exists and -over not set - skipping write of fLambda to file")
    else:
        with open("2_fLambda"+rawFrame+".txt", "w") as f:
            f.write("fLambda: {}".format(fLambda))
        logging.info("\nWrote a value of {} to 2_fLambda{}.txt".format(fLambda, rawFrame))

def makeBlackBody(rawFrame, grating, log, over):
    """
    - From Z header information from the cube, make a black body.
    - Make scale factor: mean of black body over fLambda.
    - Multiply blackbody spectrum by scale factor.
    Creates:
        - Unscaled blackbody, bbody.fits
        - A scaled 1D blackbody spectrum, scaledBlackBody.fits[0]
    """
    # Find the start and end wavelengths of the blackbody from our cube header.
    target_header = astropy.io.fits.open('../products_uncorrected/ctfbrsn'+rawFrame+'.fits')
    wstart = target_header[1].header['CRVAL3']
    wdelt = target_header[1].header['CD3_3']
    wend = wstart + (2040 * wdelt)
    crpix3 = target_header[1].header['CRPIX3']
    # Find the standard star temperature from 0_std_starRAWNAME.txt
    try:
        with open("0_std_star"+rawFrame+".txt", "r") as f:
            lines = f.read()
        # ['k', 'K', '7.615', '9700', 'h', 'H', '7.636', '9700', 'j', 'J', '7.686', '9700', 'j', 'J', '7.686', '9700']
        lines = lines.split()
        # Mag is entry after the grating, but may also be N/A. Check for that.
        for i in range(len(lines)):
            if grating in lines[i]:
                standardStarSpecTemperature = lines[i+2]
                logging.info("Read a standard star teff of " + str(standardStarSpecTemperature))
    except IOError:
        logging.info("No std_starRAWNAME.txt file found; setting to spec temperature to 9700K for a rough flux scaling")
        standardStarSpecTemperature = 9700
    if crpix3 != 1.:
        logging.info("WARNING in Reduce: CRPIX of wavelength axis not equal to one. Exiting flux calibration.")
        raise SystemExit
    # Make a blackbody for each of the 2040 NIFS spectral pixels.
    if os.path.exists("3_BBody"+rawFrame+".fits"):
        if over:
            os.remove("3_BBody"+rawFrame+".fits")
            iraf.mk1dspec(input="3_BBody"+rawFrame,output="",title='',ncols=2040,naps=1,header='',wstart=wstart,wend=wend,temperature=standardStarSpecTemperature)
            logging.info("\nMade a blackbody in 3_BBody{}.fits".format(rawFrame))
        else:
            logging.info("\nOutput exists and -over not set - skipping production of unscaled black body")
    else:
        iraf.mk1dspec(input="3_BBody"+rawFrame,output="",title='',ncols=2040,naps=1,header='',wstart=wstart,wend=wend,temperature=standardStarSpecTemperature)
        logging.info("\nMade a blackbody in 3_BBody{}.fits".format(rawFrame))
    mean = iraf.imstat(images="3_BBody"+rawFrame+".fits", fields="mean", lower='INDEF', upper='INDEF', nclip=0, lsigma=3.0, usigma=3.0, binwidth=0.1, format='yes', cache='no', mode='al',Stdout=1)
    print mean

def makeBlackBodyScale(rawFrame, log, over):
    """
    For now, scale the black body by the ratio of the black body mean flux to fLambda.
    """
    # Get the mean of the unscaled blackbody.
    mean = iraf.imstat(images="3_BBody"+rawFrame+".fits", fields="mean", lower='INDEF', upper='INDEF', nclip=0, lsigma=3.0, usigma=3.0, binwidth=0.1, format='yes', cache='no', mode='al',Stdout=1)
    mean = float(mean[1].replace("'",""))

    # Get fLambda.
    with open("2_fLambda"+rawFrame+".txt", "r") as f:
        fLambda = f.read()
    fLambda = float(fLambda.split()[1])

    # Create the scale factor.
    bbodyScaleFactor = fLambda / mean

    # Write it to a file.
    if os.path.exists("4_bbodyScaleFactor"+rawFrame+".txt"):
        if over:
            os.remove("4_bbodyScaleFactor"+rawFrame+".txt")
            logging.info("\nFound a scale factor of {}; writing to 4_bbodyScaleFactor{}.txt".format(bbodyScaleFactor, rawFrame))
            with open("4_bbodyScaleFactor"+rawFrame+".txt", "w") as f:
                f.write("bbodyScaleFactor: {} \n".format(bbodyScaleFactor))
        else:
            logging.info("\nOutput exists and -over not set - skipping writing of 4_bbodyScaleFactor{}.txt".format(rawFrame))
    else:
        logging.info("\nFound a scale factor of {}; writing to 4_bbodyScaleFactor{}.txt".format(bbodyScaleFactor, rawFrame))
        with open("4_bbodyScaleFactor"+rawFrame+".txt", "w") as f:
            f.write("bbodyScaleFactor: {} \n".format(bbodyScaleFactor))

def scaleBlackBody(rawFrame, log, over):
    """
    Scale a black body.
    """
    # Get scale factor from file.
    with open("4_bbodyScaleFactor"+rawFrame+".txt", "r") as f:
        line = f.read()
    bbodyScaleFactor = float(line.split()[1])
    if os.path.exists("5_scaledBBody"+rawFrame+".fits"):
        if over:
            os.remove("5_scaledBBody"+rawFrame+".fits")
            iraf.imarith(operand1="3_BBody"+rawFrame, op="*", operand2=bbodyScaleFactor, result="5_scaledBBody"+rawFrame,title='',divzero=0.0,hparams='',pixtype='',calctype='',verbose='no',noact='no',mode='al')
            logging.info("\nCreated a scaled blackbody, 5_scaledBBody{}.fits".format(rawFrame))
        else:
            logging.info("\nOutput exists and -over not set - skipping production of scaled black body")
    else:
        iraf.imarith(operand1="3_BBody"+rawFrame, op="*", operand2=bbodyScaleFactor, result="5_scaledBBody"+rawFrame,title='',divzero=0.0,hparams='',pixtype='',calctype='',verbose='no',noact='no',mode='al')
        logging.info("\nCreated a scaled blackbody, 5_scaledBBody{}.fits".format(rawFrame))
    # We now have a scaled blackbody, scaledBlackBody.fits

def multiplyByBlackBody(rawFrame, log, over):
    """
    - Multiply each slice of continuum multiplied telluric corrected cube
      by the scaled black body.

    Creates:
        - Flux calibrated cube, "factfbrsn"+scienceObjectName+".fits"
    """
    # Open the telluric corrected, continuum multiplied, un-fluxcalibrated data cube.
    cube = astropy.io.fits.open('1_continuum'+rawFrame+'.fits')
    # Open the scaled blackbody. We will multiply the cube by this.
    scaledBlackBody = astropy.io.fits.open("5_scaledBBody"+rawFrame+".fits")

    if os.path.exists("factfbrsn"+rawFrame+'.fits'):
        if over:
            os.remove('factfbrsn'+rawFrame+'.fits')
            # Divide each spectrum in the cubedata array by the telluric correction spectrum.
            for i in range(cube[1].header['NAXIS2']):         # NAXIS2 is the y axis of the final cube.
                for j in range(cube[1].header['NAXIS1']):     # NAXIS1 is the x axis of the final cube.
                    cube[1].data[:,i,j] *= (scaledBlackBody[0].data)
            # Write the corrected cube to a new file.
            cube.writeto('factfbrsn'+rawFrame+'.fits', output_verify='ignore')
        else:
            logging.info("\nOutput exists and -over not set - skipping division of telluric corrected cube by scaled black body")
    else:
        # Divide each spectrum in the cubedata array by the telluric correction spectrum.
        for i in range(cube[1].header['NAXIS2']):         # NAXIS2 is the y axis of the final cube.
            for j in range(cube[1].header['NAXIS1']):     # NAXIS1 is the x axis of the final cube.
                cube[1].data[:,i,j] *= (scaledBlackBody[0].data)
        # Write the corrected cube to a new file.
        cube.writeto('factfbrsn'+rawFrame+'.fits', output_verify='ignore')
