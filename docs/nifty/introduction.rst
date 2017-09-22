Introduction
============

Nifty, for now, uses Python 2.7. Please keep this in mind.

Running from the Command Line
=============================

Nifty is started with the runNifty command by specifying a pipeline or step with arguments and options.

The syntax used to start Nifty is:

.. code-block:: text

 runNifty <Pipeline or Step Name> <arguments>

To get help or list the available options, type the runNifty command without any arguments.

.. code-block:: text

  runNifty

Running from Python
===================

Python Programmers: even though Nifty's API has not been defined yet, you can still run Nifty Pipelines, Steps, Routines and Tasks from a Python interpeter
by importing them.

For example, to run a final cube merge from the Python interpreter:

.. code-block:: python

  # Import relevant modules; you can find those at top of nifsMerge.py
  from pyraf import iraf, iraffunctions
  # Import relevant local script
  import nifty.pipeline.steps.nifsMerge

  # Set up iraf
  iraf.gemini()
  iraf.gemtools()
  iraf.gnirs()
  iraf.nifs()

  # Define routine parameters
  scienceDirectoryList = []
  cubeType = "uncorrected"
  mergeType = "sum"
  use_pq_offsets = True
  im3dtran = True
  over = False

  # Start the cube merging
  nifty.pipeline.steps.nifsMerge.mergeCubes(scienceDirectoryList, cubeType, mergeType, use_pq_offsets, im3dtran, over="")

You might be able to figure out what imports you need by checking the tops of the relevant scripts.

Examples of Running from the Command Line
-----------------------------------------

Starting a Data Reduction from the Beginning


Supply the -i flag to start the NIFS pipeline, populating a configuration file interactively:

.. code-block:: text

 runNifty nifsPipeline -i

Supply a config.cfg file to start the NIFS pipeline from a pre-built configuration file:

.. code-block:: text

 runNifty nifsPipeline config.cfg

Supply the -f flat to do a fully automatic data reduction, downloading raw data from the Gemini Public Archive (Eg: GN-2013A-Q-62):

.. code-block:: text

  runNifty nifsPipeline -f GN-2013A-Q-62

Supply the -f flag to do a fully automatic data reduction, using raw data from a local directory (Eg: /Users/ncomeau/data/TUTORIAL):

.. code-block:: text

 runNifty nifsPipeline -f /Users/ncomeau/data/TUTORIAL

Starting a Data Reduction from a Specified Point


You can run each step, one at a time, from the command line like so. *You need a config.cfg file in your current working directory to run individual steps.
Each step requires the general config section and its unique config section to be populated*.

You can also run an individual step by turning them on or off in nifsPipeline config and running the nifsPipeline.

**nifsSort:** To only copy and sort NIFS raw data use a config.cfg file like this:

.. code-block:: text

  # Nifty configuration file.
  #
  # Each section lists parameters required by a pipeline step.

  manualMode = False
  over = False
  extractionXC = 15.0
  extractionYC = 33.0
  extractionRadius = 2.5
  scienceOneDExtraction = True
  scienceDirectoryList = []
  telluricDirectoryList = []
  calibrationDirectoryList = []

  [nifsPipelineConfig]
  sort = True
  calibrationReduction = False
  telluricReduction = False
  scienceReduction = False
  telluricCorrection = False
  fluxCalibration = False
  merge = False
  telluricCorrectionMethod = 'gnirs'
  fluxCalibrationMethod = 'gnirs'
  mergeMethod = ''

  [sortConfig]
  rawPath = '/Users/nat/data/TUTORIAL'
  program = ''
  proprietaryCookie = ''
  skyThreshold = 2.0
  sortTellurics = True
  telluricTimeThreshold = 5400

  [calibrationReductionConfig]
  baselineCalibrationStart = 1
  baselineCalibrationStop = 4

  [telluricReductionConfig]
  telStart = 1
  telStop = 5
  telluricSkySubtraction = True

  [telluricCorrectionConfig]
  telluricCorrectionStart = 1
  telluricCorrectionStop = 9
  hLineMethod = 'vega'
  hLineInter = False
  continuumInter = False
  telluricInter = False
  tempInter = False
  standardStarSpecTemperature = ''
  standardStarMagnitude = ''
  standardStarRA = ''
  standardStarDec = ''
  standardStarBand = ''

  [fluxCalbrationConfig]
  fluxCalibrationStart = 1
  fluxCalibrationStop = 6

  [mergeConfig]
  mergeStart = 1
  mergeStop = 3
  mergeType = 'median'
  use_pq_offsets = True
  im3dtran = True

  # Good luck with your Science!

