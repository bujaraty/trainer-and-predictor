import unittest
import os
import combivep.template as main_template
import combivep.settings as combivep_settings


class SafeGeneralTester(main_template.SafeTester):
    """ General template for "utils" testing """


    def __init__(self, test_name):
        main_template.SafeTester.__init__(self, test_name)

    def set_dir(self):
        self.working_dir = os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'tmp'), self.test_class), self.test_function)
        self.data_dir    = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), self.test_class)


class RiskyGeneralTester(main_template.RiskyTester):
    """ General template for "utils" testing """


    def __init__(self, test_name):
        main_template.RiskyTester.__init__(self, test_name)

    def set_dir(self):
        self.working_dir = combivep_settings.COMBIVEP_WORKING_DIR
        self.data_dir    = os.path.join(os.path.join(os.path.dirname(__file__), 'big_data'), self.test_class)





