Example of Directory Modifications Through Nifty
================================================

This is an example of how the Nifty directory tree appears after each step of the
date reduction. These directory trees were created using a custom **niftree** bash command:

.. code-block:: text

  find . -name .git -prune -o -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'

Add the following line to your ~/.bash_profile to create the **niftree** alias:

.. code-block:: text

  alias niftree="find . -name .git -prune -o -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"

Table of Contents
-----------------

- nifsSort_

- nifsBaselineCalibration_

- nifsReduceTelluric_

- nifsReduceScience_

Contents of user_options.json if you would like to reproduce this experiment:

.. code-block:: text

    "sci": "yes",
    "mag": null,
    "over": false,
    "telred": "yes",
    "tel": "yes",
    "efficiencySpectrumCorrection": "yes",
    "telinter": false,
    "telluric_correction_method": "python",
    "telStop": 6,
    "continuuminter": false,
    "telStart": 1,
    "program": null,
    "spectemp": null,
    "__version__": "v0.1.1",
    "red": "yes",
    "sort": "yes",
    "sciStop": 6,
    "rawPath": "/Users/ncomeau/data/TUTORIAL_HD141004",
    "rstop": 4,
    "hlineinter": false,
    "rstart": 1,
    "hline_method": "vega",
    "date": null,
    "copy": null,
    "sciStart": 1,
    "use_pq_offsets": true,
    "merge": "yes"

.. _nifsSort:

nifsSort
========

Before nifsSort
---------------

.. code-block:: text

    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After makePythonLists()
-----------------------

makePythonLists() only creates python lists of files; it does not write any new files.

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After sortScienceAndTelluric()
------------------------------

sortScienceAndTelluric() creates a directory structure and copies science, telluric, sky frames and
acquisitions to the appropriate directories.

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After sortCalibrations()
------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____flatdarklist
    | | | |____flatlist
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____ronchilist
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After matchTels()
-----------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____flatdarklist
    | | | |____flatlist
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____ronchilist
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After nifsSort
--------------

nifsSort.py adds a scienceObjectName directory and some data files in the runtimeData directory.

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____flatdarklist
    | | | |____flatlist
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____ronchilist
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

.. _nifsBaselineCalibration:

nifsBaselineCalibration
=======================

Before running nifsBaselineCalibration()
----------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____flatdarklist
    | | | |____flatlist
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____ronchilist
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 1: Locate the Spectrum
---------------------------------

This step writes two new files; a .fits shiftfile and a textfile storing the name of the shiftfile.

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____flatdarklist
    | | | |____flatlist
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____ronchilist
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 2: Flat Field
------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
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
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 3: Wavelength Solution
---------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____rgnN20100401S0137.fits
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
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 4: Spatial Distortion
--------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After nifsBaselineCalibration
-----------------------------

No new files were created since the end of Step 4: Spatial Distortion.

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl


.. _nifsReduceTelluric:

nifsReduce(tellurics)
=====================

Before nifsReduce
-----------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

Before Step 1: Locate the Spectrum
----------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____database
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    | | | | | |____wrgnN20100401S0137.fits
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 1: Locate the Spectrum
---------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____database
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____tellist
    | | | | | |____wrgnN20100401S0137.fits
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 2: Sky Subtraction
-----------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____database
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____tellist
    | | | | | |____wrgnN20100401S0137.fits
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 3: Flat Fielding and Bad Pixels Correction
-----------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____database
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____tellist
    | | | | | |____wrgnN20100401S0137.fits
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 4: 2D to 3D Transformation and Wavelength Calibration
----------------------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____tellist
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 5: Extract 1D Spectra and Combined Telluric 1D Spectrum
------------------------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____tellist
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 6: Make Efficiency Spectrum for Flux Calibration and Telluric Correction
-----------------------------------------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After nifsReduce(tellurics)
---------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl


.. _nifsReduceScience:

nifsReduce(science)
===================

Before nifsReduce(Science)
--------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

