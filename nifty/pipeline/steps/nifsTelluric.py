import glob, shutil, os, logging, glob, urllib, re, traceback, pkg_resources
from pyraf import iraf, iraffunctions
import astropy.io.fits
import numpy as np
import scipy.ndimage.interpolation
import matplotlib.pyplot as plt

# Import config parsing.
from ..configobj.configobj import ConfigObj

# Define constants
# Paths to Nifty data.
RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

def run():
    """
    Do a telluric correction.
    """
    # Store current working directory for later use.
    path = os.getcwd()

    # Set up the logging file.
    log = os.getcwd()+'/Nifty.log'

    logging.info('\n#################################################')
    logging.info('#                                               #')
    logging.info('#       Start the NIFS Telluric Correction      #')
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
        telluricCorrectionConfig = config['telluricCorrectionConfig']
        start = telluricCorrectionConfig['telluricCorrectionStart']
        stop = telluricCorrectionConfig['telluricCorrectionStop']
        hLineMethod = telluricCorrectionConfig['hLineMethod']
        hLineInter = telluricCorrectionConfig['hLineInter']
        continuumInter = telluricCorrectionConfig['continuumInter']
        telluricInter = telluricCorrectionConfig['telluricInter']
        tempInter = telluricCorrectionConfig['tempInter']
        standardStarSpecTemperature = telluricCorrectionConfig['standardStarSpecTemperature']
        standardStarMagnitude = telluricCorrectionConfig['standardStarMagnitude']
        standardStarBand = telluricCorrectionConfig['standardStarBand']
        standardStarRA = telluricCorrectionConfig['standardStarRA']
        standardStarDec = telluricCorrectionConfig['standardStarDec']

    # TESTING IRAF
    iraf.gemini()
    #iraf.gemtools()
    #iraf.gnirs()
    #iraf.nifs()

    #iraf.unlearn(iraf.gemini,iraf.gemtools,iraf.gnirs,iraf.nifs)

    #iraf.set(stdimage='imt2048')
    #iraf.nsheaders("nifs", logfile=log)
    #user_clobber=iraf.envget("clobber")
    #iraf.reset(clobber='yes')


    for scienceDirectory in scienceDirectoryList:
        try:
            os.chdir(scienceDirectory + '/products_telluric_corrected')
        except OSError:
            logging.info("\nWARNING: no products_telluric_corrected/ directory found. Skipping this telluric correction.")
            continue

        scienceFrameList = open("../scienceFrameList", "r").readlines()
        scienceFrameList = [frame.strip() for frame in scienceFrameList]

        # Get standardStarBand from current directory.
        temp = os.path.split(os.getcwd()) # Looks like: ('/Users/nat/tests/core/linearPipelineTest/HD141004/20100401/K/obs107', 'products_telluric_corrected')
        temp2 = os.path.split(temp[0]) # Looks like: ('/Users/nat/tests/core/linearPipelineTest/HD141004/20100401/K', 'obs107')
        temp3 = os.path.split(temp2[0]) # Looks like: ('/Users/nat/tests/core/linearPipelineTest/HD141004/20100401', 'K')
        grating = temp3[1] # Looks like: 'K'

        for rawFrame in scienceFrameList:

            valindex = start
            while valindex <= stop:
                if valindex == 1:
                    getStandardInfo(rawFrame, standardStarMagnitude, standardStarSpecTemperature, standardStarBand, standardStarRA, standardStarDec, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 1 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 2:
                    hLineCorrection(rawFrame, grating, hLineInter, hLineMethod, tempInter, log, over)

                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 2 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 3:
                    fitContinuum(rawFrame, grating, continuumInter, tempInter, log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 3 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 4:
                    divideByContinuum(rawFrame, log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 4 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 5:
                    get1dSpecFromCube(rawFrame, log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 5 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 6:
                    getShiftScale(rawFrame, telluricInter, log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 6 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")
                # Shift and scale the telluric correction spectrum and continuum fit to the telluric correction spectrum.
                if valindex == 7:
                    shiftScaleSpec(rawFrame, "2_fit", "6_shiftedFit", log, over)
                    shiftScaleSpec(rawFrame, "3_chtel", "7_schtel", log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 7 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 8:
                    divideCubebyTel(rawFrame, log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 8 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")

                if valindex == 9:
                    copyToFluxCalDirectory(rawFrame, log, over)
                    logging.info("\n##############################################################################")
                    logging.info("")
                    logging.info("  STEP 9 - COMPLETED ")
                    logging.info("")
                    logging.info("##############################################################################\n")


                valindex += 1

        os.chdir(path)

def getStandardInfo(rawFrame, standardStarMagnitude, standardStarSpecTemperature, standardStarBand, standardStarRA, standardStarDec, log, over):
    """
    Find standard star spectral type, temperature, and standardStarMagnitude, and exposure time. Write results
    to std_starRAWNAME.txt in products_fluxcal_AND_telluric_corrected. Based on XDGNIRS code.

    Executes a SIMBAD query and parses the resulting html to find spectal type,
    temperature and/or standardStarMagnitude.

    Args:
        rawFrame (str): name of raw science frame. Eg: "N20130527S0264"
        standardStarMagnitude (str): standard star standardStarMagnitude provided in config file
        standardStarSpecTemperature (str): standard star effective temperature specified in config file
        standardStarBand (str): spectral standardStarBand of standard star specified in config file
        standardStarRA (str): Right Ascension of standard star specified in config file
        standardStarDec (str): Declination of standard star specified in config file

    Reads:
        0_tel + rawFrame + .fits : Combined, extracted one d standard star spectra

    Writes:
        ../products_fluxcal_AND_telluric_corrected/std_starRAWNAME.txt : Text file storing spectral magnitudes and temperatures of standard star
                                                                  Used later in flux calibration

    """

    starfile = '../products_fluxcal_AND_telluric_corrected/0_std_star'+rawFrame+'.txt'
    kelvinfile = RUNTIME_DATA_PATH+'new_starstemp.txt'

    if os.path.exists(starfile):
        if over:
            pass
        else:
            logging.info("\nOutput exists and -over not set - skipping get standard star info")
            return

    if os.path.exists('../products_fluxcal_AND_telluric_corrected'):
        if over:
            shutil.rmtree('../products_fluxcal_AND_telluric_corrected')
            os.mkdir('../products_fluxcal_AND_telluric_corrected')
        else:
            logging.info("\nOutput exists and -over not set - skipping creation oproducts_fluxcal_AND_telluric_corrected/")
    else:
        os.mkdir('../products_fluxcal_AND_telluric_corrected')

    sf = open(starfile,'w')
    klf = open (kelvinfile)
    Kmag = ''
    Jmag = ''
    Hmag = ''

    # If user didn't specify a standardStarMagnitude, standardStarSpecTemperature, standardStarBand, standardStarRA, or standardStarDec
    # Get standardStarBand, standardStarRA and standardStarDec from the combined extracted standard star spectra headers
    # Use SIMBAD to look up standardStarMagnitude and standardStarSpecTemperature
    if (not standardStarMagnitude or not standardStarSpecTemperature) and (not standardStarBand or not standardStarRA or not standardStarDec):
        telheader = astropy.io.fits.open('0_tel'+rawFrame+'.fits')
        if not standardStarBand:
            standardStarBand = telheader[0].header['GRATING'][0]
        if not standardStarRA:
            standardStarRA = telheader[0].header['RA']
        if not standardStarDec:
            standardStarDec = telheader[0].header['DEC']
        # Make pretty Right Ascensions and Declinations, to pass to SIMBAD.
        if '-' in str(standardStarDec):
            coordinates = str(standardStarRA)+'d'+str(standardStarDec)+'d'
        else:
            coordinates = str(standardStarRA)+'d+'+str(standardStarDec)+'d'
        std_exp_time = telheader[0].header['EXPTIME']
        std_exp_time = str(std_exp_time)
    else:
        # Grab the exposure time anyways
        telheader = astropy.io.fits.open('0_tel'+rawFrame+'.fits')
        std_exp_time = telheader[0].header['EXPTIME']
        std_exp_time = str(std_exp_time)

    # check to see if a spectral type or temperature has been given
    if standardStarSpecTemperature:
        specfind = False
        tempfind = False
        kelvin = standardStarSpecTemperature
    else:
        specfind = True
        tempfind = True

    if standardStarMagnitude:
        magfind = False
        if standardStarBand=='K':
            Kmag=standardStarMagnitude
        if standardStarBand=='H':
            Hmag=standardStarMagnitude
        if standardStarBand=='J':
            Jmag=standardStarMagnitude
    else:
        magfind = True

    if specfind or tempfind or magfind:
        #Construct URL based on standard star coords, execute SIMBAD query to find spectral type
        coordinates = coordinates.replace("+","%2b")
        coordinates = coordinates.replace("-", "%2D")
        start_name='http://simbad.u-strasbg.fr/simbad/sim-coo?Coord='
        end_name = '&submit=submit%20query&Radius.unit=arcsec&Radius=10'
        www_page = start_name+coordinates+end_name
        #f = urllib.urlopen(www_page)
        while True:
            try:
                with urllib.urlopen(www_page) as f:
                    html2 = f.read()
                    break
            except IOError:
                logging.info("\nFailed to open SIMBAD; retrying.")
                pass
        html2 = html2.replace(' ','')
        search_error = str(html2.split('\n'))
        #Exit if the lookup found nothing.
        if 'Noastronomicalobjectfound' in search_error:
            logging.info("ERROR: no object was found at the coordinates you entered. You'll need to supply information in a file; see the manual for instructions.")
        #If >1 object found, decrease search radius and try again
        if 'Numberofrows:' in search_error:
            start_name='http://simbad.u-strasbg.fr/simbad/sim-coo?Coord='
            end_name = '&submit=submit%20query&Radius.unit=arcsec&Radius=1'
            www_page = start_name+coordinates+end_name
            f = urllib.urlopen(www_page)
            html2 = f.read()
            html2 = html2.replace(' ','')
            search_error = str(html2.split('\n'))
        #If that didn't return anything, exit and let the user sort it out
        if 'Noastronomicalobjectfound' in search_error:
            logging.info("ERROR: didn't find a star at your coordinates within a search radius of 10 or 1 arcsec. You'll need to supply information in a file; see the manual for instructions.")
            return
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
            spectral_type = str(html2[numi][0:3])
            if count > 0:
                logging.info("ERROR: problem with SIMBAD output. You'll need to supply the spectral type or temperature in the command line prompt.")
                return
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
                return

    kelvin = str(kelvin)
    # Write results to std_starRAWNAME.txt
    if (Kmag or Jmag or Hmag) and Kmag!='x' and magfind:
        sf.write('k K '+Kmag+' '+kelvin+'\n')
        sf.write('h H '+Hmag+' '+kelvin+'\n')
        sf.write('j J '+Jmag+' '+kelvin+'\n')
        sf.write('j J '+Jmag+' '+kelvin+'\n')
        sf.write('Exp time: '+std_exp_time+'\n')

    elif (Kmag or Jmag or Hmag) and Kmag!='x' and not magfind:
        sf.write('k K '+Kmag+' '+kelvin+'\n')
        sf.write('Exp time: '+std_exp_time+'\n')
    elif Kmag=='x':
        logging.info("WARNING: no magnitudes found for standard star. Doing relative flux calibration only.")
        sf.write('k K N/A '+kelvin+' \n')
        sf.write('h H N/A '+kelvin+' \n')
        sf.write('j J N/A '+kelvin+' \n')
        sf.write('j J N/A '+kelvin+' \n')
        sf.write('Exp time: '+std_exp_time+'\n')
    else:
        logging.info("WARNING: no magnitudes found for standard star. Doing relative flux calibration only.")
        sf.write('k K N/A '+kelvin+' \n')
        sf.write('h H N/A '+kelvin+' \n')
        sf.write('j J N/A '+kelvin+' \n')
        sf.write('j J N/A '+kelvin+' \n')
        sf.write('Exp time: '+std_exp_time+'\n')

    sf.close()
    klf.close()

    with open(starfile,'r') as sf:
        lines = sf.readlines()
    logging.info("\nContents of std_starRAWNAME.txt:")
    for line in lines:
        logging.info(line)


def hLineCorrection(rawFrame, grating, hLineInter, hLineMethod, tempInter, log, over):
    """
    Remove hydrogen lines from the spectrum of a telluric standard,
    using a model of vega's atmosphere.

    Args:

    Returns:

    Reads:
        0_tel + rawFrame + .fits  : Combined, extracted one d standard star spectrum

    Writes:
        1_htel + rawFrame + .fits : Hline corrected standard star spectrum
    """

    # Remove H lines from standard star correction spectrum
    if os.path.exists("1_htel" + rawFrame + ".fits"):
        if over:
            os.remove("1_htel" + rawFrame + ".fits")
            if hLineMethod == "vega":
                vega(rawFrame, grating, hLineInter, log, over)
        else:
            logging.info("Output file exists and -over- not set - skipping H line removal")
    else:
        if hLineMethod == "vega":
            vega(rawFrame, grating, hLineInter, log, over)

    #if hLineMethod == "linefitAuto" and not no_hLine:
    #    linefitAuto(combined_extracted_1d_spectra, grating)

    # Disabled and untested because interactive scripted iraf tasks are broken...
    #if hLineMethod == "linefitManual" and not no_hLine:
    #    linefitManual(combined_extracted_1d_spectra+'[sci,1]', grating)

    #if hLineMethod == "vega_tweak" and not no_hLine:
        #run vega removal automatically first, then give user chance to interact with spectrum as well
    #    vega(combined_extracted_1d_spectra,grating, path, hLineInter, telluric_shift_scale_record, log, over)
    #    linefitManual("final_tel_no_hLines_no_norm", grating)

    #if hLineMethod == "linefit_tweak" and not no_hLine:
        #run Lorentz removal automatically first, then give user chance to interact with spectrum as well
    #    linefitAuto(combined_extracted_1d_spectra,grating)
    #    linefitManual("final_tel_no_hLines_no_norm", grating)

    if tempInter:
        # Plot the non-hLine corrected spectrum and the h-line corrected spectrum.
        uncorrected = astropy.io.fits.open("1_htel" + rawFrame + ".fits")[1].data
        corrected = astropy.io.fits.open("1_htel" + rawFrame + ".fits")[0].data
        plt.title('Before and After HLine Correction')
        plt.plot(uncorrected)
        plt.plot(corrected)
        plt.show()

def fitContinuum(rawFrame, grating, continuumInter, tempInter, log, over):
    """
    Fit a continuum to the telluric correction spectrum to normalize it. The continuum
    fitting regions were derived by eye and can be improved.

    Results are in fit<Grating>.fits
    """
    # These were found to fit the curves well by hand. You can probably improve them; feel free to fiddle around!
    if grating == "K":
        order = 5
        sample = "20279:20395,20953:24283"
    elif grating == "J":
        order = 5
        sample = "11561:12627,12745:12792,12893:13566"
    elif grating == "H":
        order = 5
        sample = "*"
    elif grating == "Z":
        order = 5
        sample = "9453:10015,10106:10893,10993:11553"
    if os.path.exists('2_fit'+rawFrame+'.fits'):
        if over:
            os.remove('2_fit'+rawFrame+'.fits')
            iraf.continuum(input='1_htel'+rawFrame,output='2_fit'+rawFrame,ask='yes',lines='*',bands='1',type="fit",replace='no',wavescale='yes',logscale='no',override='no',listonly='no',logfiles=log,inter=continuumInter,sample=sample,naverage=1,func='spline3',order=order,low_rej=1.0,high_rej=3.0,niterate=2,grow=1.0,markrej='yes',graphics='stdgraph',cursor='',mode='ql')
        else:
            logging.info("\nOutput exists and -over not set - skipping continuum fit to telluric correction")
    else:
        iraf.continuum(input='1_htel'+rawFrame,output='2_fit'+rawFrame,ask='yes',lines='*',bands='1',type="fit",replace='no',wavescale='yes',logscale='no',override='no',listonly='no',logfiles=log,inter=continuumInter,sample=sample,naverage=1,func='spline3',order=order,low_rej=1.0,high_rej=3.0,niterate=2,grow=1.0,markrej='yes',graphics='stdgraph',cursor='',mode='ql')
    if os.path.exists('../products_fluxcal_AND_telluric_corrected/0_fit'+rawFrame+'.fits'):
        if over:
            os.remove('../products_fluxcal_AND_telluric_corrected/0_fit'+rawFrame+'.fits')
            shutil.copy('2_fit'+rawFrame+'.fits', '../products_fluxcal_AND_telluric_corrected/0_fit'+rawFrame+'.fits')
        else:
            logging.info("\nOutput exists and -over not set - skipping copy of fit to products_fluxcal_AND_telluric_corrected")
    else:
        shutil.copy('2_fit'+rawFrame+'.fits', '../products_fluxcal_AND_telluric_corrected/0_fit'+rawFrame+'.fits')

    if tempInter:
        # Plot the telluric correction spectrum with the continuum fit.
        final_tel_no_hLines_no_norm = astropy.io.fits.open('1_htel'+rawFrame+'.fits')[0].data
        fit = astropy.io.fits.open('2_fit'+rawFrame+'fit.fits')[0].data
        plt.title('Unnormalized Telluric Correction and Continuum fit Used to Normalize')
        plt.plot(final_tel_no_hLines_no_norm)
        plt.plot(fit)
        plt.show()

def divideByContinuum(rawFrame, log, over):
    """
    Divide the standard star spectrum by the continuum to normalize it.
    """
    if os.path.exists("3_chtel"+rawFrame+'.fits'):
        if over:
            os.remove("3_chtel"+rawFrame+'.fits')
            # This is related to issue #3
            #iraf.imarith("1_htel"+rawFrame+'.fits', "/", "2_fit"+rawFrame+'.fits', result="3_chtel"+rawFrame+'.fits',title='',divzero=0.0,hparams='',pixtype='',calctype='',verbose='no',noact='no',mode='al')
            operand1 = astropy.io.fits.open("1_htel"+rawFrame+'.fits')[0].data
            operand2 = astropy.io.fits.open("2_fit"+rawFrame+'.fits')[0].data
            header = astropy.io.fits.open("1_htel"+rawFrame+'.fits')[0].header
            multiplied = np.array(operand1, copy=True)
            for i in range(len(multiplied)):
                if operand2[i] != 0:
                    multiplied[i] = operand1[i] / operand2[i]
                else:
                    multiplied[i] = 0.0
            hdu = astropy.io.fits.PrimaryHDU(multiplied)
            hdu.header = header
            hdu.writeto("3_chtel"+rawFrame+".fits")
            logging.info("\nDivided telluric correction by continuum")
        else:
            logging.info("\nOutput exists and -over not set - skipping division by continuum")
    else:
        # This is related to issue #3
        #iraf.imarith('1_htel'+rawFrame+'.fits', "/", '2_fit'+rawFrame+'.fits', result='3_chtel'+rawFrame+'.fits',title='',divzero=0.0,hparams='',pixtype='',calctype='',verbose='no',noact='no',mode='al')
        operand1 = astropy.io.fits.open("1_htel"+rawFrame+'.fits')[0].data
        operand2 = astropy.io.fits.open("2_fit"+rawFrame+'.fits')[0].data
        header = astropy.io.fits.open("1_htel"+rawFrame+'.fits')[0].header
        multiplied = np.array(operand1, copy=True)
        for i in range(len(multiplied)):
            if operand2[i] != 0:
                multiplied[i] = operand1[i] / operand2[i]
            else:
                multiplied[i] = 0.0
        hdu = astropy.io.fits.PrimaryHDU(multiplied)
        hdu.header = header
        hdu.writeto("3_chtel"+rawFrame+".fits")
        logging.info("\nDivided telluric correction by continuum")

def get1dSpecFromCube(rawFrame, log, over):
    """
    Turn a cube into a 1D spec, used to find shift and scale values of telluric spectrum.
    Currently: Extracts 1D spectra from center of cube.
    """
    cube = astropy.io.fits.open('ctfbrsn'+rawFrame+'.fits')
    cubeheader = cube[1].header
    cubeslice = cube[1].data[:,30,30]
    # Create a PrimaryHDU object to encapsulate the data and header.
    hdu = astropy.io.fits.PrimaryHDU(cubeslice)
    # Modify the cd1_1 and CRVAL1 values; this adds the wavelength calibration to the correct cube dimension.
    hdu.header = cubeheader
    hdu.header['CRVAL1'] = cubeheader['CRVAL3']
    hdu.header['CD1_1'] = cubeheader['CD3_3']
    hdu.header['CRPIX1'] = 1.
    if os.path.exists('4_cubeslice'+rawFrame+'.fits'):
        if over:
            os.remove('4_cubeslice'+rawFrame+'.fits')
            # Write the spectrum and header to a new .fits file.
            hdu.writeto('4_cubeslice'+rawFrame+'.fits', output_verify="ignore")
        else:
            logging.info("\nOutput exists and -over not set - skipping extraction of single cube slice")
    else:
        # Write the spectrum and header to a new .fits file.
        hdu.writeto('4_cubeslice'+rawFrame+'.fits', output_verify="ignore")

def getShiftScale(rawFrame, telluricInter, log, over):
    """
    Use iraf.telluric() to get the best shift and scale of a telluric correction spectrum.

    Writes:
        "6_shiftScale"+rawFrame+".txt" :
    """
    if os.path.exists('5_oneDCorrected'+rawFrame+'.fits') and os.path.exists("6_shiftScale"+rawFrame+".txt"):
        if over:
            os.remove('5_oneDCorrected'+rawFrame+'.fits')
            # TODO(nat): implement logging for this
            tell_info = iraf.telluric(input='4_cubeslice'+rawFrame+'.fits[0]',output='5_oneDCorrected'+rawFrame+'.fits',cal="3_chtel"+rawFrame+'.fits[0]',airmass=1.0,answer='yes',ignoreaps='yes',xcorr='yes',tweakrms='yes',inter=telluricInter,sample="*",threshold=0.1,lag=3,shift=0.,dshift=0.1,scale=1.0,dscale=0.1, offset=1,smooth=1,cursor='',mode='al',Stdout=1)
        else:
            logging.info("\nOutput exists and -over not set - skipping get shift scale of telluric correction and fit")
            return
    else:
        tell_info = iraf.telluric(input='4_cubeslice'+rawFrame+'.fits[0]',output='5_oneDCorrected'+rawFrame+'.fits',cal="3_chtel"+rawFrame+'.fits[0]',airmass=1.0,answer='yes',ignoreaps='yes',xcorr='yes',tweakrms='yes',inter=telluricInter,sample="*",threshold=0.1,lag=3,shift=0.,dshift=0.1,scale=1.0,dscale=0.1, offset=1,smooth=1,cursor='',mode='al',Stdout=1)
    # Get shift and scale from the list of values iraf.telluric() returns.
    # Sample tell_info:
    # ['cubeslice.fits[0]: norm.fits[1]: cubeslice.fits[0]: dshift 5.', 'window:again:window:window:again:window:window:again:window:TELLURIC:',
    # '  Output: vtella - HE1353-1917', '  Input: cubeslice.fits[0] - HE1353-1917', '
    # Calibration: norm.fits[1] - Hip70765', '  Tweak: shift = 59.12, scale = 1.323,
    # normalization = 0.9041', '  WARNING: 3 pixels outside of calibration limits']
    tellshift = 0.
    scale = 1.0
    for i in range(len(tell_info)):
        # Now string looks like '  Tweak: shift = 59.12, scale = 1.323, normalization = 0.9041'
        if "Tweak" in tell_info[i]:
            # Remove the first 9 characters,
            temp = tell_info[i][9:]
            # Split into a list; now it looks like '['shift', '=', '59.12,', 'scale', '=', '1.323,', 'normalization', '=', '0.9041']'
            temp = temp.split()
            # Index two is the shift value with a trailing comma, index 5 is the scale value with a trailing comma.
            # Remove trailing comma.
            tellshift = temp[2].replace(',', '')
            # Turn it into a float.
            tellshift = float(tellshift) # Convert to a clean float
            # Do the same for the scale.
            scale = temp[5].replace(',', '')
            scale = float(scale)
    with open("6_shiftScale"+rawFrame+".txt", "w") as text_file:
        text_file.write("Shift: {} Scale: {} \n".format(tellshift, scale))

def shiftScaleSpec(rawFrame, inPrefix, outPrefix, log, over):
    """
    Shifts and scales a spectrum using scipy.
    Replaces overflow with 1.
    """
    spectrum = astropy.io.fits.open(inPrefix+rawFrame+'.fits')
    spectrumData = spectrum[0].data
    try:
        with open("6_shiftScale"+rawFrame+".txt", "r") as f:
            line = f.readlines()
        line = line[0].strip().split()
        tellshift = line[1]
        scale = line[3]
        logging.info("\nRead a shift for "+inPrefix+" spectrum for " + str(tellshift))
        logging.info("\nRead a scale of "+inPrefix+" spectrum for  " + str(scale))
    except IOError:
        logging.info("\nNo shiftScale file found for " + rawFrame + " in " + str(os.getcwd() + ". Skipping."))
        return

    if os.path.exists(outPrefix+rawFrame+'.fits'):
        if over:
            os.remove(outPrefix+rawFrame+'.fits')
            # Shift using SciPy, substituting 1 where data overflows.
            # TODO(nat): doesn't look like interpolation is happening but could be tested more.
            # Works but it's gross. The int(round(float())) is a funny way to turn "-0.02" into 0
            spectrumData = scipy.ndimage.interpolation.shift(spectrumData, -1*int(round(float(tellshift))), cval=1.)
            # Scale by simple multiplication; 1D spectrum times a scalar.
            spectrumData = spectrumData * float(scale)
            spectrum[0].data = spectrumData
            spectrum.writeto(outPrefix+rawFrame+'.fits')
        else:
            logging.info("\nOutput exists and -over not set - skipping shift and scale of " + inPrefix)
    else:
        # Shift using SciPy, substituting 1 where data overflows.
        # TODO(nat): doesn't look like interpolation is happening but could be tested more.
        # Works but it's gross. The int(round(float())) is a funny way to turn "-0.02" into 0
        spectrumData = scipy.ndimage.interpolation.shift(spectrumData, -1*int(round(float(tellshift))), cval=1.)
        # Scale by simple multiplication; 1D spectrum times a scalar.
        spectrumData = spectrumData * float(scale)
        spectrum[0].data = spectrumData
        spectrum.writeto(outPrefix+rawFrame+'.fits')

def divideCubebyTel(rawFrame, log, over):
    """
    Divide every element of a data cube by the derived telluric correction spectrum.
    """
    # Open the uncorrected data cube.
    cube = astropy.io.fits.open('ctfbrsn'+rawFrame+'.fits')
    # Open the shifted, scaled telluric correction spectrum.
    telluricSpec = astropy.io.fits.open('7_schtel'+rawFrame+'.fits')
    if os.path.exists("actfbrsn"+rawFrame+'.fits'):
        if over:
            os.remove("actfbrsn"+rawFrame+'.fits')
            # Divide each slice of cube by telluric correction spectrum.
            for i in range(cube[1].header['NAXIS2']):         # NAXIS2 is the y axis of the final cube.
                for j in range(cube[1].header['NAXIS1']):     # NAXIS1 is the x axis of the final cube.
                    cube[1].data[:,i,j] /= (telluricSpec[0].data)
            # Write the telluric corrected cube to a new file.
            cube.writeto("actfbrsn"+rawFrame+'.fits', output_verify='ignore')
        else:
            logging.info("\nOutput exists and -over not set - skipping application of telluric correction to cube")
    else:
        for i in range(cube[1].header['NAXIS2']):         # NAXIS2 is the y axis of the final cube.
            for j in range(cube[1].header['NAXIS1']):     # NAXIS1 is the x axis of the final cube.
                cube[1].data[:,i,j] /= (telluricSpec[0].data)
        cube.writeto("actfbrsn"+rawFrame+'.fits', output_verify='ignore')

def copyToFluxCalDirectory(rawFrame, log, over):
    """
    Copy finished cubes to products_fluxcal_AND_telluric_corrected directory
    """
    if os.path.exists('../products_fluxcal_AND_telluric_corrected/actfbrsn'+rawFrame+'.fits'):
        if over:
            os.remove('../products_fluxcal_AND_telluric_corrected/actfbrsn'+rawFrame+'.fits')
            shutil.copy('actfbrsn'+rawFrame+'.fits','../products_fluxcal_AND_telluric_corrected/0_telactfbrsn'+rawFrame+'.fits')
        else:
            logging.info("\nOutput exists and -over not set - skipping copy of telluric corrected cube to products_fluxcal_AND_telluric_corrected/")
    else:
            shutil.copy('actfbrsn'+rawFrame+'.fits','../products_fluxcal_AND_telluric_corrected/0_telactfbrsn'+rawFrame+'.fits')

# ---------------------------------------------------------------------------- #

def vega(rawFrame, grating, hLineInter, log, over):
    """
    Use iraf.telluric to remove H lines from standard star, then remove
    normalization added by telluric with iraf.imarith.

    The extension for vega_ext.fits is specified from grating (from header of
    telluricfile.fits).

    Args:


    """
    if grating=='K':
        ext = '1'
        sample = "21537:21778"
        scale = 0.8
    elif grating=='H':
        ext = '2'
        sample = "16537:17259"
        scale = 0.7
    elif grating=='J':
        ext = '3'
        sample = "11508:13492"
        scale = 0.885
    elif grating=='Z':
        ext = '4'
        sample = "*"
        scale = 0.8
    else:
        logging.info("\nWARNING: invalid standard star band. Exiting this correction.")
        return
    if os.path.exists("1_htel" + rawFrame + ".fits"):
            if over:
                os.remove("1_htel" + rawFrame + ".fits")
                tell_info = iraf.telluric(input="0_tel" + rawFrame + ".fits[1]", output="1_htel"+rawFrame, cal= RUNTIME_DATA_PATH+'vega_ext.fits['+ext+']', xcorr='yes', tweakrms='yes', airmass=1.0, inter=hLineInter, sample=sample, threshold=0.1, lag=3, shift=0., dshift=0.05, scale=scale, dscale=0.05, offset=0., smooth=1, cursor='', mode='al', Stdout=1)
            else:
                logging.info("Output file exists and -over not set - skipping H line correction")
                return
    else:
        tell_info = iraf.telluric(input="0_tel" + rawFrame + ".fits[1]", output="1_htel"+rawFrame, cal= RUNTIME_DATA_PATH+'vega_ext.fits['+ext+']', xcorr='yes', tweakrms='yes', airmass=1.0, inter=hLineInter, sample=sample, threshold=0.1, lag=3, shift=0., dshift=0.05, scale=scale, dscale=0.05, offset=0., smooth=1, cursor='', mode='al', Stdout=1)

    # need this loop to identify telluric output containing warning about pix outside calibration limits (different formatting)
    if "limits" in tell_info[-1].split()[-1]:
        norm=tell_info[-2].split()[-1]
    else:
        norm=tell_info[-1].split()[-1]

    if os.path.exists("final_tel_no_hLines_no_norm.fits"):
        if over:
            # Subtle bugs in iraf mean imarith doesn't work. So we use an astropy/numpy solution.
            # Open the image and the scalar we will be dividing it by.
            operand1 = astropy.io.fits.open("1_htel" + rawFrame+'.fits')[0].data
            operand2 = float(norm)
            # Create a new data array
            multiplied = np.array(operand1, copy=True)
            # Don't forget to include the original header! If you don't later IRAF tasks get confused.
            header = astropy.io.fits.open("1_htel" + rawFrame+'.fits')[0].header
            for i in range(len(multiplied)):
                if operand2 != 0:
                    multiplied[i] = operand1[i] / operand2
                else:
                    multiplied[i] = 1
            # Set the data and header of the in-memory image
            hdu = astropy.io.fits.PrimaryHDU(multiplied)
            hdu.header = header
            # Finally, write the new image to a new .fits file. It only has one extension; zero, with a header and data.
            hdu.writeto('final_tel_no_hLines_no_norm.fits')
            #iraf.imarith(operand1="1_htel" + rawFrame, op='/', operand2=norm, result='final_tel_no_hLines_no_norm', title='', divzero=0.0, hparams='', pixtype='', calctype='', verbose='yes', noact='no', mode='al')
        else:
            logging.info("Output file exists and -over not set - skipping H line normalization correction")
    else:
        #iraf.imarith(operand1="1_htel" + rawFrame, op='/', operand2=norm, result='final_tel_no_hLines_no_norm', title='', divzero=0.0, hparams='', pixtype='', calctype='', verbose='yes', noact='no', mode='al')
        operand1 = astropy.io.fits.open("1_htel" + rawFrame+'.fits')[0].data
        operand2 = float(norm)
        multiplied = np.array(operand1, copy=True)
        header = astropy.io.fits.open("1_htel" + rawFrame+'.fits')[0].header
        for i in range(len(multiplied)):
            if operand2 != 0:
                multiplied[i] = operand1[i] / operand2
            else:
                multiplied[i] = 1
        hdu = astropy.io.fits.PrimaryHDU(multiplied)
        hdu.header = header
        hdu.writeto('final_tel_no_hLines_no_norm.fits')

    if os.path.exists('final_tel_no_hLines_no_norm.fits'):
        os.remove("1_htel" + rawFrame + ".fits")
        shutil.move('final_tel_no_hLines_no_norm.fits', "1_htel" + rawFrame + ".fits")

# TODO(nat): linefitAuto and linefitManual could be useful at some point.
def linefitAuto(spectrum, grating):
    """automatically fit Lorentz profiles to lines defined in existing cur* files
    Go to x position in cursor file and use space bar to find spectrum at each of those points
    """

    specpos = iraf.bplot(images=spectrum+'[SCI,1]', cursor='cur'+grating, Stdout=1, StdoutG='/dev/null')
    specpose = str(specpos).split("'x,y,z(x):")
    nextcur = 'nextcur'+grating+'.txt'
    # Write line x,y info to file containing Lorentz fitting commands for bplot
    write_line_positions(nextcur, specpos)
    iraf.delete('final_tel_no_hLines_no_norm.fits',ver="no",go_ahead='yes',Stderr='/dev/null')
    # Fit and subtract Lorentz profiles. Might as well write output to file.
    iraf.bplot(images=spectrum+'[sci,1]',cursor='nextcur'+grating+'.txt', new_image='final_tel_no_hLines_no_norm', overwrite="yes",StdoutG='/dev/null',Stdout='Lorentz'+grating)

def linefitManual(spectrum, grating):
    """ Enter splot so the user can fit and subtract lorents (or, actually, any) profiles
    """

    iraf.splot(images=spectrum, new_image='final_tel_no_hLines_no_norm', save_file='../PRODUCTS/lorentz_hLines.txt', overwrite='yes')
    # it's easy to forget to use the 'i' key to actually write out the line-free spectrum, so check that it exists:
    # with the 'tweak' options, the line-free spectrum will already exists, so this lets the user simply 'q' and move on w/o editing (too bad if they edit and forget to hit 'i'...)
    while True:
        try:
            with open("final_tel_no_hLines_no_norm.fits") as f: pass
            break
        except IOError as e:
            logging.info("It looks as if you didn't use the i key to write out the lineless spectrum. We'll have to try again. --> Re-entering splot")
            iraf.splot(images=spectrum, new_image='final_tel_no_hLines_no_norm', save_file='../PRODUCTS/lorentz_hLines.txt', overwrite='yes')
