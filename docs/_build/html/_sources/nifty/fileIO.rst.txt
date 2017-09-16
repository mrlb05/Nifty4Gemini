Example of Nifty File I/O
=========================

This is an example of how the Nifty directory tree appears after each step of the
date reduction. These directory trees were created using a custom **niftree** bash command:

.. code-block:: text

  find . -name .git -prune -o -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'

Add the following line to your ~/.bash_profile to create the **niftree** alias:

.. code-block:: text

  alias niftree="find . -name .git -prune -o -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"

nifsPipeline Data Reduction
-----------------------------

Config file used (slightly out of date but still a useful example):

.. code-block:: text

  # Nifty configuration file.
  #
  # Each section lists parameters required by a pipeline step.

  manualMode = True
  over = False
  merge = True
  scienceDirectoryList = []
  telluricDirectoryList = []
  calibrationDirectoryList = []

  [nifsPipelineConfig]
  sort = True
  calibrationReduction = True
  telluricReduction = True
  scienceReduction = True

  [sortConfig]
  rawPath = '/Users/ncomeau/data/TUTORIAL_HD141004'
  program = ''
  skyThreshold = 2.0
  sortTellurics = True
  date = ''
  copy = ''

  [calibrationReductionConfig]
  baselineCalibrationStart = 1
  baselineCalibrationStop = 4

  [telluricReductionConfig]
  telStart = 1
  telStop = 6
  telluricSkySubtraction = True
  spectemp = ''
  mag = ''
  hline_method = 'vega'
  hlineinter = False
  continuuminter = False

  [scienceReductionConfig]
  sciStart = 1
  sciStop = 6
  scienceSkySubtraction = True
  telluricCorrectionMethod = 'gnirs'
  telinter = False
  fluxCalibrationMethod = 'gnirs'
  use_pq_offsets = True
  im3dtran = True

  # Good luck with your Science!

Starting directory structure:

.. code-block:: text

  .
  |____config.cfg


Command used to launch Nifty:

.. code-block:: text

  runNifty nifsPipeline config.cfg

Directory structure after sorting:

.. code-block:: text

  .
  |____config.cfg
  |____HD141004/                         # Object name, from science header
  | |____20100401/                       # UT date, from science header
  | | |____Calibrations_K/               # Calibrations for a given science observation
  | | | |____arcdarklist                 # Textfile list of lamps-off arc frames
  | | | |____arclist                     # Textfile list of lamps-on arc frames
  | | | |____flatdarklist                # Textfile list of lamps-off flats; same length as flatlist
  | | | |____flatlist                    # Textfile list of lamps-on flats; same length as flatdarklist
  | | | |____N201004*.fits               # Raw Calibration Frames
  | | | |____original_flatdarklist       # Unmodified textfile list of lamps-off flats
  | | | |____original_flatlist           # Unmodified textfile list of lamps-on flats
  | | | |____ronchilist                  # Textfile list of lamps-on ronchi flats
  | | |____K/                            # Grating of science and telluric frames
  | | | |____obs107/                     # Science observation, from science headers
  | | | | |____N201004*.fits             # Raw science frames
  | | | | |____scienceFrameList          # Textfile list of science frames
  | | | | |____skyFrameList              # Textfile list of science sky frames
  | | | |____Tellurics/
  | | | | |____obs109/                   # A single standard star observation directory
  | | | | | |____N201004*.fits           # Raw standard star frames
  | | | | | |____scienceMatchedTellsList # Textfile matching telluric observations with science frames
  | | | | | |____skyFrameList            # Textfile list of standard star sky frames
  | | | | | |____tellist                 # Textfile list of standard star frames
  |____Nifty.log                         # Master log file

Now in nifsBaselineCalibration:

After Step 1: Get Shift, two new files appear.

.. code-block:: text

  .
  |____config.cfg
  |____HD141004/
  | |____20100401/
  | | |____Calibrations_K/
  | | | |____arcdarklist
  | | | |____arclist
  | | | |____flatdarklist
  | | | |____flatlist
  | | | |____N201004*.fits
  | | | |____original_flatdarklist
  | | | |____original_flatlist
  | | | |____ronchilist
  | | | |____shiftfile               # Textfile storing name of the reference shift file
  | | | |____sN20100410S0362.fits    # Reference shift file; a single lamps-on flat run through nfprepare
  |____Nifty.log

After Step 2: Make Flat and bad pixel mask, several new files and intermediate results appear.

