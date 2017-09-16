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
from ..nifsUtils import datefmt, listit, writeList, checkLists, makeSkyList, MEFarith, convertRAdec
# Import Nifty python data cube merging script.
from .nifsMerge import mergeCubes

# Define constants
# Paths to Nifty data.
RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

def makeTelluricCorrection(
    telluricDirectory, path, continuuminter, hlineinter, tempInter, hline_method="vega", spectemp="",
    mag="", log="test.log", over=False):
    """FLUX CALIBRATION
    Consists of this start function and six required functions at the end of
    this file.
    """
    """iraf.gemini(_doprint=0, motd="no")
    iraf.gnirs(_doprint=0)
    iraf.imutil(_doprint=0)
    iraf.onedspec(_doprint=0)
    iraf.nsheaders('nifs',Stdout='/dev/null')"""
    # Overview of Telluric Correction procedure:
    # We make a telluric correction by:
    # Remove H-lines from combined 1D standard star spectrum.
    # Divide by H-line corrected standard spectrum by continuum fit.
    # We apply a telluric correction by:
    # Dividing the cube by the correction spectrum (with iraf.telluric) to figure out the shift and scaling.
    # Dividing again by the continuum to add a continuum shape back in.
    # Telluric correction done.


    # Overview of flux calibration procedure:
    # Make a blackbody spectrum.
    # Scale to the observed magnitude of the standard.
    # Multiply telluric corrected target spectrum by this scaled blackbody.
    # Done!
    iraffunctions.chdir(telluricDirectory)

    logging.info('I am starting to create telluric correction spectrum and blackbody spectrum')
    logging.info('I am starting to create telluric correction spectrum and blackbody spectrum ')

    # Open the combine extracted 1d spectrum.
    try:
        combined_extracted_1d_spectra = str(open('telluricfile', 'r').readlines()[0]).strip()
    except:
        logging.info("No telluricfile found in " + str(telluricDirectory) + "Skipping telluric correction and flux calibration.")
        return
    if not os.path.exists('scienceMatchedTellsList'):
        logging.info("No scienceMatchedTellsList found in " + str(telluricDirectory))
        return
    telheader = astropy.io.fits.open(combined_extracted_1d_spectra+'.fits')
    grating = telheader[0].header['GRATING'][0]

    # Get standard star spectral type, teff, and magnitude from the interwebs. Go forth, brave parser!
    getStandardInfo(path, mag, grating, spectemp)

    hLineCorrection(combined_extracted_1d_spectra, grating, path, hlineinter, tempInter, hline_method, log, over)

    # Fit a continuum from the standard star spectrum, saving both continuum and continuum divided standard spectrum.
    fitContinuum(continuuminter, tempInter, grating)
    # Divide the standard star spectrum by the continuum to normalize it.
    if os.path.exists("telluricCorrection.fits"):
        os.remove("telluricCorrection.fits")
    iraf.imarith('final_tel_no_hlines_no_norm', "/", 'fit', result='telluricCorrection',title='',divzero=0.0,hparams='',pixtype='',calctype='',verbose='no',noact='no',mode='al')
    # Done deriving telluric correction! We have two new products:
    # 1) A continuum-normalized telluric correction spectrum, telluricCorrection.fits, and
    # 2) The continuum we used to normalize it, fit.fits.


