import unittest
import os
import filecmp
import combivep.test.template as template
import combivep.settings as combivep_settings
import combivep.cfg as combivep_cfg


class TestConfigure(template.RiskyGeneralTester):


    def __init__(self, test_name):
        template.RiskyGeneralTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'configure'
        self.remove_user_dir()

    def init_configure_instance(self):
        self.__configure = combivep_cfg.Configure()

    def test_initial(self):
        #init
        self.individual_debug = True
        self.init_test('test_initial')
        self.init_configure_instance()
        #test nonexistent file
        self.__configure.write_ljb_config('1.3', '/home/jessada/development/scilifelab/projects/CombiVEP/combivep/data/LJB/dbNSFP_light1.3')
        expected_out_file1 = os.path.join(self.data_dir, 'expected_update_initial_config_output1.txt')
        self.assertTrue(filecmp.cmp(combivep_settings.COMBIVEP_CONFIGURATION_FILE, expected_out_file1), "Configure cannot update nonexistent config file correctly")
        #test if it can be made into the complete one
        self.__configure.write_ucsc_config('137', '/home/jessada/development/scilifelab/projects/CombiVEP/combivep/data/UCSC/snp137.txt.gz')
        expected_out_file2 = os.path.join(self.data_dir, 'expected_update_initial_config_output2.txt')
        self.assertTrue(filecmp.cmp(combivep_settings.COMBIVEP_CONFIGURATION_FILE, expected_out_file2), "Configure cannot update nonexistent config file into the complete one")

    def tearDown(self):
        self.remove_working_dir()
        pass