.. code-block:: text

  .
  |____config.cfg
  |____HD141004/
  | |____20100401/
  | | |____Calibrations_K/
  | | | |____arcdarklist
  | | | |____arclist
  | | | |____flatdarklist
  | | | |____flatfile                         # Textfile storing name of final flat
  | | | |____flatlist
  | | | |____gnN20100410S0362.fits            # Median-combined with gemcombine() and prepared lamps-on flat
  | | | |____gnN20100410S0368.fits            # Median-combined with gemcombine() and prepared lamps-off flat
  | | | |____N201004*.fits
  | | | |____nN201004*.fits                   # Result of running raw frames through nfprepare()
  | | | |____original_flatdarklist
  | | | |____original_flatlist
  | | | |____rgnN20100410S0362.fits           # Result of running gemcombine() lamps-on flats through nsreduce()
  | | | |____rgnN20100410S0362_flat.fits      # Final rectified flat; result of nsslitfunction()
  | | | |____rgnN20100410S0362_sflat.fits     # Preliminary flat; result of nsflat()
  | | | |____rgnN20100410S0362_sflat_bpm.pl   # Final bad pixel mask; later used in nffixbad()
  | | | |____rgnN20100410S0368.fits           # Result of running gemcombine() lamps-off flats through nsreduce()
  | | | |____rgnN20100410S0368_dark.fits      # Final flat dark frame
  | | | |____ronchilist
  | | | |____sflat_bpmfile                    # Textfile storing name of final bad pixel mask
  | | | |____sflatfile
  | | | |____shiftfile
  | | | |____sN20100410S0362.fits
  |____Nifty.log


  After Step 3: Wavelength Solution, similar files are created as well as a database/ directory containing wavelength solutions for each slice.

  .. code-block:: text

  .
  |____config.cfg
  |____HD141004/
  | |____20100401/
  | | |____Calibrations_K/
  | | | |____arcdarkfile
  | | | |____arcdarklist
  | | | |____arclist
  | | | |____database/                        # Contains textfile results from nswavelength(), nfsdist(), nffitcoords(), nifcube()
  | | | | |____idwrgnN20100401S0137_SCI_*_    # Textfiles containing wavelength solutions for a particular slice
  | | | |____flatdarklist
  | | | |____flatfile
  | | | |____flatlist
  | | | |____gnN20100401S0137.fits            # Median-combined with gemcombine() arc dark frame
  | | | |____gnN20100410S0362.fits
  | | | |____gnN20100410S0368.fits
  | | | |____gnN20100410S0373.fits            # Median-combined with gemcombine() arc frame
  | | | |____N201004*.fits
  | | | |____nN201004*.fits                   # Results of running raw frames through nfprepare()
  | | | |____original_flatdarklist
  | | | |____original_flatlist
  | | | |____rgnN20100401S0137.fits           # Results from nsreduce() of combined arc dark frame
  | | | |____rgnN20100410S0362.fits
  | | | |____rgnN20100410S0362_flat.fits
  | | | |____rgnN20100410S0362_sflat.fits
  | | | |____rgnN20100410S0362_sflat_bpm.pl
  | | | |____rgnN20100410S0368.fits
  | | | |____rgnN20100410S0368_dark.fits
  | | | |____ronchilist
  | | | |____sflat_bpmfile
  | | | |____sflatfile
  | | | |____shiftfile
  | | | |____sN20100410S0362.fits
  | | | |____wrgnN20100401S0137.fits          # Final wavelength calibration frame
  |____Nifty.log

After Step 4: Spatial Distortion, the last step of the calibration reduction, more files are added to the database directory.

