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


class Routine(object):
    """
    """

    def __init__(self, name, subroutines):
        """

        """
        self.name = name
        # class, arguments tuple
        self.subroutines = subroutines
        checkOverwrite()
        run()

    def doSingle(self, subroutine):
        """
        Run a given subroutine, abstracting away the busywork of overwriting, checking output,
        and writing output files.
        """
        checkOverwrite()
        subroutine.run()
        checkOutput()


    def doLoop(self, inputList, subroutine):
        """
        Do a subroutine, looping over multiple input.

        """
        for inputFile in inputList:


    def checkOutput():
        pass





class MakeFlat(Routine):
    """
    """

    def run(self):
        """
        """
        flatlist = readFile("flatlist")
        flatdarklist = readFile("flatdarklist")
        # Run nfprepare on everything in flatlist.
        doLoop(flatlist,
            Prepare(),
            (rawpath='.',shiftim="s"+calflat, fl_vardq='yes', fl_corr='no',fl_nonl='no', logfile=log))
        )

        # Run nfprepare on everything in flatdarklist.
        doLoop(flatdarklist,
            Prepare(rawpath='.',shiftim="s"+calflat, fl_vardq='yes',fl_corr='no',fl_nonl='no', logfile=log)
        )

        doSingle(
            Combine(listit(flatlist, "n"), output="gn"+calflat,fl_dqpr='yes', fl_vardq='yes',masktype="none",logfile=log)
        )

        doSingle(
            Combine(listit(flatdarklist, "n"),output="gn"+flatdark,fl_dqpr='yes', fl_vardq='yes',masktype="none",logfile=log)
        )

        doSingle(
            Reduce("gn"+calflat,fl_cut='yes',fl_nsappw='yes',fl_vardq='yes', fl_sky='no',fl_dark='no',fl_flat='no',logfile=log)
        )
        doSingle(
            Reduce("gn"+flatdark,fl_cut='yes',fl_nsappw='yes',fl_vardq='yes', fl_sky='no',fl_dark='no',fl_flat='no',logfile=log)
        )

        doSingle(
            Flat("rgn"+calflat,darks="rgn"+flatdark,flatfile="rgn"+calflat+"_sflat", \
                darkfile="rgn"+flatdark+"_dark", fl_save_dark='yes',process="fit", \
                thr_flo=flo,thr_fup=fup, fl_vardq='yes', fl_int=inter, logfile=log )
        )

        doSingle(
            SlitFunction("rgn"+calflat,"rgn"+calflat+"_flat", \
                        flat="rgn"+calflat+"_sflat",dark="rgn"+flatdark+"_dark",combine="median", \
                        order=3,fl_vary='no',logfile=log)
        )









#
