import unittest
import os.path




class Tester(unittest.TestCase):
    """ CombiVEP template for testing """


    def __init__(self, test_name):
        unittest.TestCase.__init__(self, test_name)
        self.root_test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