.. code-block:: text

  .
  |____config.cfg
  |____HD141004/
  | |____20100401/
  | | |____Calibrations_K/
  | | | |____arcdarkfile
  | | | |____arcdarklist
  | | | |____arclist
  | | | |____database/
  | | | | |____idrgnN20100410S0375_SCI_*_      # Textfiles containing spatial solutions for particular slices
  | | | | |____idwrgnN20100401S0137_SCI_*_
  | | | |____flatdarklist
  | | | |____flatfile
  | | | |____flatlist
  | | | |____gnN20100401S0137.fits
  | | | |____gnN20100410S0362.fits
  | | | |____gnN20100410S0368.fits
  | | | |____gnN20100410S0373.fits
  | | | |____gnN20100410S0375.fits             # Median combined with gemcombine() lamps-on ronchi frame
  | | | |____N201004*.fits
  | | | |____nN20100401S0137.fits              # Results of running raw lamps-on ronchi frames through nfprepare()
  | | | |____original_flatdarklist
  | | | |____original_flatlist
  | | | |____rgnN20100401S0137.fits
  | | | |____rgnN20100410S0362.fits
  | | | |____rgnN20100410S0362_flat.fits
  | | | |____rgnN20100410S0362_sflat.fits
  | | | |____rgnN20100410S0362_sflat_bpm.pl
  | | | |____rgnN20100410S0368.fits
  | | | |____rgnN20100410S0368_dark.fits
  | | | |____rgnN20100410S0375.fits            # Results of running combined lamps-on ronchi frame through nsreduce() AND nfsdist()
  | | | |____ronchifile                        # Text file storing name of final ronchi frame
  | | | |____ronchilist
  | | | |____sflat_bpmfile
  | | | |____sflatfile
  | | | |____shiftfile
  | | | |____sN20100410S0362.fits
  | | | |____wrgnN20100401S0137.fits
  |____Nifty.log

The final directory structure after nifsBaselineCalibration, should look something like. The products used by appropriate
standard star and science observation directories are the "rgn" prefixed final ronchi file, the "wrgn" prefixed final wavelength
solution file, the "database/" directory, the "s" prefixed shiftfile, the "rgn" prefixed and "_flat.fits" suffixed final flat field correction
frame, the "rgn" prefixed and "_sflat_bpm.pl" suffixed final bad pixel mask.

.. code-block:: text

  .
  |____config.cfg
  |____HD141004/                               # OT object name; from science frame .fits headers
  | |____20100401/                             # Date; from science frame .fits headers
  | | |____Calibrations_K/                     # Calibrations directory; All the work in this step happens in one of these
  | | | |____arcdarkfile                       # Text file storing name of final reduced arc dark
  | | | |____arcdarklist                       # Text file storing name of arc dark frames
  | | | |____arclist                           # Text file storing name of arc frames
  | | | |____database/                         # Directory with text file results of nswavelength() and nfsdist()
  | | | | |____idrgnN20100410S0375_SCI_*_      # Textfiles containing spatial solutions for particular slices
  | | | | |____idwrgnN20100401S0137_SCI_*_     # Textfiles containing wavelength solutions for particular slices
  | | | |____flatdarklist                      # Text file storing names of lamps-off flats; pipeline uses this, not original_flatlist
  | | | |____flatfile                          # Text file storing name of final flat field correction frame, corrected for slice to slice variation
  | | | |____flatlist                          # Text file storing names of lamps-on flats; pipeline uses this, not original_flatlist
  | | | |____gnN20100401S0137.fits             # Median combined and prepared arc frame
  | | | |____gnN20100410S0362.fits             # Median combined and prepared lamps-on flat
  | | | |____gnN20100410S0368.fits             # Median combined and prepared lamps-off flat
  | | | |____gnN20100410S0373.fits             # Median combined and prepared arc dark frame
  | | | |____gnN20100410S0375.fits             # Median combined and prepared lamps-on ronchi frame
  | | | |____N201004*.fits                     # Raw calibration frames
  | | | |____nN20100401S0137.fits              # Results of running raw lamps-on ronchi frames through nfprepare()
  | | | |____original_flatdarklist             # Text file list of lamps-off flats, NOT taking P and Q offset zero-points into account
  | | | |____original_flatlist                 # Text file list of lamps-on flats, NOT taking P and Q offset zero-points into account
  | | | |____rgnN20100401S0137.fits            # Final reduced, combined and prepared arc frame
  | | | |____rgnN20100410S0362.fits            # Final reduced, combined and prepared lamps-on flat
  | | | |____rgnN20100410S0362_flat.fits       # Final flat field correction frame, corrected for slice to slice variations with nsslitfunction()
  | | | |____rgnN20100410S0362_sflat.fits      # Preliminary flat field correction frame. Result of nsflat()
  | | | |____rgnN20100410S0362_sflat_bpm.pl    # Final bad pixel mask. Result of nsflat()
  | | | |____rgnN20100410S0368.fits            # Final reduced, combined and prepared lamps-off flat frame
  | | | |____rgnN20100410S0368_dark.fits       # Final flat field correction dark frame; result of nsflat()
  | | | |____rgnN20100410S0375.fits            # Results of running combined lamps-on ronchi frame through nsreduce() AND nfsdist()
  | | | |____ronchifile                        # Text file storing name of final ronchi frame
  | | | |____ronchilist                        # Text file list of lamps-on ronchi flat frames
  | | | |____sflat_bpmfile                     # Text file storing name of final bad pixel mask frame
  | | | |____sflatfile                         # Text file storing name of preliminary flat field correction frame
  | | | |____shiftfile                         # Text file storing name of shift file; used to get consistent shift to the MDF
  | | | |____sN20100410S0362.fits              # Shift file; used to get consistent shift to MDF. Result of nfprepare()
  | | | |____wrgnN20100401S0137.fits           # Final wavelength solution frame. Result of nswavelength()
  |____Nifty.log                               # Logfile; all log files should go here.

