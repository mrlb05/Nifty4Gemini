# Copyright(c) 2006-2011 Association of Universities for Research in Astronomy, Inc.

procedure nftelluric(inimages,calspec)

# Routine to correct telluric absorption in transformed NIFS images.
#
# Version Dec 21, 2005 - I. Song V1.1
#
# History: 25-MAR-05  PJM      - Creation based on nstelluric.cl.
#          DEC-05  I.Song      - major modification to run with 
#                                the Gemini NIFS package
#          Mar-06  I.Song      - a few bugs fixed and make consistent with nfextract
#          Jul-17  N.Comeau    - Added a non-interactive way
#
# Still to do:
#   - Need to verify the VAR and DQ calculations.  
#   - Need to add a non-interactive way.
#

char inimages    {           prompt="Input NIFS images or list"}
char calspec     {           prompt="Telluric calibration spectrum"}
char outimages   {"",        prompt="Output images"}
char outprefix   {"a",       prompt="Output prefix\n"}

bool fl_inter    {yes,       prompt="Run task interactively?"}
bool fl_xcorr    {yes,       prompt="Cross correlate for shift?"}
bool fl_tweakrms {yes,       prompt="Tweak to minimize RMS?"}
char sample      {"*",       prompt="Sample ranges for fits"}
real threshold   {0.5,       prompt="Threshold for calibration"}
real shift       {0.,        prompt="Initial shift of calibration spectrum [pixels]"}
real scale       {1.,        prompt="Initial scale factor multiplying airmass ratio"}
real dshift      {0.5,       prompt="Initial shift search step"}
real dscale      {0.1,       prompt="Initial scale factor search step"}
int  lag         {20,        prompt="Cross-correln. lag [pixels]\n"}
real xc          {0.,        prompt="X-coordinate for nftelluric"}
real yc          {0.,        prompt="Y-coordinate for nftelluric"}

char database    {"database",prompt="Directory for database files"}
int  dispaxis    {1,         min=1,max=2, prompt="Dispersion axis"}

char logfile     {"",        prompt="Logfile"}
bool verbose     {yes,       prompt="Verbose output?"}
int  status      {0,         prompt="Exit status (0=good)"}
struct *scanfile1{"",        prompt="For internal use only"}
struct *scanfile2{"",        prompt="For internal use only"}

begin

# Define local variables.
int  l_lag, l_dispaxis
real l_threshold, l_shift, l_scale, l_dshift, l_dscale, l_xc, l_yc
char l_inimages, l_calspec, l_outimages, l_outprefix
char l_sample, l_database, l_logfile
char l_sci_ext, l_var_ext, l_dq_ext, l_key_airmass, l_key_dispaxis
bool l_fl_xcorr, l_fl_tweakrms, l_fl_inter, l_verbose

# Define run time variables.
int  ii, inputnum, outnum, junk, ref_dispaxis
int  nfiles, nbad, nversion, version, n
real scaler, shiftr, sciairmass, calairmass, scaleexp
char imagesdel, filesdel, imgi, imgout, tmpimg0, imgin, phu, s_empty
char shifts, scales, badhdr, sci, sciapp, var, varapp, dq, dqapp
char airmass, tmpsci1d, tmpimout, tmpout
char tmpcalshift, tmpcalshiftvar, tmpcalshiftdq, tmpcalfit, tmpcalnorm
char tmpcalscale, tmpcalscalevar, tmpcalscaledq
char tmpinimages, tmpoutimages, tmptwodsci, tmptwodvar
char basissci, basisvar
bool madenewoutput, twod

struct sdate

# Make temporary files.
tmpout       = mktemp("tmp$nfs")

tmpinimages  = mktemp("tmp$nfs")
tmpoutimages = mktemp("tmp$nfs")
filesdel     = tmpinimages//","//tmpoutimages

tmpcalfit    = mktemp("tmp$nfs")
tmpcalnorm   = mktemp("tmp$nfs")

tmpsci1d     = mktemp("tmp$nfs")
tmptwodsci   = mktemp("tmp$nfs")
tmptwodvar   = mktemp("tmp$nfs")

# Set local variable values.
l_inimages    = inimages
l_calspec     = calspec
l_outimages   = outimages
l_outprefix   = outprefix

