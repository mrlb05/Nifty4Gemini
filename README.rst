Nifty4Gemini
============
.. image:: https://badge.fury.io/py/nifty4gemini.svg
   :target: https://badge.fury.io/py/nifty4gemini
.. image:: https://readthedocs.org/projects/nifty4gemini/badge/?version=latest
   :alt: Nifty4Gemini's documentation, hosted on ReadtheDocs.
   :target: http://nifty4gemini.readthedocs.io/en/latest/
.. image:: https://zenodo.org/badge/103719389.svg
   :alt: DOI
   :target: https://zenodo.org/badge/latestdoi/103719389
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :alt: MIT license.
   :target: https://opensource.org/licenses/MIT
.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
   :alt: Nifty4Gemini uses Astropy! Here is a link to the project webpage:
   :target: http://www.astropy.org/

A Python Data Reduction Pipeline for the Gemini-North Near-Infrared Integral
Field Spectrometer (NIFS).

Full documentation: `ReadTheDocs <http://nifty4gemini.readthedocs.io/en/latest/>`_.

This is a new data reduction Python pipeline that uses Astroconda and the Gemini
IRAF Package to reduce NIFS data. It offers a complete data reduction process from
sorting the data to producing a final flux calibrated and wavelength calibrated
combined cube with the full S/N for a science target.

This pipeline is open source and it is supported via the `Gemini Data Reduction User Forum <http://drforum.gemini.edu/>`_.

Any feedback and comments (mbusserolle@gemini.edu) are welcome!

Copyright
---------

For more details, please read the LICENSE.


How to Submit Bugs and Requests
-------------------------------

Very important: **do not submit a Gemini help desk ticket!**

If you want to report a problem, use the `Gemini Data Reduction Forum thread <http://drforum.gemini.edu/topic/nifs-python-data-reduction-pipeline/>`_
or create an issue in this repo.

Installation
============

Pre-Requisites
--------------
Make sure you have the latest version of Gemini Astroconda installed, have activated an Astroconda environment and have set up PYRAF.
You can find instructions for installing Astroconda `here <https://astroconda.readthedocs.io/en/latest/>`_. PYRAF can be set up by running the mkiraf command
in your "~/iraf" directory.

Installing
----------
From PyPi.org:

.. code-block:: text

    pip install nifty4gemini

Installing in Editable Mode
---------------------------
If you want to edit the Nifty source code, it's recommended to install Nifty in editable Mode. First obtain the Nifty source code. You
can do this by downloading and unpacking the latest release or cloning this github repository.

Once you have the source code, change to the top level of the source code directory (you should see the setup.py file). Run:

.. code-block:: text

    pip install -e .

to install Nifty in editable mode. Now you can edit your copy of the Nifty source code and run it without having to reinstall every time.

Quick Start
===========

To run Nifty4Gemini, getting data reduction parameters from an interactive input session:

.. code-block:: text

   runNifty nifsPipeline -i

To run Nifty in full-automatic mode with default input parameters, provide the -f flag
and a full local path to the raw data or a Gemini Program ID string (Eg: GN-2013A-Q-62).

.. code-block:: text

   runNifty nifsPipeline -f <data_location>


License
=======

See the LICENSE file in the current directory. Note that downloadFromGeminiPublicArchive does not use the MIT
license. Refer to the LICENCE file in the downloadFromGeminiPublicArchive directory to view the appropriate license.