Before Step 1: Locate the Spectrum (and prepare raw data)
---------------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____database
    | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____rgnN20100410S0375.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | | |____wrgnN20100401S0137.fits
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 1: Locate the Spectrum (and prepare raw data)
--------------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____database
    | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____nN20100401S0182.fits
    | | | | |____nN20100401S0183.fits
    | | | | |____nN20100401S0184.fits
    | | | | |____nN20100401S0186.fits
    | | | | |____nN20100401S0187.fits
    | | | | |____nN20100401S0188.fits
    | | | | |____nN20100401S0189.fits
    | | | | |____nN20100401S0190.fits
    | | | | |____rgnN20100410S0375.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | | |____wrgnN20100401S0137.fits
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 2: Sky Subtraction
-----------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____database
    | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____nN20100401S0182.fits
    | | | | |____nN20100401S0183.fits
    | | | | |____nN20100401S0184.fits
    | | | | |____nN20100401S0186.fits
    | | | | |____nN20100401S0187.fits
    | | | | |____nN20100401S0188.fits
    | | | | |____nN20100401S0189.fits
    | | | | |____nN20100401S0190.fits
    | | | | |____rgnN20100410S0375.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | | |____snN20100401S0182.fits
    | | | | |____snN20100401S0184.fits
    | | | | |____snN20100401S0186.fits
    | | | | |____snN20100401S0188.fits
    | | | | |____snN20100401S0190.fits
    | | | | |____wrgnN20100401S0137.fits
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 3: Flat Fielding and Bad Pixels Correction
-----------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____brsnN20100401S0182.fits
    | | | | |____brsnN20100401S0184.fits
    | | | | |____brsnN20100401S0186.fits
    | | | | |____brsnN20100401S0188.fits
    | | | | |____brsnN20100401S0190.fits
    | | | | |____database
    | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____nN20100401S0182.fits
    | | | | |____nN20100401S0183.fits
    | | | | |____nN20100401S0184.fits
    | | | | |____nN20100401S0186.fits
    | | | | |____nN20100401S0187.fits
    | | | | |____nN20100401S0188.fits
    | | | | |____nN20100401S0189.fits
    | | | | |____nN20100401S0190.fits
    | | | | |____rgnN20100410S0375.fits
    | | | | |____rsnN20100401S0182.fits
    | | | | |____rsnN20100401S0184.fits
    | | | | |____rsnN20100401S0186.fits
    | | | | |____rsnN20100401S0188.fits
    | | | | |____rsnN20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | | |____snN20100401S0182.fits
    | | | | |____snN20100401S0184.fits
    | | | | |____snN20100401S0186.fits
    | | | | |____snN20100401S0188.fits
    | | | | |____snN20100401S0190.fits
    | | | | |____wrgnN20100401S0137.fits
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 4: 2D to 3D Transformation and Wavelength Calibration
----------------------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____brsnN20100401S0182.fits
    | | | | |____brsnN20100401S0184.fits
    | | | | |____brsnN20100401S0186.fits
    | | | | |____brsnN20100401S0188.fits
    | | | | |____brsnN20100401S0190.fits
    | | | | |____database
    | | | | | |____fcfbrsnN20100401S0182_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_9_sdist
    | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | |____fbrsnN20100401S0182.fits
    | | | | |____fbrsnN20100401S0184.fits
    | | | | |____fbrsnN20100401S0186.fits
    | | | | |____fbrsnN20100401S0188.fits
    | | | | |____fbrsnN20100401S0190.fits
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____nN20100401S0182.fits
    | | | | |____nN20100401S0183.fits
    | | | | |____nN20100401S0184.fits
    | | | | |____nN20100401S0186.fits
    | | | | |____nN20100401S0187.fits
    | | | | |____nN20100401S0188.fits
    | | | | |____nN20100401S0189.fits
    | | | | |____nN20100401S0190.fits
    | | | | |____rgnN20100410S0375.fits
    | | | | |____rsnN20100401S0182.fits
    | | | | |____rsnN20100401S0184.fits
    | | | | |____rsnN20100401S0186.fits
    | | | | |____rsnN20100401S0188.fits
    | | | | |____rsnN20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | | |____snN20100401S0182.fits
    | | | | |____snN20100401S0184.fits
    | | | | |____snN20100401S0186.fits
    | | | | |____snN20100401S0188.fits
    | | | | |____snN20100401S0190.fits
    | | | | |____tfbrsnN20100401S0182.fits
    | | | | |____tfbrsnN20100401S0184.fits
    | | | | |____tfbrsnN20100401S0186.fits
    | | | | |____tfbrsnN20100401S0188.fits
    | | | | |____tfbrsnN20100401S0190.fits
    | | | | |____wrgnN20100401S0137.fits
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 5: Apply Telluric Correction and Flux Calibration
------------------------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____brsnN20100401S0182.fits
    | | | | |____brsnN20100401S0184.fits
    | | | | |____brsnN20100401S0186.fits
    | | | | |____brsnN20100401S0188.fits
    | | | | |____brsnN20100401S0190.fits
    | | | | |____cptfbrsnN20100401S0182.fits
    | | | | |____cptfbrsnN20100401S0184.fits
    | | | | |____cptfbrsnN20100401S0186.fits
    | | | | |____cptfbrsnN20100401S0188.fits
    | | | | |____cptfbrsnN20100401S0190.fits
    | | | | |____ctfbrsnN20100401S0182.fits
    | | | | |____ctfbrsnN20100401S0184.fits
    | | | | |____ctfbrsnN20100401S0186.fits
    | | | | |____ctfbrsnN20100401S0188.fits
    | | | | |____ctfbrsnN20100401S0190.fits
    | | | | |____database
    | | | | | |____fcfbrsnN20100401S0182_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_9_sdist
    | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | |____fbrsnN20100401S0182.fits
    | | | | |____fbrsnN20100401S0184.fits
    | | | | |____fbrsnN20100401S0186.fits
    | | | | |____fbrsnN20100401S0188.fits
    | | | | |____fbrsnN20100401S0190.fits
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____nN20100401S0182.fits
    | | | | |____nN20100401S0183.fits
    | | | | |____nN20100401S0184.fits
    | | | | |____nN20100401S0186.fits
    | | | | |____nN20100401S0187.fits
    | | | | |____nN20100401S0188.fits
    | | | | |____nN20100401S0189.fits
    | | | | |____nN20100401S0190.fits
    | | | | |____rgnN20100410S0375.fits
    | | | | |____rsnN20100401S0182.fits
    | | | | |____rsnN20100401S0184.fits
    | | | | |____rsnN20100401S0186.fits
    | | | | |____rsnN20100401S0188.fits
    | | | | |____rsnN20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | | |____snN20100401S0182.fits
    | | | | |____snN20100401S0184.fits
    | | | | |____snN20100401S0186.fits
    | | | | |____snN20100401S0188.fits
    | | | | |____snN20100401S0190.fits
    | | | | |____tfbrsnN20100401S0182.fits
    | | | | |____tfbrsnN20100401S0184.fits
    | | | | |____tfbrsnN20100401S0186.fits
    | | | | |____tfbrsnN20100401S0188.fits
    | | | | |____tfbrsnN20100401S0190.fits
    | | | | |____wrgnN20100401S0137.fits
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl

After Step 6: Create Combined Final 3D Cube.
--------------------------------------------

.. code-block:: text

    .
    |____.DS_Store
    |____.gitignore
    |____docs
    | |____directoryModifications.rst
    | |____example_calibrationDirectoryList.txt
    | |____example_scienceDirectoryList.txt
    | |____example_telluricDirectoryList.txt
    | |____faq.rst
    | |____hline_removal.rst
    | |____maintenance.rst
    | |____nifs_pipeline_june_2015.pdf
    | |____preparingJSONinput.rst
    |____extras
    | |____gemini_sort.py
    | |____MANIFEST.in
    | |____old_merge.py
    | |____setup.py
    | |____spec-file-osx-64.txt
    |____HD141004
    | |____20100401
    | | |____Calibrations_K
    | | | |____arcdarkfile
    | | | |____arcdarklist
    | | | |____arclist
    | | | |____database
    | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | |____flatdarklist
    | | | |____flatfile
    | | | |____flatlist
    | | | |____gnN20100401S0137.fits
    | | | |____gnN20100410S0362.fits
    | | | |____gnN20100410S0368.fits
    | | | |____gnN20100410S0373.fits
    | | | |____gnN20100410S0375.fits
    | | | |____N20100401S0137.fits
    | | | |____N20100401S0181.fits
    | | | |____N20100410S0362.fits
    | | | |____N20100410S0363.fits
    | | | |____N20100410S0364.fits
    | | | |____N20100410S0365.fits
    | | | |____N20100410S0366.fits
    | | | |____N20100410S0367.fits
    | | | |____N20100410S0368.fits
    | | | |____N20100410S0369.fits
    | | | |____N20100410S0370.fits
    | | | |____N20100410S0371.fits
    | | | |____N20100410S0372.fits
    | | | |____N20100410S0373.fits
    | | | |____N20100410S0374.fits
    | | | |____N20100410S0375.fits
    | | | |____N20100410S0376.fits
    | | | |____nN20100401S0137.fits
    | | | |____nN20100401S0181.fits
    | | | |____nN20100410S0362.fits
    | | | |____nN20100410S0363.fits
    | | | |____nN20100410S0364.fits
    | | | |____nN20100410S0365.fits
    | | | |____nN20100410S0366.fits
    | | | |____nN20100410S0367.fits
    | | | |____nN20100410S0368.fits
    | | | |____nN20100410S0369.fits
    | | | |____nN20100410S0370.fits
    | | | |____nN20100410S0371.fits
    | | | |____nN20100410S0372.fits
    | | | |____nN20100410S0373.fits
    | | | |____nN20100410S0374.fits
    | | | |____nN20100410S0375.fits
    | | | |____nN20100410S0376.fits
    | | | |____rgnN20100401S0137.fits
    | | | |____rgnN20100410S0362.fits
    | | | |____rgnN20100410S0362_flat.fits
    | | | |____rgnN20100410S0362_sflat.fits
    | | | |____rgnN20100410S0362_sflat_bpm.pl
    | | | |____rgnN20100410S0368.fits
    | | | |____rgnN20100410S0368_dark.fits
    | | | |____rgnN20100410S0375.fits
    | | | |____ronchifile
    | | | |____ronchilist
    | | | |____sflat_bpmfile
    | | | |____sflatfile
    | | | |____shiftfile
    | | | |____sN20100410S0362.fits
    | | | |____wrgnN20100401S0137.fits
    | | |____K
    | | | |____obs107
    | | | | |____brsnN20100401S0182.fits
    | | | | |____brsnN20100401S0184.fits
    | | | | |____brsnN20100401S0186.fits
    | | | | |____brsnN20100401S0188.fits
    | | | | |____brsnN20100401S0190.fits
    | | | | |____cptfbrsnN20100401S0182.fits
    | | | | |____cptfbrsnN20100401S0184.fits
    | | | | |____cptfbrsnN20100401S0186.fits
    | | | | |____cptfbrsnN20100401S0188.fits
    | | | | |____cptfbrsnN20100401S0190.fits
    | | | | |____ctfbrsnN20100401S0182.fits
    | | | | |____ctfbrsnN20100401S0184.fits
    | | | | |____ctfbrsnN20100401S0186.fits
    | | | | |____ctfbrsnN20100401S0188.fits
    | | | | |____ctfbrsnN20100401S0190.fits
    | | | | |____database
    | | | | | |____fcfbrsnN20100401S0182_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0182_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0182_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0184_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0184_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0186_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0186_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0188_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0188_SCI_9_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_10_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_10_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_11_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_11_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_12_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_12_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_13_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_13_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_14_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_14_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_15_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_15_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_16_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_16_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_17_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_17_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_18_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_18_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_19_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_19_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_1_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_1_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_20_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_20_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_21_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_21_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_22_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_22_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_23_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_23_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_24_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_24_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_25_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_25_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_26_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_26_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_27_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_27_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_28_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_28_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_29_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_29_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_2_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_2_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_3_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_3_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_4_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_4_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_5_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_5_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_6_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_6_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_7_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_7_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_8_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_8_sdist
    | | | | | |____fcfbrsnN20100401S0190_SCI_9_lamp
    | | | | | |____fcfbrsnN20100401S0190_SCI_9_sdist
    | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | |____fbrsnN20100401S0182.fits
    | | | | |____fbrsnN20100401S0184.fits
    | | | | |____fbrsnN20100401S0186.fits
    | | | | |____fbrsnN20100401S0188.fits
    | | | | |____fbrsnN20100401S0190.fits
    | | | | |____N20100401S0182.fits
    | | | | |____N20100401S0183.fits
    | | | | |____N20100401S0184.fits
    | | | | |____N20100401S0185.fits
    | | | | |____N20100401S0186.fits
    | | | | |____N20100401S0187.fits
    | | | | |____N20100401S0188.fits
    | | | | |____N20100401S0189.fits
    | | | | |____N20100401S0190.fits
    | | | | |____Nifty.log
    | | | | |____nN20100401S0182.fits
    | | | | |____nN20100401S0183.fits
    | | | | |____nN20100401S0184.fits
    | | | | |____nN20100401S0186.fits
    | | | | |____nN20100401S0187.fits
    | | | | |____nN20100401S0188.fits
    | | | | |____nN20100401S0189.fits
    | | | | |____nN20100401S0190.fits
    | | | | |____rgnN20100410S0375.fits
    | | | | |____rsnN20100401S0182.fits
    | | | | |____rsnN20100401S0184.fits
    | | | | |____rsnN20100401S0186.fits
    | | | | |____rsnN20100401S0188.fits
    | | | | |____rsnN20100401S0190.fits
    | | | | |____scienceFrameList
    | | | | |____skyframelist
    | | | | |____snN20100401S0182.fits
    | | | | |____snN20100401S0184.fits
    | | | | |____snN20100401S0186.fits
    | | | | |____snN20100401S0188.fits
    | | | | |____snN20100401S0190.fits
    | | | | |____tfbrsnN20100401S0182.fits
    | | | | |____tfbrsnN20100401S0184.fits
    | | | | |____tfbrsnN20100401S0186.fits
    | | | | |____tfbrsnN20100401S0188.fits
    | | | | |____tfbrsnN20100401S0190.fits
    | | | | |____wrgnN20100401S0137.fits
    | | | |____Tellurics
    | | | | |____obs109
    | | | | | |____brsnN20100401S0138.fits
    | | | | | |____brsnN20100401S0140.fits
    | | | | | |____brsnN20100401S0142.fits
    | | | | | |____brsnN20100401S0144.fits
    | | | | | |____brsnN20100401S0146.fits
    | | | | | |____cgxtfbrsnN20100401S0138.fits
    | | | | | |____database
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0138_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0140_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0142_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0144_SCI_9_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_10_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_11_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_12_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_13_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_14_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_15_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_16_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_17_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_18_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_19_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_1_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_20_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_21_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_22_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_23_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_24_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_25_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_26_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_27_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_28_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_29_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_2_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_3_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_4_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_5_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_6_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_7_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_8_sdist
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_lamp
    | | | | | | |____fcfbrsnN20100401S0146_SCI_9_sdist
    | | | | | | |____idrgnN20100410S0375_SCI_10_
    | | | | | | |____idrgnN20100410S0375_SCI_11_
    | | | | | | |____idrgnN20100410S0375_SCI_12_
    | | | | | | |____idrgnN20100410S0375_SCI_13_
    | | | | | | |____idrgnN20100410S0375_SCI_14_
    | | | | | | |____idrgnN20100410S0375_SCI_15_
    | | | | | | |____idrgnN20100410S0375_SCI_16_
    | | | | | | |____idrgnN20100410S0375_SCI_17_
    | | | | | | |____idrgnN20100410S0375_SCI_18_
    | | | | | | |____idrgnN20100410S0375_SCI_19_
    | | | | | | |____idrgnN20100410S0375_SCI_1_
    | | | | | | |____idrgnN20100410S0375_SCI_20_
    | | | | | | |____idrgnN20100410S0375_SCI_21_
    | | | | | | |____idrgnN20100410S0375_SCI_22_
    | | | | | | |____idrgnN20100410S0375_SCI_23_
    | | | | | | |____idrgnN20100410S0375_SCI_24_
    | | | | | | |____idrgnN20100410S0375_SCI_25_
    | | | | | | |____idrgnN20100410S0375_SCI_26_
    | | | | | | |____idrgnN20100410S0375_SCI_27_
    | | | | | | |____idrgnN20100410S0375_SCI_28_
    | | | | | | |____idrgnN20100410S0375_SCI_29_
    | | | | | | |____idrgnN20100410S0375_SCI_2_
    | | | | | | |____idrgnN20100410S0375_SCI_3_
    | | | | | | |____idrgnN20100410S0375_SCI_4_
    | | | | | | |____idrgnN20100410S0375_SCI_5_
    | | | | | | |____idrgnN20100410S0375_SCI_6_
    | | | | | | |____idrgnN20100410S0375_SCI_7_
    | | | | | | |____idrgnN20100410S0375_SCI_8_
    | | | | | | |____idrgnN20100410S0375_SCI_9_
    | | | | | | |____idwrgnN20100401S0137_SCI_10_
    | | | | | | |____idwrgnN20100401S0137_SCI_11_
    | | | | | | |____idwrgnN20100401S0137_SCI_12_
    | | | | | | |____idwrgnN20100401S0137_SCI_13_
    | | | | | | |____idwrgnN20100401S0137_SCI_14_
    | | | | | | |____idwrgnN20100401S0137_SCI_15_
    | | | | | | |____idwrgnN20100401S0137_SCI_16_
    | | | | | | |____idwrgnN20100401S0137_SCI_17_
    | | | | | | |____idwrgnN20100401S0137_SCI_18_
    | | | | | | |____idwrgnN20100401S0137_SCI_19_
    | | | | | | |____idwrgnN20100401S0137_SCI_1_
    | | | | | | |____idwrgnN20100401S0137_SCI_20_
    | | | | | | |____idwrgnN20100401S0137_SCI_21_
    | | | | | | |____idwrgnN20100401S0137_SCI_22_
    | | | | | | |____idwrgnN20100401S0137_SCI_23_
    | | | | | | |____idwrgnN20100401S0137_SCI_24_
    | | | | | | |____idwrgnN20100401S0137_SCI_25_
    | | | | | | |____idwrgnN20100401S0137_SCI_26_
    | | | | | | |____idwrgnN20100401S0137_SCI_27_
    | | | | | | |____idwrgnN20100401S0137_SCI_28_
    | | | | | | |____idwrgnN20100401S0137_SCI_29_
    | | | | | | |____idwrgnN20100401S0137_SCI_2_
    | | | | | | |____idwrgnN20100401S0137_SCI_3_
    | | | | | | |____idwrgnN20100401S0137_SCI_4_
    | | | | | | |____idwrgnN20100401S0137_SCI_5_
    | | | | | | |____idwrgnN20100401S0137_SCI_6_
    | | | | | | |____idwrgnN20100401S0137_SCI_7_
    | | | | | | |____idwrgnN20100401S0137_SCI_8_
    | | | | | | |____idwrgnN20100401S0137_SCI_9_
    | | | | | |____fbrsnN20100401S0138.fits
    | | | | | |____fbrsnN20100401S0140.fits
    | | | | | |____fbrsnN20100401S0142.fits
    | | | | | |____fbrsnN20100401S0144.fits
    | | | | | |____fbrsnN20100401S0146.fits
    | | | | | |____final_tel_no_hlines_no_normK.fits
    | | | | | |____finalcorrectionspectrum
    | | | | | |____gnN20100401S0139.fits
    | | | | | |____gxtfbrsnN20100401S0138.fits
    | | | | | |____N20100401S0138.fits
    | | | | | |____N20100401S0139.fits
    | | | | | |____N20100401S0140.fits
    | | | | | |____N20100401S0141.fits
    | | | | | |____N20100401S0142.fits
    | | | | | |____N20100401S0143.fits
    | | | | | |____N20100401S0144.fits
    | | | | | |____N20100401S0145.fits
    | | | | | |____N20100401S0146.fits
    | | | | | |____nifs.log
    | | | | | |____nN20100401S0138.fits
    | | | | | |____nN20100401S0139.fits
    | | | | | |____nN20100401S0140.fits
    | | | | | |____nN20100401S0141.fits
    | | | | | |____nN20100401S0142.fits
    | | | | | |____nN20100401S0143.fits
    | | | | | |____nN20100401S0144.fits
    | | | | | |____nN20100401S0145.fits
    | | | | | |____nN20100401S0146.fits
    | | | | | |____rgnN20100410S0375.fits
    | | | | | |____rsnN20100401S0138.fits
    | | | | | |____rsnN20100401S0140.fits
    | | | | | |____rsnN20100401S0142.fits
    | | | | | |____rsnN20100401S0144.fits
    | | | | | |____rsnN20100401S0146.fits
    | | | | | |____scienceMatchedTellsList
    | | | | | |____skyframelist
    | | | | | |____snN20100401S0138.fits
    | | | | | |____snN20100401S0140.fits
    | | | | | |____snN20100401S0142.fits
    | | | | | |____snN20100401S0144.fits
    | | | | | |____snN20100401S0146.fits
    | | | | | |____std_star.txt
    | | | | | |____tell_nolinesK.fits
    | | | | | |____tellist
    | | | | | |____telluric_hlines.txt
    | | | | | |____telluricfile
    | | | | | |____tfbrsnN20100401S0138.fits
    | | | | | |____tfbrsnN20100401S0140.fits
    | | | | | |____tfbrsnN20100401S0142.fits
    | | | | | |____tfbrsnN20100401S0144.fits
    | | | | | |____tfbrsnN20100401S0146.fits
    | | | | | |____wrgnN20100401S0137.fits
    | | | | | |____xtfbrsnN20100401S0138.fits
    | | | | | |____xtfbrsnN20100401S0140.fits
    | | | | | |____xtfbrsnN20100401S0142.fits
    | | | | | |____xtfbrsnN20100401S0144.fits
    | | | | | |____xtfbrsnN20100401S0146.fits
    | | | | |____PRODUCTS
    | |____Merged
    | | |____20100401_obs107
    | | | |____20100401_obs107_merged.fits
    | | | |____cptfbrsnN20100401S0182.fits
    | | | |____cptfbrsnN20100401S0184.fits
    | | | |____cptfbrsnN20100401S0186.fits
    | | | |____cptfbrsnN20100401S0188.fits
    | | | |____cptfbrsnN20100401S0190.fits
    | | | |____cube_merged.fits
    | | | |____NONtranscube182.fits
    | | | |____NONtranscube184.fits
    | | | |____NONtranscube186.fits
    | | | |____NONtranscube188.fits
    | | | |____NONtranscube190.fits
    | | | |____offsets.txt
    | | |____20100401_obs107_merged.fits
    |____LICENSE
    |____nifsBaselineCalibration.py
    |____nifsBaselineCalibration.pyc
    |____nifsDefs.py
    |____nifsDefs.pyc
    |____nifsMerge.py
    |____nifsMerge.pyc
    |____nifsReduce.py
    |____nifsReduce.pyc
    |____nifsSort.py
    |____nifsSort.pyc
    |____Nifty.log
    |____Nifty.py
    |____README.rst
    |____recipes
    | |____just_merge.json
    |____runtimeData
    | |____calibrationDirectoryList.txt
    | |____default_input.json
    | |____h_test_one_argon.dat
    | |____j_test_one_argon.dat
    | |____k_test_two_argon.dat
    | |____new_starstemp.txt
    | |____scienceDirectoryList.txt
    | |____telluricDirectoryList.txt
    | |____user_options.json
    | |____vega_ext.fits
    |____unitTests
    | |____generate_response_curve.py
    | |____hk.txt
    | |____nftelluric_modified.cl


The End
-------


.. Just a placeholder comment