And run the nifsPipeline with:

.. code-block:: text

 runNifty nifsPipeline config.cfg

**nifsBaselineCalibration:** To only reduce calibrations use a config.cfg file like this:

.. code-block:: text

  # Nifty configuration file.
  #
  # Each section lists parameters required by a pipeline step.

  manualMode = False
  over = False
  extractionXC = 15.0
  extractionYC = 33.0
  extractionRadius = 2.5
  scienceOneDExtraction = True
  scienceDirectoryList = []
  telluricDirectoryList = []
  calibrationDirectoryList = []

  [nifsPipelineConfig]
  sort = False
  calibrationReduction = True
  telluricReduction = False
  scienceReduction = False
  telluricCorrection = False
  fluxCalibration = False
  merge = False
  telluricCorrectionMethod = 'gnirs'
  fluxCalibrationMethod = 'gnirs'
  mergeMethod = ''

  [sortConfig]
  rawPath = '/Users/nat/data/TUTORIAL'
  program = ''
  proprietaryCookie = ''
  skyThreshold = 2.0
  sortTellurics = True
  telluricTimeThreshold = 5400

  [calibrationReductionConfig]
  baselineCalibrationStart = 1
  baselineCalibrationStop = 4

  [telluricReductionConfig]
  telStart = 1
  telStop = 5
  telluricSkySubtraction = True

  [telluricCorrectionConfig]
  telluricCorrectionStart = 1
  telluricCorrectionStop = 9
  hLineMethod = 'vega'
  hLineInter = False
  continuumInter = False
  telluricInter = False
  tempInter = False
  standardStarSpecTemperature = ''
  standardStarMagnitude = ''
  standardStarRA = ''
  standardStarDec = ''
  standardStarBand = ''

  [fluxCalbrationConfig]
  fluxCalibrationStart = 1
  fluxCalibrationStop = 6

  [mergeConfig]
  mergeStart = 1
  mergeStop = 3
  mergeType = 'median'
  use_pq_offsets = True
  im3dtran = True

  # Good luck with your Science!

And run the nifsPipeline with:

.. code-block:: text

 runNifty nifsPipeline config.cfg

**nifsReduce Telluric:** To only reduce telluric data use a config.cfg file like this:
*Make sure to populate scienceDirectoryList, telluricDirectoryList and calibrationDirectoryList before running!*

.. code-block:: text

  # Nifty configuration file.
  #
  # Each section lists parameters required by a pipeline step.

  manualMode = False
  over = False
  extractionXC = 15.0
  extractionYC = 33.0
  extractionRadius = 2.5
  scienceOneDExtraction = True
  scienceDirectoryList = []
  telluricDirectoryList = []
  calibrationDirectoryList = []

  [nifsPipelineConfig]
  sort = False
  calibrationReduction = False
  telluricReduction = True
  scienceReduction = False
  telluricCorrection = False
  fluxCalibration = False
  merge = False
  telluricCorrectionMethod = 'gnirs'
  fluxCalibrationMethod = 'gnirs'
  mergeMethod = ''

  [sortConfig]
  rawPath = '/Users/nat/data/TUTORIAL'
  program = ''
  proprietaryCookie = ''
  skyThreshold = 2.0
  sortTellurics = True
  telluricTimeThreshold = 5400

  [calibrationReductionConfig]
  baselineCalibrationStart = 1
  baselineCalibrationStop = 4

  [telluricReductionConfig]
  telStart = 1
  telStop = 5
  telluricSkySubtraction = True

  [telluricCorrectionConfig]
  telluricCorrectionStart = 1
  telluricCorrectionStop = 9
  hLineMethod = 'vega'
  hLineInter = False
  continuumInter = False
  telluricInter = False
  tempInter = False
  standardStarSpecTemperature = ''
  standardStarMagnitude = ''
  standardStarRA = ''
  standardStarDec = ''
  standardStarBand = ''

  [fluxCalbrationConfig]
  fluxCalibrationStart = 1
  fluxCalibrationStop = 6

  [mergeConfig]
  mergeStart = 1
  mergeStop = 3
  mergeType = 'median'
  use_pq_offsets = True
  im3dtran = True

  # Good luck with your Science!

