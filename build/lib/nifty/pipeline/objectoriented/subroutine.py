

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
