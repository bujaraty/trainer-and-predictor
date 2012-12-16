import unittest
import os.path
import shutil
import subprocess
import combivep.config as combivep_config


class CombiVEPBase(object):
    """ CombiVEP base class """


    def remove_dir(self, dir_name):
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

    def create_dir(self, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    def copy_file(self, source, destination):
        shutil.copy2(source, destination)


class Tester(unittest.TestCase, CombiVEPBase):
    """ CombiVEP template for testing """
    individual_debug = False


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

    def remove_dir(self, dir_name):
        self.assertTrue(dir_name, '"None" is not a valid directory')
        CombiVEPBase.remove_dir(self, dir_name)

    def create_dir(self, dir_name):
        self.assertTrue(dir_name, '"None" is not a valid directory')
        CombiVEPBase.create_dir(self, dir_name)

    def empty_working_dir(self):
        if (not combivep_config.DEBUG_MODE) and (not self.individual_debug):
            self.remove_dir(self.working_dir)
        self.create_dir(self.working_dir)

    def remove_working_dir(self):
        if (not combivep_config.DEBUG_MODE) and (not self.individual_debug):
            self.remove_dir(self.working_dir)

