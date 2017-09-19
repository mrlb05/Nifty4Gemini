Nifty
=====
.. image:: https://badge.fury.io/py/nifty4gemini.svg
    :alt: Available on PyPi.
    :target: https://badge.fury.io/py/nifty4gemini
.. image:: https://zenodo.org/badge/93109208.svg
   :alt: DOI of the latest release. See releases.
   :target: https://zenodo.org/record/852696#.WaWmr5PyhMA
.. image:: https://readthedocs.org/projects/nifty4gemini/badge/?version=latest
   :alt: Nifty's documentation, hosted on ReadtheDocs.
   :target: http://nifty4gemini.readthedocs.io/en/latest/
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :alt: MIT license.
   :target: https://opensource.org/licenses/MIT
.. image:: https://badges.frapsoft.com/os/v2/open-source.svg?v=103
   :alt: Nifty is open-source.
   :target: https://github.com/ellerbrock/open-source-badges/
.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
   :alt: Nifty uses Astropy! Here is a link to the project webpage:
   :target: http://www.astropy.org/

*Now in Beta status! Please let us know of any bugs you find on the issues page.*

A Python Data Reduction Pipeline for the Gemini-North Near-Infrared Integral
Field Spectrometer (NIFS).

Full documentation: `ReadTheDocs <http://nifty4gemini.readthedocs.io/en/latest/>`_.

This is a new data reduction Python pipeline that uses Astroconda and the Gemini
IRAF Package to reduce NIFS data. It offers a complete data reduction process from
sorting the data to producing a final flux calibrated and wavelength calibrated
combined cube with the full S/N for a science target.

This pipeline is open source but is not supported by Gemini Observatory.

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

    pip install Nifty4NIFS

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

To run Nifty, getting data reduction parameters from an interactive input session:

.. code-block:: text

   runNifty nifsPipeline -i

To run Nifty in full-automatic mode with default input parameters, provide the -f flag
and a full local path to the raw data or a Gemini Program ID string (Eg: GN-2013A-Q-62).

.. code-block:: text

   runNifty nifsPipeline -f <data_location>
