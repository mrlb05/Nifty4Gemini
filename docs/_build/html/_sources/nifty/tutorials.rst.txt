H Line Removal
==============

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

Merging Data Cubes
==================

Nifty offers a few ways to merge data cubes. These are all contained in the
nifsMerge.py script.

**Note:** If cubes are not transposed each call to iraf.imcombine() can take
25 minutes or more. The current implementation is much slower at combining when cubes
have a y-offset.

Cubes Were Shifted by Hand with QFitsView or Similar
----------------------------------------------------
A user can shift cubes by hand and add the prefix "shift" to the cube name. The
pipeline will automatically find these cubes and combine them with gemcube.

If no "shift"-prefixed cubes exist the user has two more choices to make. The first is to
generate offsets automatically or to provide an offsets file by hand.

Generating an offsets.txt File
------------------------------
If use_pq_offsets is True in the config.cfg file, *Nifty* will determine offsets automatically from the
POFFSET and QOFFSET entry of each cubes .fits header. Otherwise, *Nifty* will pause
and wait for you to provide a suitably formatted offsets.txt file in the
scienceObjectName/Merged/date_obsid/ directory.

Using iraf.im3dtran()
---------------------
Cubes have been found to combine 50 times faster when the y and lambda axis are
swapped with iraf.im3dtran(). In our tests we found it took ~25 minutes to merge
cubes without transposition and ~0.5 minutes to merge cubes in a tranposed state.

We have found the cubes produced with and without tranposition to be identical. We
have made the default not to use transposition but we urge further testing.