nifsReduce of Tellurics
-----------------------

After Step 1: Locate the Spectrum, calibrations are copied over from the appropriate calibrations directory and
each raw frame is run through nfprepare().

.. code-block:: text

  .
  |____config.cfg
  |____HD141004/
  | |____20100401/
  | | |____K/
  | | | |____Tellurics/
  | | | | |____obs109/
  | | | | | |____database/                      # Database from appropriate calibrations directory
  | | | | | | |____idrgnN20100410S0375_SCI_*_   # Spatial distortion database text files
  | | | | | | |____idwrgnN20100401S0137_SCI_*_  # Wavelength solution database text files
  | | | | | |____N201004*.fits
  | | | | | |____nN201004*.fits                 # Results of running each raw frame through nfprepare()
  | | | | | |____rgnN20100410S0375.fits         # Final reduced ronchi flat frame from appropriate calibrations directory
  | | | | | |____scienceMatchedTellsList
  | | | | | |____skyFrameList
  | | | | | |____tellist
  | | | | | |____wrgnN20100401S0137.fits        # Final reduced arc frame from appropriate calibrations directory
  |____Nifty.log

After Step 2: Sky Subtraction, the only files that are written are in standard star observation directories. Each prepared standard star frame
is sky subtracted with gemarith(), and then the sky-subtracted prepared frames are median combined into one frame.

.. code-block:: text

  obs109/
  |____database/
  | |____idrgnN20100410S0375_SCI_*_
  | |____idwrgnN20100401S0137_SCI_*_
  |____gnN20100401S0139.fits           # Single median-combined standard star frame
  |____N201004*.fits
  |____nN201004*.fits
  |____rgnN20100410S0375.fits
  |____scienceMatchedTellsList
  |____skyFrameList
  |____snN201004*.fits                 # Sky subtracted, prepared standard star frames
  |____tellist
  |____wrgnN20100401S0137.fits

After Step 3: Flat fielding and Bad Pixels Correction:

.. code-block:: text

  obs109/
  |____brsnN20100401S0138.fits        # Flat fielded and bad pixels corrected standard frames; results of nffixbad()
  |____database/
  | |____idrgnN20100410S0375_SCI_*_
  | |____idwrgnN20100401S0137_SCI_*_
  |____gnN20100401S0139.fits
  |____N201004*.fits
  |____nN201004*.fits
  |____rgnN20100410S0375.fits
  |____rsnN201004*.fits               # Flat fielded standard frames; results of nsreduce()
  |____scienceMatchedTellsList
  |____skyFrameList
  ____snN201004*.fits
  |____tellist
  |____wrgnN20100401S0137.fits

After Step 4: 2D to 3D transformation and Wavelength Calibration:

.. code-block:: text

  obs109/
  |____brsnN201004*.fits
  |____database/
  | |____fcfbrsnN20100401S0138_SCI_*_lamp   # Textfile result of nffitcoords()
  | |____fcfbrsnN20100401S0138_SCI_*_sdist  # Textfile result of nffitcoords()
  | |____fcfbrsnN20100401S0140_SCI_*_lamp
  | |____fcfbrsnN20100401S0140_SCI_*_sdist
  | |____fcfbrsnN20100401S0142_SCI_*_lamp
  | |____fcfbrsnN20100401S0142_SCI_*_sdist
  | |____fcfbrsnN20100401S0144_SCI_*_lamp
  | |____fcfbrsnN20100401S0144_SCI_*_sdist
  | |____fcfbrsnN20100401S0146_SCI_*_lamp
  | |____fcfbrsnN20100401S0146_SCI_*_sdist
  | |____idrgnN20100410S0375_SCI_*_
  | |____idwrgnN20100401S0137_SCI_*_
  |____fbrsnN201004*.fits                   # Results of nffitcoords()
  |____gnN20100401S0139.fits
  |____N201004*.fits
  |____nN201004*.fits
  |____rgnN20100410S0375.fits
  |____rsnN201004*.fits
  |____scienceMatchedTellsList
  |____skyFrameList
  |____snN201004*.fits
  |____tellist
  |____tfbrsnN20100401S0138.fits            # Results of nftransform()
  |____wrgnN20100401S0137.fits

