Known Issues
============

Nifty.py
--------

nifsSort.py
-----------

nifsBaselineCalibration.py
--------------------------
- **Long data file path names are not fed to IRAF tasks**. It seems IRAF task parameters
must be 99 characters or less. Nifty's data files are stored in the Astroconda environment
packages directory; for example, on my system it is "/Users/nat/miniconda2/envs/niftypip/lib/python2.7/site-packages/nifty/pipeline/".
If you have a long username, for example, this can cause the path name to be too long to
be parsed by iraf.
*Temporary fix:* I have made the names of all the data files short enough for it to work
okay on my system. **Please let me (ncomeau AT gemini DOT edu) know if this seems to be
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

nifsDefs.py
-----------

General Issues
--------------
- A longstanding bug (see `astropy<https://github.com/astropy/astropy/pull/960>`_ ) in astropy has made it
  difficult to build Nifty as a binary executable.
- The conversion of print statements to logging.info() statements was messy. Some of these
  may still not be properly converted and will throw nasty tracebacks. However these seem to
  have no effect on the functionioning of the code.
- Logging is still not perfect. One or two iraf tasks are sending their log files to
  "nifs.log" instead of "Nifty.log".
