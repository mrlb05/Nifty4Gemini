#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#                Import some useful Python utilities/modules                   #
################################################################################

# STDLIB

import argparse
import logging, os, sys, shutil, pkg_resources
from datetime import datetime

# LOCAL

# Import major Nifty scripts.
import nifsSort as nifsSort
import nifsBaselineCalibration as nifsBaselineCalibration
import nifsReduce as nifsReduce
import nifsUtils as nifsUtils
# Import config parsing.
from configobj.configobj import ConfigObj
# Import custom Nifty functions.
from nifsUtils import datefmt, printDirectoryLists, writeList, getParam, getUserInput

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

# Welcome to Nifty, the nifs data reduction pipeline!

# The current version:
# TODO(nat): fix this to work as a proper package. This should not be hardcoded.
__version__ = "1.0.0"

# The time when Nifty was started is:
startTime = str(datetime.now())

def start(args):
    """

    NIFTY

    This script launches a nifs data reduction.

    It does two things; it:
        - gets data reduction parameters; either from an interactive input session or
          an input file
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
    logging.info('The log file is Nifty.log.\n')

    # Parse command line options.
    parser = argparse.ArgumentParser(description='Do a Gemini NIFS data reduction.')
    # Ability to repeat the last data reduction
    parser.add_argument('-r', '--repeat', dest = 'repeat', default = False, action = 'store_true', help = 'Repeat the last data reduction, loading parameters from runtimeData/config.cfg.')
    # Ability to load a built-in configuration file (recipe)
    parser.add_argument('-l', '--recipe', dest = 'recipe', action = 'store', help = 'Load data reduction parameters from the a provided recipe. Default is default_input.cfg.')
    # Ability to load your own configuration file
    parser.add_argument(dest = 'inputfile', action = 'store', help = 'Load data reduction parameters from <inputfile>.cfg.')
    # Ability to do a quick and dirty fully automatic data reduction with no user input
    # TODO(nat): make it so Nifty does this when you type "niftyRun" with no options
    parser.add_argument('-f', '--fullReduction', dest = 'fullReduction', default = False, action = 'store_true', help = 'Do a full reduction with data reduction parameters loaded from runtimeData/default_input.cfg')

    args = parser.parse_args(args)

    repeat = args.repeat
    fullReduction = args.fullReduction
    inputfile = args.inputfile

    # Check if the user specified at command line to repeat the last Reduction, do a full default data reduction from a
    # recipe file or do a full data reduction from a handmade file.
    if not repeat and not fullReduction and not inputfile:
        # If not get user input and check if user specified a full data reduction.
        fullReduction = getUserInput()

    # TODO(nat): Add proper documentation on supplying an input file name (the args option here).
    if fullReduction:
        # TODO(nat): move this code to a function.
        # Read and use parameters of the last Reduction from runtimeData/config.cfg.
        shutil.copy(RECIPES_PATH+'default_input.cfg', RUNTIME_DATA_PATH+'config.cfg')
        logging.info("\nData reduction parameters for this reduction were copied from recipes/default_input.cfg to runtimeData/config.cfg.")

    if inputfile:
        # Load input from a .cfg file user specified at command line.
        shutil.copy('./'+inputfile, RUNTIME_DATA_PATH+'config.cfg')
        logging.info("\nPipeline configuration for this data reduction was read from " + str(inputfile) + \
        " and copied to ./config.cfg.")
    else:
        shutil.copy(RUNTIME_DATA_PATH+'config.cfg', './config.cfg')
        logging.info("\nPipeline configuration for this data reduction has been written to ./config.cfg")

    # Print data reduction parameters for a user's peace-of-mind.
    logging.info("\nParameters for this data reduction as read from that file:\n")
    with open('./config.cfg') as config_file:
        options = ConfigObj(config_file, unrepr=True)
        for i in options:
            logging.info(str(i) + " " + str(options[i]))
    logging.info("")

    # Define parameters used by this script:
    with open('./config.cfg') as config_file:
        options = ConfigObj(config_file, unrepr=True)
        sort = options['sort']
        calibrationReduction = options['calibrationReduction']
        telluricReduction = options['telluricReduction']
        scienceReduction = options['scienceReduction']
        debug = options['debug']

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
        if debug:
            a = raw_input('About to enter sort.')
        nifsSort.start()
    printDirectoryLists()

    ###########################################################################
    ##                STEP 2: Reduce baseline calibrations.                  ##
    ###########################################################################

    if calibrationReduction:
        if debug:
            a = raw_input('About to enter calibrate.')
        nifsBaselineCalibration.start()

    ###########################################################################
    ##                STEP 3: Reduce telluric observations.                  ##
    ###########################################################################

    if telluricReduction:
        if debug:
            a = raw_input('About to enter reduce to reduce Telluric images, create telluric correction spectrum and blackbody spectrum.')
        nifsReduce.start('Telluric')

    ###########################################################################
    ##                 STEP 4: Reduce science observations.                  ##
    ###########################################################################

    if scienceReduction:
        if debug:
            a = raw_input('About to enter reduce to reduce science images.')
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
    logging.info('#   For docs, recipes and examples.     #')
    logging.info('#                                       #')
    logging.info('#########################################')

    return

if __name__ == '__main__':
    # If running ./nifsPipeline or python nifsPipeline.py, call start.
    #Currently broken... Have to supply options somehow!
    #start()
    pass
