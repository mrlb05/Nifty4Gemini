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
