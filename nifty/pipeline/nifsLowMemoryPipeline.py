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

import logging, os, sys, shutil, pkg_resources, argparse, glob
from datetime import datetime

# LOCAL

# Import major Nifty scripts.
import steps.nifsSort as nifsSort
import steps.nifsBaselineCalibration as nifsBaselineCalibration
import steps.nifsReduce as nifsReduce
import nifsUtils as nifsUtils
# Import config parsing.
# Import config parsing.
from configobj.configobj import ConfigObj
from objectoriented.getConfig import GetConfig
# Import custom Nifty functions.
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
    # Save path for later use and change one directory up.
    path = os.getcwd()

    # Get paths to Nifty data.
    RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
    RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

    # Format logging options.
    FORMAT = '%(asctime)s %(message)s'
    DATEFMT = datefmt()

    # Set up the logging file.
    logging.basicConfig(filename='Nifty.log',format=FORMAT,datefmt=DATEFMT,level=logging.DEBUG)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # This lets us logging.info(to stdout AND a logfile. Cool, huh?
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logging.info("\nWARNING: This pipeline is untested and needs revision.")
    # TODO(nat): revise this pipeline.

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

    # Read or write a configuration file, interactively or from some defaults.
    # Second argument is the name of the current script. Used to get script-dependent configuration.
    GetConfig(args, "nifsPipeline")

    # TODO(nat): fix this. It isn't recursively printing the dictionaries of values.
    logging.info("\nParameters for this data reduction as read from ./config.cfg:\n")
    with open('./config.cfg') as config_file:
        config = ConfigObj(config_file, unrepr=True)
        for i in config:
            logging.info(str(i) + " " + str(config[i]))
    logging.info("")

    # Load configuration from ./config.cfg that is used by this script.
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

    with open('./config.cfg') as config_file:
        # Load general config.
        config = ConfigObj(config_file, unrepr=True)
        scienceDirectoryList = config['scienceDirectoryList']

    # This mode does a full reduction, science observation by science observation.
    # For each science directory in science directory list:
    # Reduce the associated calibrations
    # Reduce the associated tellurics
    # Reduce the science observation
    for scienceObservation in scienceDirectoryList:
        # Find associated calibrations by looping through calibration directory list.
        # Split to this form: ('/Users/nat/tests/core/M85/20150508/J', 'obs36')
        temp = os.path.split(scienceObservation)
        # Split again to this form: ('/Users/nat/tests/core/M85/20150508', 'J')
        temp2 = os.path.split(temp[0])
        # Now temp[0] is calibation base path name, temp[1] is grating.
        calibrationDirectory = temp2[0]+"/Calibrations_"+temp2[1]
        # Have to convert it to a one-element list first.
        calibrationDirectory = [calibrationDirectory]
        # We now have our calibration directory for the given science!
        # Now find associated telluric observations.
        # temp[0] looks like: '/Users/nat/tests/core/M85/20150508/J'
        telluricBaseName = temp[0]+"/Tellurics/"
        os.chdir(telluricBaseName)
        telluricDirectoryList = glob.glob("obs*")
        # We must make these incomplete paths into full paths by adding the base path.
        telluricDirectoryList = [telluricBaseName+x for x in telluricDirectoryList]
        # Don't forget to change back to starting point.
        os.chdir(path)

        ###########################################################################
        ##                STEP 2: Reduce baseline calibrations.                  ##
        ###########################################################################

        if calibrationReduction:
            if manualMode:
                a = raw_input('About to enter nifsBaselineCalibration.')
            nifsBaselineCalibration.start(calibrationDirectoryList=calibrationDirectory)

        ###########################################################################
        ##                STEP 3: Reduce telluric observations.                  ##
        ###########################################################################

        if telluricReduction:
            if manualMode:
                a = raw_input('About to enter nifsReduce to reduce Tellurics.')
            nifsReduce.start('Telluric', telluricDirectoryList=telluricDirectoryList)

        ###########################################################################
        ##                 STEP 4: Reduce science observations.                  ##
        ###########################################################################

        if scienceReduction:
            if manualMode:
                a = raw_input('About to enter nifsReduce to reduce science.')
            nifsReduce.start('Science')

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
