import unittest
import os.path
import combivep.template as combivep_template


class UtilsTester(combivep_template.Tester):
    """ General template for "utils" testing """


    def __init__(self, test_name):
        unittest.TestCase.__init__(self, test_name)

    def init_test(self, test_function):
        self.working_dir = os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'tmp'), self.test_class), test_function)
        self.data_dir    = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), self.test_class)

        self.empty_working_dir()



class SafeUtilsTester(UtilsTester):
    """

    General template for "utils" testing
    that can be run in both dev and production environment
    The purpose of this template is to test general functionality

    """


    def __init__(self, test_name):
        unittest.TestCase.__init__(self, test_name)


class RiskUtilsTester(UtilsTester):
    """

    General template for "utils" testing
    that can be run only in dev environment

    The purpose of this template is to test
    if the modules can function properly in real environment

    """


    def __init__(self, test_name):
        unittest.TestCase.__init__(self, test_name)