And run the nifsPipeline with:

.. code-block:: text

 runNifty nifsPipeline config.cfg

**nifsReduce Science:** To only reduce science data use a config.cfg file like this:
*Make sure to populate scienceDirectoryList, telluricDirectoryList and calibrationDirectoryList before running!*

.. code-block:: text

  # Nifty configuration file.
  #
  # Each section lists parameters required by a pipeline step.

  manualMode = False
  over = False
  extractionXC = 15.0
  extractionYC = 33.0
  extractionRadius = 2.5
  scienceOneDExtraction = True
  scienceDirectoryList = []
  telluricDirectoryList = []
  calibrationDirectoryList = []

  [nifsPipelineConfig]
  sort = False
  calibrationReduction = False
  telluricReduction = False
  scienceReduction = True
  telluricCorrection = False
  fluxCalibration = False
  merge = False
  telluricCorrectionMethod = 'gnirs'
  fluxCalibrationMethod = 'gnirs'
  mergeMethod = ''

  [sortConfig]
  rawPath = '/Users/nat/data/TUTORIAL'
  program = ''
  proprietaryCookie = ''
  skyThreshold = 2.0
  sortTellurics = True
  telluricTimeThreshold = 5400

  [calibrationReductionConfig]
  baselineCalibrationStart = 1
  baselineCalibrationStop = 4

  [telluricReductionConfig]
  telStart = 1
  telStop = 5
  telluricSkySubtraction = True

  [telluricCorrectionConfig]
  telluricCorrectionStart = 1
  telluricCorrectionStop = 9
  hLineMethod = 'vega'
  hLineInter = False
  continuumInter = False
  telluricInter = False
  tempInter = False
  standardStarSpecTemperature = ''
  standardStarMagnitude = ''
  standardStarRA = ''
  standardStarDec = ''
  standardStarBand = ''

  [fluxCalbrationConfig]
  fluxCalibrationStart = 1
  fluxCalibrationStop = 6

  [mergeConfig]
  mergeStart = 1
  mergeStop = 3
  mergeType = 'median'
  use_pq_offsets = True
  im3dtran = True

  # Good luck with your Science!

And run the nifsPipeline with:

.. code-block:: text

 runNifty nifsPipeline config.cfg

**nifsTelluric Correction:** To only derive and apply a telluric correction use a config.cfg file like this:
*Make sure to populate scienceDirectoryList, telluricDirectoryList and calibrationDirectoryList before running!*

