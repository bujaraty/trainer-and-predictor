import unittest
import os
import filecmp
import combivep.refdb.test.template as template
import combivep.settings as combivep_settings
import combivep.refdb.control as combivep_control


class TestUcscController(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'ucsc_controller'

    def init_ucsc_controller_instance(self):
        self.__ucsc_controller = combivep_control.UcscController()

#    def test_clean_raw_database(self):
#        #initialize variables
##        self.individual_debug = True
#        self.init_test('test_clean_raw_database')
#        self.init_ucsc_controller_instance()
#        test_file = os.path.join(self.data_dir, 'test_clean_raw_database.txt')
#        working_file = os.path.join(self.working_dir, 'test_clean_raw_database.txt')
#        out_file  = os.path.join(self.working_dir, 'clean_database.txt')
#        expected_out_file = os.path.join(self.data_dir, 'expected_clean_database.txt')
#        self.copy_file(test_file, working_file)
#
#        self.__ucsc_controller.clean_raw_database(working_file, out_file)
#        self.assertTrue(filecmp.cmp(out_file, expected_out_file), "Raw UCSC database haven't been clean properly");
#
    def test_transform_database(self):
        #init
        self.init_test('test_transform_database')
        self.init_ucsc_controller_instance()
        test_file    = os.path.join(self.data_dir, 'test_transform.txt')
        working_file = os.path.join(self.working_dir, 'test_transform.txt')
        out_file     = os.path.join(self.working_dir, 'test_transform.txt.gz')
        self.copy_file(test_file, working_file)

        #test if the 'tabix' files are produced
        self.__ucsc_controller.transform_database(working_file)
        self.assertTrue(os.path.exists(out_file), "Tabix doesn't work correctly")
        self.assertTrue(os.path.exists(out_file+'.tbi'), "Tabix doesn't work correctly")

        #test if it is readable
        self.__ucsc_controller.read(out_file)
        readable = False
        for rec in self.__ucsc_controller.fetch_array_snps('chr3', 108572604, 108572605):
            readable = True
            self.assertEqual(rec[combivep_settings.UCSC_0_INDEX_START_POS], '108572604', "Database transform doesn't work correctly")
            break
        self.assertTrue(readable, "Transformed ucsc database is not readable")

    def tearDown(self):
        self.remove_working_dir()


class TestLjbController(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'ljb_controller'

    def init_ljb_controller_instance(self):
        self.__ljb_controller = combivep_control.LjbController()

    def test_clean_raw_database(self):
        #initialize variables
#        self.individual_debug = True
        self.init_test('test_clean_raw_database')
        self.init_ljb_controller_instance()
        test_file = os.path.join(self.data_dir, 'test_clean_raw_database.txt')
        out_file  = os.path.join(self.working_dir, 'clean_database.txt')
        expected_out_file = os.path.join(self.data_dir, 'expected_clean_database.txt')

        #call function
#        self.__ljb_controller.raw_db_file   = test_file
#        self.__ljb_controller.clean_db_file = out_file
        self.__ljb_controller.clean_raw_database(test_file, out_file)
        self.assertTrue(filecmp.cmp(out_file, expected_out_file), "Raw LJB database haven't been clean properly");

    def test_transform_database(self):
        #init
        self.init_test('test_transform_database')
        self.init_ljb_controller_instance()
        test_file    = os.path.join(self.data_dir, 'test_transform_database.txt')
        working_file = os.path.join(self.working_dir, 'test_transform_database.txt')
        out_file     = os.path.join(self.working_dir, 'test_transform_database.txt.gz')
        self.copy_file(test_file, working_file)

        #test if the 'tabix' files are produced
        self.__ljb_controller.transform_database(working_file)
        self.assertTrue(os.path.exists(out_file), "Tabix doesn't work correctly")
        self.assertTrue(os.path.exists(out_file+'.tbi'), "Tabix doesn't work correctly")

        #test if it is readable
        self.__ljb_controller.read(out_file)
        readable = False
        for rec in self.__ljb_controller.fetch_array_snps('3', 108549516, 108549517): #to be tested again
            readable = True
            self.assertEqual(rec[combivep_settings.LJB_PARSED_0_INDEX_START_POS], '108549517', "Database transform doesn't work correctly")
            break
        self.assertTrue(readable, "Transformed ljb database is not readable")

    def tearDown(self):
        self.remove_working_dir()






