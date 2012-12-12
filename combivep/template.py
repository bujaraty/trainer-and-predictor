import unittest
import os.path




class Tester(unittest.TestCase):
    """ CombiVEP template for testing """


    def __init__(self, test_name):
        unittest.TestCase.__init__(self, test_name)

    def get_root_data_dir(self, __file):
        """

        It's 'root' because several module gonna use this folder as well.
        To use this function properly, the caller module has to create their
        own sub-folders

        """
        return os.path.join(os.path.dirname(__file), 'data')

    def get_root_working_dir(self, __file):
        """

        It's 'root' because several module gonna use this folder as well.
        To use this function properly, the caller module has to create their
        own sub-folders

        """
        return os.path.join(os.path.dirname(__file), 'tmp')