l_fl_xcorr    = fl_xcorr
l_fl_tweakrms = fl_tweakrms
l_sample      = sample
l_threshold   = threshold
l_lag         = lag
l_shift       = shift
l_scale       = scale
l_dshift      = dshift
l_dscale      = dscale
l_xc          = xc
l_yc          = yc

l_fl_inter    = fl_inter
ref_dispaxis  = dispaxis
l_database    = database

l_logfile     = logfile
l_verbose     = verbose

# Initialize variables.
status        = 0
imagesdel     = ""
filesdel      = ""
madenewoutput = no

l_sci_ext     = nsheaders.sci_ext
l_var_ext     = nsheaders.var_ext
l_dq_ext      = nsheaders.dq_ext
l_key_airmass = nsheaders.key_airmass
l_key_dispaxis= nsheaders.key_dispaxis

# Keep task parameters from changing from the outside.
cache ("gimverify", "gemextn", "keypar", "nfextract", "gemdate")

# Test the logfile.
s_empty=""; print(l_logfile) | scan(s_empty); l_logfile=s_empty
if (l_logfile == "" || stridx(" ",l_logfile) > 0) {
  l_logfile = nifs.logfile
  if (l_logfile == "" || stridx(" ",l_logfile) > 0) {
    l_logfile = "nifs.log"
    print (logfile,l_logfile,nifs.logfile)
    printlog("WARNING - NFTELLURIC: Both nftelluric.logfile and nifs.logfile"//
      "are empty.",l_logfile,l_verbose)
    printlog("                      Using default file nifs.log.",l_logfile,
      l_verbose)
  }
}

# Start logging.
date | scan(sdate)
printlog("-----------------------------------------------------------------"//
  "-----------",l_logfile,l_verbose)