After Step 5: Extract 1D Spectra and Make Combined Telluric:

.. code-block:: text

  obs109/
  |____brsnN201004*.fits
  |____database/
  | |____fcfbrsnN201004*_SCI_*_lamp
  | |____fcfbrsnN201004*_SCI_*_sdist
  | |____idrgnN20100410S0375_SCI_*_
  | |____idwrgnN20100401S0137_SCI_*_
  |____fbrsnN201004*.fits
  |____gnN20100401S0139.fits
  |____gxtfbrsnN20100401S0138.fits    # Median-combined extracted standard star spectra; result of gemcombine()
  |____N201004*.fits
  |____nN201004*.fits
  |____rgnN20100410S0375.fits
  |____rsnN201004*.fits
  |____scienceMatchedTellsList
  |____skyFrameList
  |____snN201004*.fits
  |____tellist
  |____telluricfile                   # Text file storing name of median-combined extracted standard star spectrum.
  |____tfbrsnN201004*.fits
  |____wrgnN20100401S0137.fits
  |____xtfbrsnN201004*.fits           # Extracted 1D standard star spectra; result of nfextract()

After Step 6: Create Telluric Correction Spectrum, the telluric standard data reduction is complete. The final products of the reduction are
telluricCorrection.fits, the final continuum-normalized telluric correction spectrum, and fit.fits, the continuum used to normalize the final
telluric correction spectrum. These two products are copied to an appropriate science observation directory and used by the 'gnirs' telluric
correction method.

.. code-block:: text

  obs109/
  |____brsnN201004*.fits
  |____database/
  | |____fcfbrsnN201004*_SCI_*_lamp
  | |____fcfbrsnN201004*_SCI_*_sdist
  | |____idrgnN201004*_SCI_*_
  | |____idwrgnN201004*_SCI_*_
  |____fbrsnN201004*.fits
  |____final_tel_no_hlines_no_norm.fits  # Final telluric correction spectrum NOT continuum normalized
  |____fit.fits                          # Continuum used to normalize the final telluric correction spectrum
  |____gnN20100401S0139.fits
  |____gxtfbrsnN20100401S0138.fits
  |____N201004*.fits
  |____nN201004*.fits
  |____rgnN20100410S0375.fits
  |____rsnN201004*.fits
  |____scienceMatchedTellsList
  |____skyFrameList
  |____snN201004*.fits
  |____std_star.txt                      # Text file storing temperature and magnitude of standard star
  |____tell_nolines.fits                 # H-line corrected standard star spectrum
  |____tellist
  |____telluric_hlines.txt               # Text file storing what linefitAuto() and linefitManual did. Empty file for now
  |____telluricCorrection.fits           # Final continuum-normalized telluric correction spectrum
  |____telluricfile
  |____tfbrsnN201004*.fits
  |____wrgnN20100401S0137.fits
  |____xtfbrsnN201004*.fits
  PRODUCTS/

The final telluric observation directory structure after nifsReduce Tellurics:

.. code-block:: text

  obs109/                                # Base standard star observation directory; from .fits headers
  |____brsnN201004*.fits                 # Results of nffixbad()
  |____database/                         # Database directory containing text file results of nswavelength(), nfsdist(), nffitcoords()
  | |____fcfbrsnN201004*_SCI_*_lamp      # Text file result of nffitcoords()
  | |____fcfbrsnN201004*_SCI_*_sdist     # Text file result of nffitcoords()
  | |____idrgnN201004*_SCI_*_            # Text file result of nfsdist()
  | |____idwrgnN201004*_SCI_*_           # Text file result of nswavelength()
  |____fbrsnN201004*.fits                # Results of nffitcoords()
  |____final_tel_no_hlines_no_norm.fits  # Final telluric correction spectrum NOT continuum normalized
  |____fit.fits                          # Continuum used to normalize the final telluric correction spectrum
  |____gnN20100401S0139.fits             # Median combined and prepared sky frame
  |____gxtfbrsnN20100401S0138.fits       # Final median-combined and extracted one D standard star spectrum; result of gemcombine()
  |____N201004*.fits                     # Raw standard star and standard star sky frames
  |____nN201004*.fits                    # Prepared standard star and standard star sky frames; results of nfprepare()
  |____rgnN20100410S0375.fits            # Final ronchi flat frame; copied from appropriate calibration directory. Result of nfsdist()
  |____rsnN201004*.fits                  # Flat fielded, cut, sky subtracted, and prepared standard star frames. Results of nsreduce()
  |____scienceMatchedTellsList           # Textfile used to match this standard star observation directory with certain science frames
  |____skyFrameList                      # Textfile list of standard star sky frames
  |____snN201004*.fits                   # Sky subtracted and prepared standard star frames. Results of gemarith()
  |____std_star.txt                      # Text file storing temperature and magnitude of standard star
  |____tell_nolines.fits                 # H-line corrected standard star spectrum
  |____tellist                           # Text file list of standard star frames
  |____telluric_hlines.txt               # Text file storing what linefitAuto() and linefitManual did. Empty file for now
  |____telluricCorrection.fits           # Final continuum-normalized telluric correction spectrum
  |____telluricfile                      # Text file storing name of final median-combined and extracted one D standard star spectrum
  |____tfbrsnN201004*.fits               # Results of nftransform()
  |____wrgnN20100401S0137.fits           # Final reduced arc frame; copied from appropriate calibrations directory
  |____xtfbrsnN201004*.fits              # One D extracted standard star spectra; results of nfextract()
  PRODUCTS/                              # Products directory; currently not used for anything



nifsReduce Science
------------------

After Step 1: locate the spectrum,

Our perspective is inside the science observation directory as all changes, until step 5, happen there.

.. code-block:: text

  obs107/
  |____database/                       # Database directory and associated text files copied from the appropriate calibrations directory
  | |____idrgnN20100410S0375_SCI_*_
  | |____idwrgnN20100401S0137_SCI_*_
  |____N201004*.fits                   # Raw science and science sky frames
  |____nN201004*.fits                  # Prepared science and sky frames. Results of nfprepare()
  |____original_skyFrameList           # Sky frame list without taking P and Q zero-point offsets into account
  |____rgnN20100410S0375.fits          # Final reduced ronchi flat; copied from appropriate calibrations directory
  |____scienceFrameList                # Text file list of science frames
  |____skyFrameList                    # Text file list of science sky frames. If an original_skyFrameList exists, this is the result of taking P and Q zero-point offsets into account
  |____wrgnN20100401S0137.fits         # Final reduce arc frame; copied from appropriate calibrations directory

After Step 2: Sky Subtraction. This is a bit different than the telluric sky subtraction as we do not subtract a median-combined sky frame from each science frame; we subtract the
sky frame of (hopefully) same exposure time closest in time to the science frame from each science frame.

.. code-block:: text

  obs107
  |____database/
  | |____idrgnN20100410S0375_SCI_*_
  | |____idwrgnN20100401S0137_SCI_*_
  |____N201004*.fits
  |____nN201004*.fits
  |____original_skyFrameList
  |____rgnN20100410S0375.fits
  |____scienceFrameList
  |____skyFrameList
  |____snN201004*.fits                # Sky-subtracted and prepared science frames. Results of gemarith()
  |____wrgnN20100401S0137.fits

After Step 3: Flat Fielding and Bad Pixels Correction:

.. code-block:: text

  obs107/
  |____brsnN201004*.fits          # Bad pixel corrected and flat fielded science frames. Results of nffixbad()
  |____database/
  | |____idrgnN201004*_SCI_*_
  | |____idwrgnN201004*_SCI_*_
  |____N201004*.fits
  |____nN201004*.fits
  |____original_skyFrameList
  |____rgnN20100410S0375.fits
  |____rsnN201004*.fits           # Flat fielded science frames. Results of nsreduce()
  |____scienceFrameList
  |____skyFrameList
  |____snN201004*.fits
  |____wrgnN20100401S0137.fits

After Step 4: 2D to 3D transformation and Wavelength Calibration

.. code-block:: text

  obs107/
  |____brsnN201004*.fits
  |____database/
  | |____fcfbrsnN201004*_SCI_*_lamp     # Text file result of nffitcoords()
  | |____fcfbrsnN201004*_SCI_*_sdist    # Text file result of nffitcoords()
  | |____idrgnN20100410S0375_SCI_*_
  | |____idwrgnN20100401S0137_SCI_*_
  |____fbrsnN20100401S0182.fits         # Results of nffitcoords()
  |____N201004*.fits
  |____nN201004*.fits
  |____original_skyFrameList
  |____rgnN20100410S0375.fits
  |____rsnN201004*.fits
  |____scienceFrameList
  |____skyFrameList
  |____snN201004*.fits
  |____tfbrsnN201004*.fits              # Results of nftransform()
  |____wrgnN20100401S0137.fits

