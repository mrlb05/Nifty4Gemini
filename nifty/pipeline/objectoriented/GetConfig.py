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
# STDLIB

import logging, os, sys, shutil, pkg_resources, argparse
from datetime import datetime

# LOCAL

# Import config parsing.
from ..configobj.configobj import ConfigObj
# Import custom Nifty functions.
from ..nifsUtils import datefmt, printDirectoryLists, writeList, getParam, interactiveNIFSInput

class GetConfig(object):
    """
    A class to get configuration from the command line.

    Configuration for each "Pipeline" and "Step" can come in one of 5 ways:

    - The -i flag is provided. Then, an interactive input session is launched.
    - An input file is provided. Configuration is read from that. Each pipeline and
    step has its own required config file name.
    - The -f flag and either a path or program ID is provided.
    - The -r flag provided. The last data reduction is repeated. (Or resumed?)

    """

    def __init__(self, args, script):
        """Return a getConfig object set up for script that is calling it."""

        # Define constants.
        # Paths to Nifty data.
        self.RECIPES_PATH = pkg_resources.resource_filename('nifty', 'recipes/')
        self.RUNTIME_DATA_PATH = pkg_resources.resource_filename('nifty', 'runtimeData/')

        self.args = args
        self.script = script
        if self.script == "nifsPipeline":
            self.configFile = "config.cfg"

        self.makeConfig()

    def makeConfig(self):
        """
        Make a configuration file.
        """

        # TODO(nat): This is really messy, and could probably be split up better. Find a better way.
        # Parse command line options.
        self.parser = argparse.ArgumentParser(description='Do a Gemini NIFS data reduction.')
        # Create a configuration file interactively
        self.parser.add_argument('-i', '--interactive', dest = 'interactive', default = False, action = 'store_true', help = 'Create a config.cfg file interactively.')
        # Ability to repeat the last data reduction
        self.parser.add_argument('-r', '--repeat', dest = 'repeat', default = False, action = 'store_true', help = 'Repeat the last data reduction, loading saved reduction parameters from runtimeData/config.cfg.')
        # Ability to load a built-in configuration file (recipe)
        self.parser.add_argument('-l', '--recipe', dest = 'recipe', action = 'store', help = 'Load data reduction parameters from the a provided recipe. Default is default_input.cfg.')
        # Ability to load your own configuration file
        self.parser.add_argument(dest = 'inputfile', nargs='?', action = 'store', help = 'Load data reduction parameters from <inputfile>.cfg.')
        # Ability to do a quick and dirty fully automatic data reduction with no user input
        self.parser.add_argument('-f', '--fullReductionPathOrProgramID', dest = 'fullReduction', default = False, action = 'store', help = 'Do a quick reduction from recipes/defaultConfig.cfg, specifying path to raw data or program ID.')

        self.args = self.parser.parse_args(self.args)

        self.interactive = self.args.interactive
        self.repeat = self.args.repeat
        self.fullReduction = self.args.fullReduction
        self.inputfile = self.args.inputfile

        if self.inputfile:
            # Load input from a .cfg file user specified at command line.
            if self.inputfile != self.configFile and os.path.exists('./'+ self.configFile):
                os.remove('./'+ self.configFile)
                shutil.copy(self.inputfile, './'+ self.configFile)
            logging.info("\nPipeline configuration for this data reduction was read from " + str(self.inputfile) + \
            ", and if not named config.cfg, copied to ./config.cfg.")

        # Check if the user specified at command line to repeat the last Reduction, do a full default data reduction from a
        # recipe file or do a full data reduction from a handmade file.
        if self.interactive:
            # Get user input interactively.
            logging.info('\nInteractively creating a ./config.cfg configuration file.')
            self.fullReduction = interactiveNIFSInput()

        if self.fullReduction:
            # Copy default input and use it
            if os.path.exists('./' + self.configFile):
                os.remove('./' + self.configFile)
            shutil.copy(self.RECIPES_PATH+'defaultConfig.cfg', './'+ self.configFile)
            # Update default config file with path to raw data or program ID.
            with open('./' + self.configFile, 'r') as self.config_file:
                self.config = ConfigObj(self.config_file, unrepr=True)
                self.sortConfig = self.config['sortConfig']
                if self.fullReduction[0] == "G":
                    # Treat it as a program ID.
                    self.sortConfig['program'] = self.fullReduction
                    self.sortConfig['rawPath'] = ""
                else:
                    # Else treat it as a path.
                    self.sortConfig['program'] = ""
                    self.sortConfig['rawPath'] = self.fullReduction
            with open('./' + self.configFile, 'w') as self.outfile:
                self.config.write(self.outfile)
            logging.info("\nData reduction parameters for this reduction were copied from recipes/defaultConfig.cfg to ./config.cfg.")