printlog("NFTELLURIC -- "//sdate,l_logfile,l_verbose)
printlog("",l_logfile,l_verbose)

# Logs the relevant parameters:
printlog("Input image or list  = "//l_inimages,l_logfile,l_verbose)
printlog("Calibration spectrum = "//l_calspec,l_logfile,l_verbose)
printlog("Output prefix        = "//l_outprefix,l_logfile,l_verbose)
printlog("",l_logfile,l_verbose)

printlog("sci_ext              = "//l_sci_ext,l_logfile,no)
printlog("var_ext              = "//l_var_ext,l_logfile,no)
printlog("dq_ext               = "//l_dq_ext,l_logfile,no)

# Check database directory.
if ((l_database == "")) {
  junk = fscan (nifs.database, l_database)
  if (l_database == "") {
    l_database = "database"
    printlog("WARNING - NFTELLURIC: Both nftelluric.database and "//
      "nifs.database are",l_logfile,yes)
    printlog("                      empty. Using database.",l_logfile,yes)
  }
}

# Check output image names.
if (l_outimages == "" && l_outprefix == "") {
  printlog("ERROR - NFTELLURIC: Parameters OUTIMAGES and OUTPREFIX are "//
    "both empty.",l_logfile,yes)
  goto crash
}

# Check input image names.
if (l_inimages == "") {
  printlog("ERROR - NFTELLURIC: Parameter INIMAGES is empty.",l_logfile,yes)
  goto crash
}

# Check calibration spectrum name.
if (l_calspec == "") {
  printlog("ERROR - NFTELLURIC: Parameter CALSPEC is empty.",l_logfile,yes)
  goto crash
}

# Check input files exist and have been NFPREPARE'd.
gemextn(l_inimages,check="mef,exists",process="none",index="",extname="",
  extversion="",ikparams="",omit="extension,kernel",replace="",
  outfile=tmpinimages,logfile="",glogpars="",verbose=l_verbose)
if (gemextn.fail_count != 0 || gemextn.count == 0) {
  printlog("ERROR - NFTELLURIC: Invalid input file list.",l_logfile,yes)
  goto crash
}
nfiles = gemextn.count

nbad = 0
scanfile1 = tmpinimages
while (fscan(scanfile1,imgin) != EOF) {
  phu = imgin//"[0]"
  keypar(phu,"PREPARE",silent+)
  if (!keypar.found) {
    printlog("ERROR - NFTELLURIC: Image "//imgin//" has not NFPREPAREd.",
      l_logfile,l_verbose) 
    nbad += 1
  }
}
if (nbad > 0) {
  printlog("ERROR - NFTELLURIC: "//nbad//" image(s) have not been run "//
    "through NFPREPARE",l_logfile,yes)
  goto crash
}

# Check output file list.
gemextn(l_outimages,check="absent",process="none",index="",extname="",
  extversion="",ikparams="",omit="extension,kernel",replace="",
  outfile=tmpoutimages,logfile="",glogpars="",verbose=l_verbose)
if (gemextn.fail_count != 0) {
  printlog ("ERROR - NFTELLURIC: Invalid output file names.",l_logfile,yes)
  goto crash
}
if (gemextn.count == 0) {
  gemextn("%^%"//l_outprefix//"%"//"@"//tmpinimages,check="absent",
    process="none",index="",extname="",extversion="",ikparams="",
    omit="kernel,exten",replace="",outfile=tmpoutimages,logfile="",
    glogpars="",verbose=l_verbose)
  if (gemextn.fail_count != 0 || gemextn.count == 0) {
    printlog("ERROR - NFTELLURIC: Bad or incorrectly formatted output file"//
      "list.",l_logfile,yes) 
    goto crash
  }
}

# Same number of input and output file names.
if (nfiles != gemextn.count) {
  printlog("ERROR - NFTELLURIC: Number of input and output files do not "//
    "match.",l_logfile,yes)
  goto crash
}

# Generate output files.
scanfile1 = tmpinimages
scanfile2 = tmpoutimages
while (fscan(scanfile1,imgin) != EOF) {
  junk = fscan(scanfile2,imgout)
  imcopy(imgin//"[0]",imgout,verbose-)
}
madenewoutput = yes

# Check calibration spectrum.
gemextn(l_calspec,check="exists,mef",process="none",index="",extname="",
  extversion="",ikparams="",omit="extension,kernel",replace="",
  outfile="dev$null",logfile="",glogpars="",verbose=l_verbose)
if (gemextn.count != 1 || gemextn.fail_count != 0) {
  printlog("ERROR - NFTELLURIC: Calibration spectrum "//l_calspec//
    " does not exist.",l_logfile,yes)
  goto crash
}

# Check threshold parameter.
if (isindef(l_threshold) == no && l_threshold > 1) {
  printlog("WARNING - NFTELLURIC: Threshold parameter is larger than "//
    "expected for normalised data (see help).",l_logfile,l_verbose)
}

# Now figure out if the calibration spectrum is 2D or 1D.
keypar (l_calspec//"["//l_sci_ext//"]","i_naxis")
if (keypar.found == no || int(keypar.value) != 1) {
  printlog("ERROR - NFTELLURIC: Input calibration spectrum is not "//
    "1-dimensional.",l_logfile,yes)
  printlog("                    Use NFEXTRACT to extract a 1-D spectrum "//
    "first.",l_logfile,yes)
  goto crash
}

# Check the number of extensions in the calibration spectrum.
gemextn(l_calspec,check="exists,mef",process="expand",index="",extname=l_sci_ext,
  extversion="",ikparams="",omit="extension,kernel",replace="",
  outfile="dev$null",logfile="",glogpars="",verbose=l_verbose)
nversion = gemextn.count
if (nversion == 0) {
  printlog("ERROR - NFTELLURIC: Input calibration spectrum has no science "//
    "data.",l_logfile,yes)
  goto crash
}

# Get the airmass of the calibration spectrum observation.
keypar(l_calspec//"[0]",l_key_airmass,silent+)
if (keypar.found == no) keypar.value = "1.0"
calairmass = real(keypar.value)

# Normalize calibration spectrum.
for(version=1;version<=nversion;version=version+1) {
  if (nversion == 1) {
    sci    = "["//l_sci_ext//"]"
    sciapp = "["//l_sci_ext//",append]"
    var    = "["//l_var_ext//"]"
    varapp = "["//l_var_ext//",append]"
  } else {
    sci    = "["//l_sci_ext//","//version//"]"
    sciapp = "["//l_sci_ext//","//version//",append]"
    var    = "["//l_var_ext//","//version//"]"
    varapp = "["//l_var_ext//","//version//",append]"
  }

  gemhedit (l_calspec//sci, "AIRMASS", calairmass, "", delete-)
  if (version == 1) {
     imcopy(l_calspec//"[0]",tmpcalnorm//"[0,overwrite]",verbose-,>&"dev$null")
  }
  l_dispaxis = ref_dispaxis
  keypar(l_calspec//sci,l_key_dispaxis,silent+)
  if (keypar.found) l_dispaxis = int(keypar.value)
  fit1d(l_calspec//sci,tmpcalfit,type="fit",func="spline1",order=1,naverage=2048,inter-)
  imexpr("(a > 0) ? a/b : 1.0",tmpcalnorm//sciapp,l_calspec//sci,tmpcalfit,outtype="real",verbose-)
  imexpr("(a > 0) ? a/(b*b) : 1.0",tmpcalnorm//varapp,l_calspec//var,tmpcalfit,outtype="real",verbose-)
}

# Run telluric. If dispaxis=1, spectrum runs along rows.
shifts = "0"
scales = "0"
scanfile1 = tmpinimages
scanfile2 = tmpoutimages
while (fscan(scanfile1,imgin) != EOF) {
  junk = fscan(scanfile2,imgout)

  gemextn(imgin,check="exists,mef",process="expand",index="",
    extname=l_sci_ext, extversion="",ikparams="",omit="",replace="",
    outfile="dev$null",logfile="",glogpars="",verbose=l_verbose)
  nversion = gemextn.count

  # Generate temporary images used within this loop.
  delete(tmpsci1d,ver-,>&"dev$null")
  tmpsci1d = mktemp("tmp$nfs")

  # Copy the airmass header keyword to the [SCI] extension.
  keypar(imgin//"[0]",l_key_airmass,silent+)
  if (!keypar.found) keypar.value = "1.0"
  gemhedit (imgin//"["//l_sci_ext//"]", "AIRMASS", real(keypar.value), "",
    delete-)

  if (nversion == 1) {
    sci    = "["//l_sci_ext//"]"
    sciapp = "["//l_sci_ext//",append]"
    var    = "["//l_var_ext//"]"
    varapp = "["//l_var_ext//",append]"
  } else {
    sci    = "["//l_sci_ext//",1]"
    sciapp = "["//l_sci_ext//",1,append]"
    var    = "["//l_var_ext//",1]"
    varapp = "["//l_var_ext//",1,append]"
  }

  # Extract data if necessary.
  # If input is 2d, run nfextract; normalize input for telluric.
  keypar(imgin//sci,"i_naxis",silent+)
  twod = keypar.found && int(keypar.value) == 2
  if (twod) {
    printlog("NFTELLURIC - Calling NFEXTRACT to extract 1D spectrum from Input.",
      l_logfile,l_verbose)
    nfextract(imgin,outspectra=tmpsci1d,outprefix="",fl_inter=l_fl_inter,
      xc=l_xc, yc=l_yc, dispaxis=l_dispaxis, logfile=l_logfile,verbose-)
    if (nfextract.status != 0) {
      printlog("ERROR - NFTELLURIC: Error processing NFEXTRACT.",l_logfile,yes)
      goto crash
    }
    imgi = tmpsci1d
  } else {
    imgi = imgin
  }

  # Generate temporary images used within this loop.
  tmpimg0        = mktemp("tmp$nfs")
  tmpimout       = mktemp("tmp$nfs")
  tmpcalshift    = mktemp("tmp$nfs")
  tmpcalshiftvar = mktemp("tmp$nfs")
  tmpcalshiftdq  = mktemp("tmp$nfs")
  tmpcalscale    = mktemp("tmp$nfs")
  tmpcalscalevar = mktemp("tmp$nfs")
  tmpcalscaledq  = mktemp("tmp$nfs")   # currently not used

  imagesdel = tmpimg0//","//tmpimout//","//tmpcalshift//
    ","//tmpcalshift//","//tmpcalshiftvar//","//tmpcalshiftdq//","//
    tmpcalscale//","//tmpcalscalevar//","//tmpcalscaledq

  sci    = "["//l_sci_ext//"]"
  sciapp = "["//l_sci_ext//",append]"
  var    = "["//l_var_ext//"]"
  varapp = "["//l_var_ext//",append]"
  dq     = "["//l_dq_ext//"]"
  dqapp  = "["//l_dq_ext//",append]"

  if (!imaccess(imgi//sci)) {
    printlog("WARNING - NFTELLURIC: No data for "//imgi//" extension "//
      version//".",l_logfile,yes)
    next
  }

  l_dispaxis = ref_dispaxis
  keypar(imgi//sci,l_key_dispaxis,silent+)
  if (keypar.found) l_dispaxis = int(keypar.value)

  keypar(imgi//sci,l_key_airmass,silent+)
  if (!keypar.found) {
     keypar(imgi//"[0]",l_key_airmass,silent+)
     sciairmass = real(keypar.value)
     gemhedit (imgi//"["//l_sci_ext//"]", "AIRMASS", sciairmass,
         "", delete-)
  } else {
      sciairmass = real(keypar.value)
  }

  # Get shift and scale factors using telluric.
  if (l_fl_inter) {
    printlog("NFTELLURIC - Calling TELLURIC...",l_logfile,l_verbose)
  }
  print("NFTELLURIC - fl_inter = ",l_fl_inter)
  telluric(imgi//sci,tmpimout,tmpcalnorm//sci,ignorea=yes,xcorr=l_fl_xcorr,
    tweakrm=l_fl_tweakrms,inter=l_fl_inter,sample=l_sample,
    threshold=l_threshold,lag=l_lag,shift=l_shift,scale=l_scale,
    dshift=l_dshift,dscale=l_dscale,offset=1.,smooth=1,cursor="",> tmpout)
  match("shift",tmpout,stop-,print_file_n-,metach-) | 
    scan(shifts,shifts,shifts,shifts,scales,scales,scales)
  delete(tmpout, ver-)
  shiftr = real(shifts)
  scaler = real(scales)

  scaleexp = (sciairmass/calairmass)*scaler
  printlog("Calibration spectrum shifted by "//shiftr//" pixels.",
    l_logfile, l_verbose)
  printlog("Airmass ratio = "//(sciairmass/calairmass),l_logfile,l_verbose)
  printlog("Scale factor = "//scaler,l_logfile,l_verbose)

  l_dispaxis = ref_dispaxis
  keypar(imgin//sci,l_key_dispaxis,silent+)
  if (keypar.found) l_dispaxis = int(keypar.value)

  # Need to generate appropriate 2D calibration spectrum?
  if (twod) {
    printlog("NFTELLURIC - Expanding to 2D (please wait).",
      l_logfile,l_verbose)
    imdelete(tmptwodsci,verify-,>&"dev$null")
    imdelete(tmptwodvar,verify-,>&"dev$null")
    tmptwodsci = mktemp("tmp$nfs")
    tmptwodvar = mktemp("tmp$nfs")
    imstack(tmpcalnorm//sci,tmptwodsci)
    imstack(tmpcalnorm//var,tmptwodvar)
    hselect(imgin//sci,"i_naxis"//(3-l_dispaxis),yes) | scan(n)
    blkrep(tmptwodsci,tmptwodsci,1,n)
    blkrep(tmptwodvar,tmptwodvar,1,n)
    if (l_dispaxis == 2) {
      imtranspose(tmptwodsci,tmptwodsci)
      imtranspose(tmptwodvar,tmptwodvar)
    }
    basissci = tmptwodsci
    basisvar = tmptwodvar
  } else {
    basissci = tmpcalnorm//sci
    basisvar = tmpcalnorm//var
  }

  # Shift and scale the calibration spectrum as determined by telluric.
  # In order to shift images by fractional pixels, the image has to be real.
  if (l_dispaxis == 1) {
    imshift(basissci,tmpcalshift,shiftr,0.,shifts_file="",interp="linear",
      boundary="nearest",constant=0.)
    imshift(basisvar,tmpcalshiftvar,shiftr,0.,shifts_file="",interp="linear",
      boundary="nearest",constant=0.)
  } else {
    imshift(basissci,tmpcalshift,0.,shiftr,shifts_file="",interp="linear",
      boundary="nearest",constant=0.)
    imshift(basisvar,tmpcalshiftvar,0.,shiftr,shifts_file="",interp="linear",
      boundary="nearest",constant=0.)
  }
  imexpr("(a > 0) ? a*b : 1.0",tmpcalscale,tmpcalshift,scaler,outtype="real",verbose-)
  imexpr("(a > 0) ? a*b : 1.0",tmpcalscalevar,tmpcalshift,scaler,tmpcalshiftvar,outtype="real",verbose-)

  if (nversion > 1) {
    for(version=1;version<=nversion;version=version+1) {
      sci    = "["//l_sci_ext//","//version//"]"
      sciapp = "["//l_sci_ext//","//version//",append]"
      var    = "["//l_var_ext//","//version//"]"
      varapp = "["//l_var_ext//","//version//",append]"
      dq     = "["//l_dq_ext//","//version//"]"
      dqapp  = "["//l_dq_ext//","//version//",append]"

    # Make the output image.
    imexpr("a/b",imgout//sciapp,imgin//sci,tmpcalscale,outtype="real",verbose-)
    imexpr("(c/(b*b))+(a*a*d/(b*b*b*b))",imgout//varapp,imgin//sci,tmpcalscale,
      imgin//var,tmpcalscalevar,outtype="real",verbose-)
    imcopy(imgin//dq,imgout//dqapp,verbose-)
    }
  }
  imdelete (imagesdel, ver-, >& "dev$null")

  #############################################################################
  # Add header info (needs much more!)
  
  gemhedit (imgout//"[0]", "NFTELCAL", l_calspec, 
    "Calibration file for NFTELLURIC", delete-)
  gemhedit (imgout//"[0]", "NFTELSHF", shiftr,
    "Applied shift (pixels)", delete-)
  gemhedit (imgout//"[0]", "NFTELSCL", scaler,
    "Scale factor for airmass ratio", delete-)
  gemhedit (imgout//"[0]", "NFTELXCO", l_fl_xcorr,
    "Use cross-correlation for shift", delete-)
  gemhedit (imgout//"[0]", "NFTELTWK", l_fl_tweakrms,
    "Tweak to minimize RMS", delete-)
  gemhedit (imgout//"[0]", "NFTELSAM", l_sample,
    "Sample ranges for fits", delete-)
  gemhedit (imgout//"[0]", "NFTELTHR", l_threshold,
    "Threshold for calibration", delete-)
  gemhedit (imgout//"[0]", "NFTELLAG", l_lag,
    "Cross correlation lag (pixels)", delete-)
  gemhedit (imgout//"[0]", "NFTELISH", l_shift,
    "Initial shift (pixels)", delete-)
  gemhedit (imgout//"[0]", "NFTELISC", l_scale,
    "Initial scale factor for airmass ratio", delete-)
  gemhedit (imgout//"[0]", "NFTELDSH", l_dshift,
    "Initial shift search step (pixels)", delete-)
  gemhedit (imgout//"[0]", "NFTELDSC", l_dscale,
    "Initial scale factor search step", delete-)
  
  gemdate ()
  gemhedit (imgout//"[0]", "NFTELLUR", gemdate.outdate,
    "UT Time stamp for NFTELLURIC", delete-)
  gemhedit (imgout//"[0]", "GEM-TLM", gemdate.outdate,
    "UT Last modification with GEMINI", delete-)

}

goto clean

###############################################################################
# Exit with error.
crash:
  status=1
  if (madenewoutput) {
    delete("@"//tmpoutimages,ver-, >& "dev$null")
  }

# Clean up and exit.
clean:
  imdelete(tmpsci1d,ver-, >& "dev$null")
  imdelete(imagesdel,ver-, >& "dev$null")
  delete(filesdel,ver-, >& "dev$null")
  imdelete(tmptwodsci,ver-, >& "dev$null")
  imdelete(tmptwodvar,ver-, >& "dev$null")

  scanfile1 = ""
  scanfile2 = ""

  printlog("",l_logfile,l_verbose)
  if (status == 0) {
    printlog("NFTELLURIC exit status:  good.",l_logfile,l_verbose)
  } else {
    printlog("NFTELLURIC exit status:  error.",l_logfile,l_verbose)
  }
  printlog("-------------------------------------------------------------"//
    "---------------",l_logfile,l_verbose)
  
end