def hLineCorrection(combined_extracted_1d_spectra, grating, path, hlineinter, tempInter, hline_method, log, over, airmass_std=1.0):
    """
    Remove hydrogen lines from the spectrum of a telluric standard,
    using a model of vega's atmosphere.

    """

    # File for recording shift/scale from calls to "telluric"
    telluric_shift_scale_record = open('telluric_hlines.txt', 'w')

    # Remove H lines from standard star correction spectrum
    no_hline = False
    if os.path.exists("final_tel_no_hlines_no_norm.fits"):
        if over:
            iraf.delete("final_tel_no_hlines_no_norm.fits")
        else:
            no_hline = True
            logging.info("Output file exists and -over- not set - skipping H line removal")

    if hline_method == "vega" and not no_hline:
        vega(combined_extracted_1d_spectra, grating, path, hlineinter, telluric_shift_scale_record, log, over)

    #if hline_method == "linefitAuto" and not no_hline:
    #    linefitAuto(combined_extracted_1d_spectra, grating)

    # Disabled and untested because interactive scripted iraf tasks are broken...
    #if hline_method == "linefitManual" and not no_hline:
    #    linefitManual(combined_extracted_1d_spectra+'[sci,1]', grating)

    #if hline_method == "vega_tweak" and not no_hline:
        #run vega removal automatically first, then give user chance to interact with spectrum as well
    #    vega(combined_extracted_1d_spectra,grating, path, hlineinter, telluric_shift_scale_record, log, over)
    #    linefitManual("final_tel_no_hlines_no_norm", grating)

    #if hline_method == "linefit_tweak" and not no_hline:
        #run Lorentz removal automatically first, then give user chance to interact with spectrum as well
    #    linefitAuto(combined_extracted_1d_spectra,grating)
    #    linefitManual("final_tel_no_hlines_no_norm", grating)

    if hline_method == "none" and not no_hline:
        #need to copy files so have right names for later use
        iraf.imcopy(input=combined_extracted_1d_spectra+'[sci,'+str(1)+']', output="final_tel_no_hlines_no_norm", verbose='no')
    # Plot the non-hline corrected spectrum and the h-line corrected spectrum.
    uncorrected = astropy.io.fits.open(combined_extracted_1d_spectra+'.fits')[1].data
    corrected = astropy.io.fits.open("final_tel_no_hlines_no_norm.fits")[0].data
    if hlineinter or tempInter:
        plt.title('Before and After HLine Correction')
        plt.plot(uncorrected)
        plt.plot(corrected)
        plt.show()

