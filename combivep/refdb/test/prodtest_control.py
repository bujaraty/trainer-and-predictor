import unittest
import sys
import os
import filecmp
import combivep.refdb.test.template as template
import combivep.settings as combivep_settings
import combivep.refdb.control as combivep_control


"""

The purpose of these tests is to test the 'control' module with the environment
close to production environment as much as possible

In many cases, the input files are likely to are huge and be excluded from
application package. So please be awared if the errors said some files
are missing

Due to the enormous size of the input files, usually, the expected results
are only 'runable'

"""


@unittest.skip("temporary disable due to long running time(last test on Dec 20)")
class TestUcscController(template.RiskRefDBTester):


    def setUp(self):
        self.test_class = 'ucsc_controller'

    def init_ucsc_controller_instance(self):
        self.__ucsc_controller = combivep_control.UcscController()

    def test_clean_raw_database(self):
        #initialize variables
        self.individual_debug = True
        self.init_test('test_clean_raw_database')
        self.init_ucsc_controller_instance()
        test_file    = os.path.join(self.data_dir, 'hg19_snp137.txt')
        working_file = os.path.join(combivep_settings.COMBIVEP_WORKING_DIR, 'hg19_snp137.txt')
        out_file     = combivep_settings.TMP_UCSC_CLEAN_DB_FILE
#        print >> sys.stderr, "copying %s to %s . . . . . " % (test_file, working_file)
#        self.copy_file(test_file, working_file)

        self.__ucsc_controller.clean_raw_database(working_file, out_file)
        #self.assertTrue(filecmp.cmp(out_file, expected_out_file), "Raw UCSC database haven't been clean properly");
#        #call function
#        self.__ucsc_controller.raw_db_file   = test_file
#        self.__ucsc_controller.clean_db_file = out_file
#        self.__ucsc_controller.clean_raw_database(test_file, out_file)
#        self.assertTrue(filecmp.cmp(out_file, expected_out_file), "Raw UCSC database haven't been clean properly");
#
#    def test_transform_database(self):
#        #init
##        self.individual_debug = True
#        self.init_test('test_transform_database')
#        self.init_ucsc_controller_instance()
#        test_file    = os.path.join(self.data_dir, 'test_transform.txt')
#        working_file = os.path.join(self.working_dir, 'test_transform.txt')
#        out_file     = os.path.join(self.working_dir, 'test_transform.txt.gz')
#        self.copy_file(test_file, working_file)
##        self.__ucsc_controller.clean_db_file = working_file
##        self.__ucsc_controller.transformed_db_file = out_file
#
#        #test if the 'tabix' files are produced
#        self.__ucsc_controller.transform_database(working_file)
#        self.assertTrue(os.path.exists(out_file), "Tabix doesn't work correctly")
#        self.assertTrue(os.path.exists(out_file+'.tbi'), "Tabix doesn't work correctly")
#
#        #test if it is readable
#        self.__ucsc_controller.read(out_file)
#        for rec in self.__ucsc_controller.fetch_snps('chr3', 138211840, 138212000):
#            self.assertEqual(rec[combivep_settings.KEY_UCSC_START_POS], '138211844', "Database transform doesn't work correctly")
#            break

    def tearDown(self):
        self.remove_working_dir()


@unittest.skip("temporary disable due to long running time(last test on Dec 22 : took around 15 seconds)")
class TestLjbController(template.RiskRefDBTester):


    def setUp(self):
        self.test_class = 'ljb_controller'

    def init_ljb_controller_instance(self):
        self.__ljb_controller = combivep_control.LjbController()

    def test_clean_raw_database(self):
        #initialize variables
        self.individual_debug = True
        self.init_test('test_clean_raw_database')
        self.init_ljb_controller_instance()
        test_file    = os.path.join(self.data_dir, 'dbNSFP_light1.3.chr1')
#        working_file = os.path.join(combivep_settings.COMBIVEP_WORKING_DIR, 'hg19_snp137.txt')
        out_file     = combivep_settings.TMP_LJB_CLEAN_DB_FILE
#        print >> sys.stderr, "copying %s to %s . . . . . " % (test_file, working_file)
#        self.copy_file(test_file, working_file)

        self.__ljb_controller.clean_raw_database(test_file, out_file)