.. code-block:: text

  # Nifty configuration file.
  #
  # Each section lists parameters required by a pipeline step.

  manualMode = False
  over = False
  extractionXC = 15.0
  extractionYC = 33.0
  extractionRadius = 2.5
  scienceOneDExtraction = True
  scienceDirectoryList = []
  telluricDirectoryList = []
  calibrationDirectoryList = []

  [nifsPipelineConfig]
  sort = False
  calibrationReduction = False
  telluricReduction = False
  scienceReduction = False
  telluricCorrection = True
  fluxCalibration = False
  merge = False
  telluricCorrectionMethod = 'gnirs'
  fluxCalibrationMethod = 'gnirs'
  mergeMethod = ''

  [sortConfig]
  rawPath = '/Users/nat/data/TUTORIAL'
  program = ''
  proprietaryCookie = ''
  skyThreshold = 2.0
  sortTellurics = True
  telluricTimeThreshold = 5400

  [calibrationReductionConfig]
  baselineCalibrationStart = 1
  baselineCalibrationStop = 4

  [telluricReductionConfig]
  telStart = 1
  telStop = 5
  telluricSkySubtraction = True

  [telluricCorrectionConfig]
  telluricCorrectionStart = 1
  telluricCorrectionStop = 9
  hLineMethod = 'vega'
  hLineInter = False
  continuumInter = False
  telluricInter = False
  tempInter = False
  standardStarSpecTemperature = ''
  standardStarMagnitude = ''
  standardStarRA = ''
  standardStarDec = ''
  standardStarBand = ''

  [fluxCalbrationConfig]
  fluxCalibrationStart = 1
  fluxCalibrationStop = 6

  [mergeConfig]
  mergeStart = 1
  mergeStop = 3
  mergeType = 'median'
  use_pq_offsets = True
  im3dtran = True

  # Good luck with your Science!

And run the nifsPipeline with:

.. code-block:: text

 runNifty nifsPipeline config.cfg

**nifsFluxCalibration:** To only do a flux calibration use a config.cfg file like this:
*Make sure to populate scienceDirectoryList, telluricDirectoryList and calibrationDirectoryList before running!*

.. code-block:: text

  # Nifty configuration file.
  #
  # Each section lists parameters required by a pipeline step.

  manualMode = False
  over = False
  extractionXC = 15.0
  extractionYC = 33.0
  extractionRadius = 2.5
  scienceOneDExtraction = True
  scienceDirectoryList = []
  telluricDirectoryList = []
  calibrationDirectoryList = []

  [nifsPipelineConfig]
  sort = False
  calibrationReduction = False
  telluricReduction = False
  scienceReduction = False
  telluricCorrection = False
  fluxCalibration = True
  merge = False
  telluricCorrectionMethod = 'gnirs'
  fluxCalibrationMethod = 'gnirs'
  mergeMethod = ''

  [sortConfig]
  rawPath = '/Users/nat/data/TUTORIAL'
  program = ''
  proprietaryCookie = ''
  skyThreshold = 2.0
  sortTellurics = True
  telluricTimeThreshold = 5400

  [calibrationReductionConfig]
  baselineCalibrationStart = 1
  baselineCalibrationStop = 4

  [telluricReductionConfig]
  telStart = 1
  telStop = 5
  telluricSkySubtraction = True

  [telluricCorrectionConfig]
  telluricCorrectionStart = 1
  telluricCorrectionStop = 9
  hLineMethod = 'vega'
  hLineInter = False
  continuumInter = False
  telluricInter = False
  tempInter = False
  standardStarSpecTemperature = ''
  standardStarMagnitude = ''
  standardStarRA = ''
  standardStarDec = ''
  standardStarBand = ''

  [fluxCalbrationConfig]
  fluxCalibrationStart = 1
  fluxCalibrationStop = 6

  [mergeConfig]
  mergeStart = 1
  mergeStop = 3
  mergeType = 'median'
  use_pq_offsets = True
  im3dtran = True

  # Good luck with your Science!

And run the nifsPipeline with:

.. code-block:: text

 runNifty nifsPipeline config.cfg

**nifsMerge Cube Merging:** To only merge final data cubes use a config.cfg file like this:
*Make sure to populate scienceDirectoryList, telluricDirectoryList and calibrationDirectoryList before running!*

