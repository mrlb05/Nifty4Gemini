#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MIT License

# Copyright (c) 2015, 2017 Marie Lemoine-Busserolle

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

################################################################################
#                Import some useful Python utilities/modules                   #
################################################################################

# STDLIB

import logging, os, sys, shutil, pkg_resources, argparse
from datetime import datetime

# LOCAL

# Import major Nifty Steps.
import steps.nifsSort as nifsSort
import steps.nifsBaselineCalibration as nifsBaselineCalibration
import steps.nifsReduce as nifsReduce
import steps.nifsTelluric as nifsTelluric
import steps.nifsFluxCalibrate as nifsFluxCalibrate
import steps.nifsMerge as nifsMerge
# Import nifs utilities module.
import nifsUtils as nifsUtils
# Import configuration file parsing.
from configobj.configobj import ConfigObj
# Import custom pipeline setup Class.
from objectoriented.getConfig import GetConfig
# Conveniently import some utility functions so we don't have to type the full name.
from nifsUtils import datefmt, printDirectoryLists, writeList, getParam, interactiveNIFSInput

#                                +
#
#
#
#              +
#         +         +         +
#
#                     +      +
#
#
#      +       +   + + + + +    + + + +  + + + + +   +    +
#     + +     +       +        +            +         + +
#    +   +   +       +        + +          +           +
#   +     + +       +        +            +           +
#  +       +   + + + + +    +            +           +
#
#
#                                      +
#                                   +     +
#                                       +
#                                      +
#

# Welcome to Nifty.

# The current version:
# TODO(nat): fix this to import the version from setup.py.
__version__ = "1.0.0"

# The time when Nifty was started is:
startTime = str(datetime.now())

def start(args):
    """

    nifsPipeline

    This script is a full-featured NIFS data reduction pipeline. It can call up
    to three "Steps".

    This script does two things. It:
        - gets data reduction parameters; either from an interactive input session or
          an input file, and
        - launches appropriate scripts to do the work. It can call up to 3 scripts directly:
                1) nifsSort.py
                2) nifsBaselineCalibration.py
                3) nifsReduce.py

    """
    # Save starting path for later use and change one directory up.
    path = os.getcwd()

    # Get paths to built-in Nifty data. Special code in setup.py makes sure recipes/ and
    # runtimeData/ will be installed when someone installs Nifty, and accessible in this way.
    RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
    RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

    # Format logging options.
    FORMAT = '%(asctime)s %(message)s'
    DATEFMT = datefmt()

    # Set up the main logging file.
    logging.basicConfig(filename='Nifty.log',format=FORMAT,datefmt=DATEFMT,level=logging.DEBUG)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # This lets us logging.info(to stdout AND a logfile. Cool, huh?
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logging.info("\n####################################")
    logging.info("#                                  #")
    logging.info("#             NIFTY                #")
    logging.info("#   NIFS Data Reduction Pipeline   #")
    logging.info("#         Version "+ __version__+ "            #")
    logging.info("#         July 25th, 2017          #")
    logging.info("#     Marie Lemoine-Busserolle     #")
    logging.info("# Gemini Observatory, Hilo, Hawaii #")
    logging.info("#                                  #")
    logging.info("####################################\n")

    # Make sure to change this if you change the default logfile.
    logging.info('The log file is Nifty.log.')

    # Read or write a configuration file, interactively, from defaults or from a provided file.
    # Second argument is the name of the current script. This could be used to get script-dependent configuration.
    GetConfig(args, "nifsPipeline")

    # TODO(nat): fix this. It isn't recursively printing the dictionaries of values.
    logging.info("\nParameters for this data reduction as read from ./config.cfg:\n")
    with open('./config.cfg') as config_file:
        config = ConfigObj(config_file, unrepr=True)
        for i in config:
            logging.info(str(i) + " " + str(config[i]))
    logging.info("")

    # Load pipeline configuration from ./config.cfg that is used by this script.
    with open('./config.cfg') as config_file:
        # Load general config.
        config = ConfigObj(config_file, unrepr=True)
        manualMode = config['manualMode']

        # Load pipeline specific config.
        nifsPipelineConfig = config['nifsPipelineConfig']

        sort = nifsPipelineConfig['sort']
        calibrationReduction = nifsPipelineConfig['calibrationReduction']
        telluricReduction = nifsPipelineConfig['telluricReduction']
        scienceReduction = nifsPipelineConfig['scienceReduction']
        telluricCorrection = nifsPipelineConfig['telluricCorrection']
        fluxCalibration = nifsPipelineConfig['fluxCalibration']
        merge = nifsPipelineConfig['merge']

    ###########################################################################
    ##                         SETUP COMPLETE                                ##
    ##                      BEGIN DATA REDUCTION                             ##
    ##                                                                       ##
    ##        Four Main Steps:                                               ##
    ##          1) Sort the Raw Data - nifsSort.py                           ##
    ##          2) Reduce baseline calibrations - nifsBaselineCalibration.py ##
    ##          3) Reduce telluric observations - nifsReduce.py              ##
    ##          4) Reduce science observations - nifsReduce.py               ##
    ##                                                                       ##
    ###########################################################################

    ###########################################################################
    ##                      STEP 1: Sort the raw data.                       ##
    ###########################################################################

    if sort:
        if manualMode:
            a = raw_input('About to enter nifsSort.')
        nifsSort.start()
    # By now, we should have paths to the three types of raw data. Print them out.
    printDirectoryLists()

    ###########################################################################
    ##                STEP 2: Reduce baseline calibrations.                  ##
    ###########################################################################

    if calibrationReduction:
        if manualMode:
            a = raw_input('About to enter nifsBaselineCalibration.')
        nifsBaselineCalibration.start()

    ###########################################################################
    ##                STEP 3: Reduce telluric observations.                  ##
    ###########################################################################

    if telluricReduction:
        if manualMode:
            a = raw_input('About to enter nifsReduce to reduce Tellurics.')
        nifsReduce.start('Telluric')

    ###########################################################################
    ##                 STEP 4: Reduce science observations.                  ##
    ###########################################################################

    if scienceReduction:
        if manualMode:
            a = raw_input('About to enter nifsReduce to reduce science.')
        nifsReduce.start('Science')

    if telluricCorrection:
        if manualMode:
            a = raw_input('About to enter nifsTelluric to make and create telluric corrected cubes.')
        nifsTelluric.run()

    if fluxCalibration:
        if manualMode:
            a = raw_input('About to enter nifsFluxCalibrate to make and create flux calibrated and telluric corrected cubes.')
        nifsFluxCalibrate.run()

    if merge:
        if manualMode:
            a = raw_input('About to enter nifsMerge to merge final 3D data cubes to single cubes.')
        nifsMerge.run()

    ###########################################################################
    ##                    Data Reduction Complete!                           ##
    ##                  Good luck with your science!                         ##
    ###########################################################################

    logging.info('#########################################')
    logging.info('#                                       #')
    logging.info('#        DATA REDUCTION COMPLETE        #')
    logging.info('#     Good luck with your science!      #')
    logging.info('#        Check out ??                   #')
    logging.info('#   For docs, tutorials and examples.   #')
    logging.info('#                                       #')
    logging.info('#########################################')

    return

if __name__ == '__main__':
    # This block could let us call start nifsPipeline.py from the command line. It is disabled for now.
    # start(args)
    pass