After Step 5: Make Uncorrected, Telluric Corrected and Flux Calibrated Data Cubes and Extracted One D Spectra:

Changes take place in both science observation directories AND objectName/ExtractedOneD/ directories.

In a science observation directory:

.. code-block:: text

  obs107/
  |____actfbrsnN201004*.fits               # Final telluric corrected data cubes
  |____bbodyN201004*.fits                  # Unshifted or scaled blackbody used to flux calibrate cubes
  |____brsnN201004*.fits
  |____combinedOneD                        # Textfile storing name of combined extracted one D standard star spectra
  |____ctfbrsnN201004*.fits                # Final uncorrected data cubes
  |____cubesliceN201004*.fits              # One D extracted spectrum of cube used to get telluric correction shift and scale
  |____database/
  | |____fcfbrsnN201004*_SCI_*_lamp
  | |____fcfbrsnN201004*_SCI_*_sdist
  | |____idrgnN20100410S0375_SCI_*_
  | |____idwrgnN20100401S0137_SCI_*_
  |____factfbrsnN201004*.fits              # Final flux calibrated AND telluric corrected data cubes
  |____fbrsnN201004*.fits
  |____finaltelCorN201004*.fits            # Final shifted and scaled fit to telluric correction
  |____gxtfbrsnN20100401S0182.fits         # One D extracted and combined standard star used to derive the telluric correction used on these cubes
  |____N201004*.fits
  |____nN201004*.fits
  |____oneDcorrectedN201004*.fits          # One D telluric corrected slice of cube; this was used to get the shift and scale of the final correction
  |____original_skyFrameList
  |____rgnN20100410S0375.fits
  |____rsnN201004*.fits
  |____scaledBlackBodyN201004*.fits        # Blackbody scaled by flambda and ratio of experiment times; telluric corrected cube multiplied by this
                                           # to get flux calibrated AND telluric corrected cube.
  |____scienceFrameList
  |____skyFrameList
  |____snN201004*.fits
  |____telCorN201004*.fits                 # UNSHIFTED AND SCALED telluric correction for each science cube
  |____telFitN201004*.fits                 # UNSHIFTED AND SCALED fit to telluric correction for each science cube
  |____tfbrsnN201004*.fits
  |____wrgnN20100401S0137.fits
  |____xtfbrsnN201004*.fits

In the scienceObjectName/ExtractedOneD/ directory:

.. code-block:: text

  ExtractedOneD/
  |____20100401_obs107/               # Science data and observation, from .fits headers of science frames
  | |____xtfbrsnN201004*.fits         # Extracted one D spectra from UNCORRECTED cubes. Results of nfextract()
  |____combined20100401_obs107.fits   # Median-combined, extracted one D spectra. Result of gemcombine()

The final science observation directory and scienceObservationName/ExtractedOneD/ directory should look something like this:

In each science directory:

.. code-block:: text

  obs107/
  |____actfbrsnN201004*.fits               # Final telluric corrected data cubes
  |____bbodyN201004*.fits                  # Unshifted or scaled blackbody used to flux calibrate cubes
  |____brsnN201004*.fits                   # Bad pixel corrected, reduced, sky subtracted and prepared science frames
  |____combinedOneD                        # Textfile storing name of combined extracted one D standard star spectra
  |____ctfbrsnN201004*.fits                # Final uncorrected data cubes
  |____cubesliceN201004*.fits              # One D extracted spectrum of cube used to get telluric correction shift and scale
  |____database/
  | |____fcfbrsnN201004*_SCI_*_lamp        # Text file results of nffitcoords()
  | |____fcfbrsnN201004*_SCI_*_sdist       # Text file results of nffitcoords()
  | |____idrgnN20100410S0375_SCI_*_        # Text file results of nfsdist()
  | |____idwrgnN20100401S0137_SCI_*_       # Text file results of nswavelength()
  |____factfbrsnN201004*.fits              # Final flux calibrated AND telluric corrected data cubes
  |____fbrsnN201004*.fits                  # Results of nffitcoords()
  |____finaltelCorN201004*.fits            # Final shifted and scaled fit to telluric correction
  |____gxtfbrsnN20100401S0182.fits         # Median-combined and extracted one D spectra from UNCORRECTED cubes. Results of gemcombine()
  |____N201004*.fits                       # Raw science and science sky frames
  |____nN201004*.fits                      # Prepared raw science frames. Results of nfprepare()
  |____oneDcorrectedN201004*.fits          # One D telluric corrected slice of cube; this was used to get the shift and scale of the final correction
  |____original_skyFrameList               # Text file storing names of science sky frames, not taking P and Q offset zero points into account
  |____rgnN20100410S0375.fits              # Final reduced, combined and prepared ronchi flat frame. Result of nfsdist()
  |____rsnN201004*.fits                    # Flat fielded, sky subtracted and prepared science frames. Result of nsreduce()
  |____scaledBlackBodyN201004*.fits        # Blackbody scaled by flambda and ratio of experiment times; telluric corrected cube multiplied by this
                                           # to get flux calibrated AND telluric corrected cube.
  |____scienceFrameList                    # Text file storing names of science frames
  |____skyFrameList                        # Text file storing names of science sky frames; pipeline uses this and not original_skyFrameList
  |____snN201004*.fits                     # Sky subtracted, prepared raw science frames. Results of gemarith()
  |____telCorN201004*.fits                 # UNSHIFTED AND SCALED telluric correction for each science cube
  |____telFitN201004*.fits                 # UNSHIFTED AND SCALED fit to telluric correction for each science cube
  |____tfbrsnN201004*.fits                 # Results of nftransform()
  |____wrgnN20100401S0137.fits             # Final reduced wavelength solution frame. Result of nswavelength()
  |____xtfbrsnN201004*.fits                # Extracted one D spectra from each UNCORRECTED science cube. Result of nfextract()

In the scienceObjectName/ExtractedOneD/ directory:

.. code-block:: text

  ExtractedOneD/
  |____20100401_obs107/               # Science data and observation, from .fits headers of science frames
  | |____xtfbrsnN201004*.fits         # Extracted one D spectra from UNCORRECTED cubes. Results of nfextract()
  |____combined20100401_obs107.fits   # Median-combined, extracted one D spectra. Result of gemcombine()

nifsMerge
---------

nifsMerge.py is called as the last step of nifsReduce Science to merge data cubes. It produces three cube merging directories:
an UNCORRECTED, a telluric corrected, and a telluric corrected AND flux calibrated directory.
Here are two examples of the structure:

First, from the test data we have been using (HD141004) the final merged directory structure should look something like:

.. code-block:: text

  .
  |____config.cfg
  |____HD141004/
  | |____20100401/
  | | |____Calibrations_K/
  | | |____K/
  | | | |____obs107/
  | |____ExtractedOneD/

  | |____Merged_telCorAndFluxCalibrated/   # Merging directory for final telluric corrected AND flux calibrated data cubes
  | | |____20100401_obs107/
  | | | |____cube_merged.fits
  | | | |____factfbrsnN201004*.fits        # Unmodified, final telluric corrected AND flux calibrated data cubes. Copied from appropriate science observation directory
  | | | |____offsets.txt                   # Offsets provided to imcombine(); see manual for details
  | | | |____out.fits
  | | | |____transcube*.fits               # Transposed data cubes. Results of im3dtran()
  | | |____20100401_obs107_merged.fits     # Final merged cube for obs107

  | |____Merged_telluricCorrected/         # Merging directory for telluric corrected data cubes
  | | |____20100401_obs107/
  | | | |____actfbrsnN201004*.fits         # Unmodified, final telluric corrected data cubes. Copied from appropriate science observation directory
  | | | |____cube_merged.fits
  | | | |____offsets.txt
  | | | |____out.fits                      # Offsets provided to imcombine(); see manual for details
  | | | |____transcube*.fits               # Transposed data cubes. Results of im3dtran()
  | | |____20100401_obs107_merged.fits     # Final merged cube for obs107

  | |____Merged_uncorrected/               # Merging directory for UNCORRECTED data cubes
  | | |____20100401_obs107/
  | | | |____ctfbrsnN201004*.fits          # Unmodified, final UNCORRECTED data cubes. Copied from appropriate science observation directory
  | | | |____cube_merged.fits
  | | | |____offsets.txt                   # Offsets provided to imcombine(); see manual for details
  | | | |____out.fits
  | | | |____transcube*.fits               # Transposed data cubes. Results of im3dtran()
  | | |____20100401_obs107_merged.fits     # Final merged cube for obs107

  |____Nifty.log


.. placeholder
