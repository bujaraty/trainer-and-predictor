import unittest
import os.path
import combivep.template as combivep_template


class GeneralTester(combivep_template.Tester):
    """ General template for "utils" testing """


    def __init__(self, test_name):
        unittest.TestCase.__init__(self, test_name)

    def set_dir(self):
        self.working_dir = os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'tmp'), self.test_class), self.test_function)
        self.data_dir    = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), self.test_class)