def vega(spectrum, band, path, hlineinter, telluric_shift_scale_record, log, over, airmass=1.0):
    """
    Use iraf.telluric to remove H lines from standard star, then remove
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
        sample = "21537:21778"
        scale = 0.8
    if band=='H':
        ext = '2'
        sample = "16537:17259"
        scale = 0.7
    if band=='J':
        ext = '3'
        sample = "11508:13492"
        scale = 0.885
    if band=='Z':
        ext = '4'
        sample = "*"
        scale = 0.8
    if os.path.exists("tell_nolines.fits"):
            if over:
                os.remove("tell_nolines.fits")
                tell_info = iraf.telluric(input=spectrum+"[1]", output='tell_nolines', cal= RUNTIME_DATA_PATH+'vega_ext.fits['+ext+']', xcorr='yes', tweakrms='yes', airmass=airmass, inter=hlineinter, sample=sample, threshold=0.1, lag=3, shift=0., dshift=0.05, scale=scale, dscale=0.05, offset=0., smooth=1, cursor='', mode='al', Stdout=1)
            else:
                logging.info("Output file exists and -over not set - skipping H line correction")
    else:
        tell_info = iraf.telluric(input=spectrum+"[1]", output='tell_nolines', cal= RUNTIME_DATA_PATH+'vega_ext.fits['+ext+']', xcorr='yes', tweakrms='yes', inter=hlineinter, airmass=airmass, sample=sample, threshold=0.1, lag=3, shift=0., dshift=0.05, scale=scale, dscale=0.05, offset=0., smooth=1, cursor='', mode='al', Stdout=1)

    # need this loop to identify telluric output containing warning about pix outside calibration limits (different formatting)
    if "limits" in tell_info[-1].split()[-1]:
        norm=tell_info[-2].split()[-1]
    else:
        norm=tell_info[-1].split()[-1]

    if os.path.exists("final_tel_no_hlines_no_norm.fits"):
        if over:
            os.remove("final_tel_no_hlines_no_norm.fits")
            iraf.imarith(operand1='tell_nolines', op='/', operand2=norm, result='final_tel_no_hlines_no_norm', title='', divzero=0.0, hparams='', pixtype='', calctype='', verbose='yes', noact='no', mode='al')
        else:
            logging.info("Output file exists and -over not set - skipping H line normalization")
    else:
        iraf.imarith(operand1='tell_nolines', op='/', operand2=norm, result='final_tel_no_hlines_no_norm', title='', divzero=0.0, hparams='', pixtype='', calctype='', verbose='yes', noact='no', mode='al')

# TODO(nat): linefitAuto and linefitManual could be useful at some point.
def linefitAuto(spectrum, band):
    """automatically fit Lorentz profiles to lines defined in existing cur* files
    Go to x position in cursor file and use space bar to find spectrum at each of those points
    """

    specpos = iraf.bplot(images=spectrum+'[SCI,1]', cursor='cur'+band, Stdout=1, StdoutG='/dev/null')
    specpose = str(specpos).split("'x,y,z(x):")
    nextcur = 'nextcur'+band+'.txt'
    # Write line x,y info to file containing Lorentz fitting commands for bplot
    write_line_positions(nextcur, specpos)
    iraf.delete('final_tel_no_hlines_no_norm.fits',ver="no",go_ahead='yes',Stderr='/dev/null')
    # Fit and subtract Lorentz profiles. Might as well write output to file.
    iraf.bplot(images=spectrum+'[sci,1]',cursor='nextcur'+band+'.txt', new_image='final_tel_no_hlines_no_norm', overwrite="yes",StdoutG='/dev/null',Stdout='Lorentz'+band)

def linefitManual(spectrum, band):
    """ Enter splot so the user can fit and subtract lorents (or, actually, any) profiles
    """

    iraf.splot(images=spectrum, new_image='final_tel_no_hlines_no_norm', save_file='../PRODUCTS/lorentz_hlines.txt', overwrite='yes')
    # it's easy to forget to use the 'i' key to actually write out the line-free spectrum, so check that it exists:
    # with the 'tweak' options, the line-free spectrum will already exists, so this lets the user simply 'q' and move on w/o editing (too bad if they edit and forget to hit 'i'...)
    while True:
        try:
            with open("final_tel_no_hlines_no_norm.fits") as f: pass
            break
        except IOError as e:
            logging.info("It looks as if you didn't use the i key to write out the lineless spectrum. We'll have to try again. --> Re-entering splot")
            iraf.splot(images=spectrum, new_image='final_tel_no_hlines_no_norm', save_file='../PRODUCTS/lorentz_hlines.txt', overwrite='yes')

def fitContinuum(continuuminter, tempInter, grating):
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
    if os.path.exists("fit.fits"):
        os.remove("fit.fits")
    iraf.continuum(input='final_tel_no_hlines_no_norm',output='fit',ask='yes',lines='*',bands='1',type="fit",replace='no',wavescale='yes',logscale='no',override='no',listonly='no',logfiles='',inter=continuuminter,sample=sample,naverage=1,func='spline3',order=order,low_rej=1.0,high_rej=3.0,niterate=2,grow=1.0,markrej='yes',graphics='stdgraph',cursor='',mode='ql')
    # Plot the telluric correction spectrum with the continuum fit.
    final_tel_no_hlines_no_norm = astropy.io.fits.open('final_tel_no_hlines_no_norm.fits')[0].data
    fit = astropy.io.fits.open('fit.fits')[0].data
    if continuuminter or tempInter:
        plt.title('Unnormalized Telluric Correction and Continuum fit Used to Normalize')
        plt.plot(final_tel_no_hlines_no_norm)
        plt.plot(fit)
        plt.show()

def divideByContinuum(inputSpectra, divisor, )
