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
#        self.remove_user_dir()

    def init_configure_instance(self):
        self.__configure = combivep_cfg.Configure()

    def test_initial(self):
        #init
        self.individual_debug = True
        self.init_test('test_initial')
        self.init_configure_instance()
        expected_out_file = os.path.join(self.data_dir, 'expected_update_initial_config_output.txt')
        #run test
        self.__configure.write_ljb_config('1.0', '/home/jessada/development/scilifelab/projects/CombiVEP/combivep/refdb/test/data/ljb_controller/dummy_dbNSFP_light1.4')
        self.assertTrue(filecmp.cmp(combivep_settings.COMBIVEP_CONFIGURATION_FILE, expected_out_file), "Configure cannot update LJB config correctly")

    def tearDown(self):
#        self.remove_working_dir()
        pass

