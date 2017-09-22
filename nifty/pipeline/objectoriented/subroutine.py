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

class TaskRunner(object):
    """
    Expects:

    inputList: list of raw input files with no prefixes.
    """
    @classmethod
    def loop(self, task, inputList, skipMessage, prefix):
        for item in inputList:
            item = str(item).strip()
            if os.path.exists(item):
                if over:
                    os.remove(item)
                    task.run(item)
                else:
                    logging.info("Output exists and -over- not set - skipping " + str(skipMessage))
            else:
                task.run(item)
        inputList = checkLists(inputList, '.', prefix, '.fits')
        return inputList

    @classmethod
    def combine(self, task, inputList, skipMessage, prefix, output):
        if os.path.exists(output):
            if over:
                iraf.delete(output)
                if len(inputList) > 1:
                    task.run(listit(inputList, prefix))
                else:
                    iraf.copy(inputList[0], output)
            else:
                print "\nOutput exists and -over- not set - skipping " + str(skipMessage)
        else:
            if len(inputList) > 1:
                task.run(listit(inputList,prefix)

    @classmethod
    def single(self, task, inputList, skipMessage, prefix, output):
        if os.path.exists(output):
            if over:
                iraf.delete(output)
                task.run(inputFrame, prefix))
            else:
                print "\nOutput exists and -over- not set - skipping " + str(skipMessage)
        else:
            task.run(inputFrame,prefix)

class Task(object):
    """
    Run like OP OOP!!!
    """
    def __init__(self, input_cls, **kwargs):
        self.input_cls = input_cls
        self.kwargs = kwargs
    def run(self, *args):
        kwargs = self.kwargs
        self.input_cls(*args, **kwargs)

Splot.run()