.. code-block:: text

  # Nifty configuration file.
  #
  # Each section lists parameters required by a pipeline step.

  manualMode = False
  over = False
  extractionXC = 15.0
  extractionYC = 33.0
  extractionRadius = 2.5
  scienceOneDExtraction = True
  scienceDirectoryList = []
  telluricDirectoryList = []
  calibrationDirectoryList = []

  [nifsPipelineConfig]
  sort = False
  calibrationReduction = False
  telluricReduction = False
  scienceReduction = False
  telluricCorrection = True
  fluxCalibration = False
  merge = True
  telluricCorrectionMethod = 'gnirs'
  fluxCalibrationMethod = 'gnirs'
  mergeMethod = ''

  [sortConfig]
  rawPath = '/Users/nat/data/TUTORIAL'
  program = ''
  proprietaryCookie = ''
  skyThreshold = 2.0
  sortTellurics = True
  telluricTimeThreshold = 5400

  [calibrationReductionConfig]
  baselineCalibrationStart = 1
  baselineCalibrationStop = 4

  [telluricReductionConfig]
  telStart = 1
  telStop = 5
  telluricSkySubtraction = True

  [telluricCorrectionConfig]
  telluricCorrectionStart = 1
  telluricCorrectionStop = 9
  hLineMethod = 'vega'
  hLineInter = False
  continuumInter = False
  telluricInter = False
  tempInter = False
  standardStarSpecTemperature = ''
  standardStarMagnitude = ''
  standardStarRA = ''
  standardStarDec = ''
  standardStarBand = ''

  [fluxCalbrationConfig]
  fluxCalibrationStart = 1
  fluxCalibrationStop = 6

  [mergeConfig]
  mergeStart = 1
  mergeStop = 3
  mergeType = 'median'
  use_pq_offsets = True
  im3dtran = True

  # Good luck with your Science!

And run the nifsPipeline with:

.. code-block:: text

 runNifty nifsPipeline config.cfg

Preparing the .cfg Input File
=============================

Nifty reads data reduction parameters with a config parser developed by Michael Foord. See
http://www.voidspace.org.uk/python/configobj.html for full documentation on the parser.

Interactive Input Preparation
-----------------------------

The best way to learn about what each config file parameter does is to populate an input file interactively by typing:

.. code-block:: text

 runNifty nifsPipeline -i

This will, for each parameter, print an explanation and supply a default parameter that you can accept by pressing enter. The output file
is named "config.cfg".

An Example Input File
---------------------

Nifty includes a default configuration file in the runtimeData/ directory. As of v1.0b2, It looks like this:
.. TODO(nat): This is out of data! Update this!

.. code-block:: text

 # Nifty configuration file.
 #
 # Each section lists parameters required by a pipeline step.

 manualMode = False
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
 rawPath = ''
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
 telluricCorrectionMethod = ''
 telinter = False
 fluxCalibrationMethod = ''
 use_pq_offsets = True
 im3dtran = True

 # Good luck with your Science!

Data Reduction Examples
=======================

Observations of Titan
---------------------

Recipe used: defaultConfig.cfg

Observations of a Moderate Redshift Galaxy
------------------------------------------

Recipe used: defaultConfig.cfg

Let's reduce NIFS data of a moderate redshift galaxy, located at z ~ 1.284. This is a faint target, so after making
individual cubes we use the reported telescope P and Q offsets to blindly merge our final cubes.

As this program is out of its proprietary period and available on the Gemini Public Archive, we can use the defaultConfig.cfg configuration
file and specify its program ID to reduce it.

.. code-block:: text

  runNifty -f GN-2013A-Q-62

We could also launch the reduction from a provided configuration file.


Contents of the configuration file:

.. code-block:: text

  TODO(nat): When finalized fill this out!

To launch the reduction:

.. code-block:: text

  runNifty <configurationFile>

Tutorials
=========

H Line Removal
--------------

