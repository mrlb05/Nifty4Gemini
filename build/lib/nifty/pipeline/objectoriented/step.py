


class Routine(object):
    """
    A step is a way to chain multiple routines together.
    """

    def start(self):
        a = False
        while not a:
            print "entering " + str(task)
            self.doStep()
            a = raw_input("Pausing. Check that results are satisfactory for you.")

    def doTask(self, input_tasks):
        for i in input_tasks:
            input_tasks[i].run()