The H-line removal can be done non-interactively, but it is advised that this be performed
interactively and using the "vega_tweak" method in order to accurately scale the vega spectrum.
In the interactive mode for the initial scaling and call to "telluric" these are the cursor keys
and colon commands (from http://iraf.net/irafhelp.php?val=telluric&help=Help+Page):

- ? - print help
- a - automatic RMS minimization within sample regions
- c - toggle calibration spectrum display
- d - toggle data spectrum display
- e - expand (double) the step for the current selection
- q - quit
- r - redraw the graphs
- s - add or reset sample regions
- w - window commands (see :/help for additional information)
- x - graph and select from corrected shifted candidates
- y - graph and select from corrected scaled candidates

- :help           - print help
- :shift  [value] - print or reset the current shift
- :scale  [value] - print or reset the current scale
- :dshift [value] - print or reset the current shift step
- :dscale [value] - print or reset the current scale step
- :offset [value] - print or reset the current offset between spectra
- :sample [value] - print or reset the sample regions
- :smooth [value] - print or reset the smoothing box size

To decrease the scale or shift value, the cursor must be under the spectrum and to increase
these values the cursor must be above the spectrum. Occasionally, this will not work in which
case the value can be designated with a colon command.

If using the vega_tweak or other interactive line removal method, the lines can be removed
in a splot environment (commands found here: http://stsdas.stsci.edu/cgi-bin/gethelp.cgi?splot.hlp).
The most useful commands for this are:

- k + (g, l or v)

Mark two continuum points and fit a single line profile. The second key selects the
type of profile: g for gaussian, l for lorentzian, and v for voigt. Any other second key
defaults to gaussian. The center, continuum at the center, core intensity, integrated flux,
equivalent width, and FWHMs are printed and saved in the log file. See d for fitting multiple profiles and - to subtract the fit.

- w

Window the graph. For further help type ? to the "window:" prompt or see help under gtools.
To cancel the windowing use a.

It is necessary to press 'i' before 'q' once the h-lines have been removed in order to save the changes.

Custom Telluric Corrections
---------------------------



You can supply your own continuum-normalized telluric correction spectrum by placing a "telluricCorrection.fits" one D spectra
and a "fit.fits" that you used to normalize that spectra in the science observation directory. Both spectra must be 2040 pixels
long and have the data extension located in header unit zero. Note that overwrite must be turned off for this to work.



Merging Data Cubes
------------------

Nifty offers a few ways to merge data cubes. These are all contained in the
nifsMerge.py script.

**Note:** If cubes are not transposed each call to iraf.imcombine() can take
25 minutes or more. The current implementation is much slower at combining when cubes
have a y-offset.

Cubes Were Shifted by Hand with QFitsView or Similar

A user can shift cubes by hand and add the prefix "shift" to the cube name. The
pipeline will automatically find these cubes and combine them with gemcube.

If no "shift"-prefixed cubes exist the user has two more choices to make. The first is to
generate offsets automatically or to provide an offsets file by hand.

Generating an offsets.txt File

If use_pq_offsets is True in the config.cfg file, *Nifty* will determine offsets automatically from the
POFFSET and QOFFSET entry of each cubes .fits header. Otherwise, *Nifty* will pause
and wait for you to provide a suitably formatted offsets.txt file in the
scienceObjectName/Merged/date_obsid/ directory.

Using iraf.im3dtran()

Cubes have been found to combine ~50 times faster when the y and lambda axis are
swapped with iraf.im3dtran(). In our tests we found it took ~25 minutes to merge
cubes without transposition and ~0.5 minutes to merge cubes in a tranposed state.

We have found the cubes produced with and without tranposition to be identical. We
have made the default not to use transposition but we urge further testing.

Known Issues
============

nifsPipeline.py
-----------------

nifsSort.py
-----------

Two things can routinely cause nifsSort to fail.

Object and Sky frame differentiation

Relevant warning:

..code-block:: text

  #####################################################################
  #####################################################################

       WARNING in sort: science " <scienceObservationName>
                        in " <currentWorkingDirectory>
                        does not have a scienceFrameList.")
                        I am trying to rewrite it with zero point offsets.

  #####################################################################
  #####################################################################

Solution:

- Change the skyThreshold parameter (given in arc seconds) and re-run sort.

If the sorting script does not create a skyFrameList in the object or telluric observation
directories this means that the offsets between sky frames and object frames were different
than expected. A skyFrameList can be manually created and saved in the appropriate directory, or
the skyThreshold parameter modified.

Telluric and Science Frame Matching

Relevant warning:

..code-block:: text

  #####################################################################

  WARNING in sort: no tellurics data found for science " <scienceImageName>
       in " <currentWorkingdirectory

  #####################################################################

Solution:

- Raise telluricTimeThreshold to something above 5400 seconds.

By default standard star observations are matched with each science frame if they
are within 1.5 hours (5400) seconds in UT start time. Sometimes just a few science frames
will be outside that threshold.

If you see the relevant warning after running sort, you will have to raise the
telluricTimeThreshold in the config.cfg file if you want to do telluric corrections.


nifsBaselineCalibration.py
--------------------------

- **Long data file path names are not fed to IRAF tasks**. It seems IRAF task parameters
must be 99 characters or less. Nifty's data files are stored in the Astroconda environment
packages directory; for example, on my system it is "/Users/nat/miniconda2/envs/niftypip/lib/python2.7/site-packages/nifty/pipeline/".
If you have a long username, for example, this can cause the path name to be too long to
be parsed by iraf.
*Temporary fix:* I have made the names of all the data files short enough for it to work
okay on my system. **Please let me know if this seems to be
causing you issues and I can come up with a better fix.**


nifsReduce.py
-------------

- z-band data is not capable of a flux calibration (yet!).
- Seems to be missing the first peak of the ronchi slit when iraf.nfsdist() is run interactively.
  This does not seem to be a problem.
- We noticed that iraf.nfsdist() produced different results when run interactively and
  non-interactively. To test check the log for iraf.nfsdist() output and make sure it is
  identifying 8/8 or 9/9 peaks every time.
- iraf.nftelluric() was not built to be run automatically. A lightly tested modified
  version that allows an automatic telluric correction is included in the extras directory
  but more testing is needed. For now applyTelluricPython() is recommended.

nifsMerge.py
------------

- When overwrite is turned on, merging the final cubes from multiple directories redundantly repeats.
This is a good quick fix for someone to implement.

nifsTelluric.py
---------------

nifsTelluric.py and nifsFluxCalibrate.py rely on several IRAF tasks finding information in the correct image
header. If this implicit header data matching changes in future IRAF implementations these tasks will break.
A fix could be to explicitly specify the data header for each task. TODO(nat): Try to do this before you leave.

- iraf.imarith() is having some strange errors. I'm using astropy and numpy instead to do the 2 imarith steps.
- See nifsFluxCalibrate for the iraf.gemini() and iraf.imarith() bug.

nifsFluxCalibrate.py
--------------------

- **If iraf.gemini() is called in nifsTelluric.py and the two steps are run back to back,**
iraf.imarith() does not work in nifsFluxCalibrate.py. iraf.imarith can't seem to open the result
of step 3; it throws this error:

..code-block:: text

  3_BBodyN20100401S0182 is not an image or a number

When I ran nifsTelluric.py and nifsFluxCalibrated.py back to back, using nifsPipeline.py as a wrapper,
iraf.imarith() *worked when iraf.gemini() was commented out in nifsTelluric.py*. It crashed with the
above error when iraf.gemini() was uncommented.

I've implemented a just-as-good solution using astropy and numpy.

nifsUtils.py
------------

General Issues
--------------

- A longstanding bug (see `astropy <https://github.com/astropy/astropy/pull/960>`_ ) in astropy has made it
  difficult to build Nifty as a binary executable.
- The conversion of print statements to logging.info() statements was messy. Some of these
  may still not be properly converted and will throw nasty tracebacks. However these seem to
  have no effect on the functionioning of the code.
- Logging is still not perfect. One or two iraf tasks are sending their log files to
  "nifs.log" instead of "Nifty.log".

Maintaining Nifty
=================

Documentation
-------------

Right now there exists four forms of documentation.

Paper

.. Insert a paper!

README.rst


.rst Files in the docs/ directory


This file, others like it in the docs/ directory and the README are written in
reStructuredText. This markup language integrates well with Python's automatic
documentation builder (we used Sphinx) and Github as well as being human readable. You can
read more about reStructuredText `here <http://www.sphinx-doc.org/en/stable/rest.html>`_.

Comments and DocStrings in Source Code

Tests
-----

This is a todo. Currently we do not have automated tests.

Pipeline Structure
------------------

See the Nifty paper for a high level overview. Nifty general runs with the following procedure:

- A script in the scripts/ directory is called from the command line.
- This script imports the relevant pipeline and steps from the nifty/pipeline/ and nifty/pipeline/steps/directories.
- The script then launches the appropriate pipeline,
- This pipeline launches the appropriate steps,
- These steps launch the appropriate routines, and
- These routines launch the appropriate sub-routines.

Nifty is built at the lowest level from Python and IRAF subroutines. It is built so that it is relatively
easy to change the implementation of the underlying tasks.

Updates
-------

To update Nifty, do five things:

- *Try to do your development in a new branch or fork, not the master branch of the repository*
- Before uploading, do a few test data reductions.
- Pick an appropriate version number based on `semantic versioning <http://semver.org/>`_; update the setup.py
- Commit all changes to GitHub
- Create a new Github Release
- `Upload the latest version to PyPi.org < https://packaging.python.org/tutorials/distributing-packages/>`_


..code-block:: text

  rm -r dist build             # Clean up old files
  python setup.py bdist_wheel  # Build python wheels
  twine upload dist/*          # Upload to PyPi.org

Version Numbers


Nifty uses semantic versioning(see http://semver.org/). This means version numbers come in

.. code-block:: text

  MAJOR.MINOR.PATCH

In brief, when releasing a version of Nifty that is not backward-compatible with old test recipes,
or changes break the public API, it is time to increment the MAJOR version number.

..TODO(nat): maybe make this a little clearer.

Code Conventions
----------------

Nifty was partly written using `atom <https://atom.io/>`_. Error messages,
warnings and updates were partly written using templates in the included snippets.cson file.

Where possible, nat used 2D (and higher) dimensional lists to implement error
checking flags. These are particularly prominent in sort.

Variables and functions were named using conventions in the
`Python Style Guide <https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles>`_.
Specifically a mix of camelCase and lower_case_with_underscores was used.

Code style was influenced by the `Google Python Style Guide <https://google.github.io/styleguide/pyguide.html>`_.

Nifty uses the Google docstring style. Examples of docstrings can be found
`here <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_.

Other Python comments use the following convention:

- A # is followed by a space and a capital letter.
- All comments end in a period where possible.

Future Work
===========

Throughout the code, ncomeau has placed many TODO notes. These are things that
should be reviewed at some point.

Future work:

- Implement more telluric and flux calibration methods
- Automated Gemini data reductions at the start of the day.
- Object Oriented rewrite; see the JWST calibration pipeline. Pipelines, Steps,
Routines and Tasks may implemented better as software objects.
- XDGNIRS integration and NDMAPPER (James EH Turner) integration
- Analysis tools: automatic velocity field? Dispersion?
- Python 3 compatability(if possible)
- Compiling as a self-contained executable
- Full AstroConda integration

Changelog
=========
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/en/1.0.0/>`_
and this project adheres to `Semantic Versioning <http://semver.org/spec/v2.0.0.html>`_.

Unreleased
----------
All in-development changes will be tracked here.

- Adding unit tests for each step and integration test for pipeline.
- Finished integrating multiple types of cube merging.

1.0b4 - 2017-09-12
------------------
Much refined and patched Beta release. Still not finished but much more robust.

- Verified overwrite; it seems to be safe to use now.
- Fixing telluric correction and absolute flux calibration.
- Added 1D extraction routine.
- Preliminary addition of three types of cubes and cube merging.

1.0b1 - 2017-09-08
------------------
Preliminary Beta release.

- Syntax errors mean this version will not compile.
- Fixing merge flip due to differences between NIFS + ALTAIR and NIFS w/o ALTAIR on the bottom port.

1.0a1 - 2017-08-31
------------------
Preliminary Alpha release.

- .whl uploaded to PIP, docs uploaded to
ReadTheDocs and preliminary DOI assigned.

API
===

Note: I didn't have time to implement this using Sphinx automodule. Nifty has fairly good docstrings and you
can use individual steps, routines and tasks by importing them. This is a todo.

.. TODO(nat): implement the public API.
