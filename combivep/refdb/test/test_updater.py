import unittest
import os.path
import combivep.refdb.test.template as template
import combivep.settings as combivep_settings
import combivep.refdb.updater as combivep_updater

DISABLE_HIGH_BANDWIDTH_TEST = 1

class TestDownloader(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'downloader'

    def test_download(self):
        self.init_test('test_download')
        downloader  = combivep_updater.Downloader()
        target_url  = 'http://dbnsfp.houstonbioinformatics.org/dbNSFPzip/dbNSFP_light_v1.3.readme.txt'
        target_file = os.path.join(self.working_dir, os.path.basename(target_url))
        downloader.download(target_url, self.working_dir)
        self.assertGreater(os.stat(target_file).st_size, 3397, msg='Download does not functional properly')

    def tearDown(self):
        self.remove_working_dir()


class TestUpdater(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'updater'

    def test_ready1(self):
        self.init_test('test_ready1')
        updater = combivep_updater.Updater(working_dir=self.working_dir)
        self.assertEqual(updater.check_new_file('135'), None, msg='Something went wrong in checking if the updater is ready to work')

    def test_ready2(self):
        self.init_test('test_ready2')
        updater = combivep_updater.Updater(working_dir=self.working_dir)
        updater.folder_url      = 'http://dummy_url'
        updater.version_pattern = 'dummy_version_pattern'
        self.assertFalse(updater.check_new_file('135'), msg='Something went wrong in checking if the updater is ready to work')

    def test_ready3(self):
        self.init_test('test_ready3')
        updater = combivep_updater.Updater(working_dir=self.working_dir)
        updater.files_pattern   = r"""href="(?P<file_name>snp\d{3}.sql)">.*>.*(?P<date>\d{2}-[a-zA-Z]{3}-\d{4})"""
        updater.version_pattern = 'dummy_version_pattern'
        self.assertFalse(updater.check_new_file('135'), msg='Something went wrong in checking if the updater is ready to work')

    def tearDown(self):
        self.remove_working_dir()


@unittest.skipIf(DISABLE_HIGH_BANDWIDTH_TEST, "temporary disable due to high bandwidth usage")
class TestUcscUpdater(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'ucsc_updater'

    def init_ucsc_updater_instance(self):
        self.__ucsc_updater                  = combivep_updater.UcscUpdater(working_dir=self.working_dir)
        self.__ucsc_updater.files_pattern    = r"""href="(?P<file_name>snp\d{3}.sql)">.*>.*(?P<date>\d{2}-[a-zA-Z]{3}-\d{4})"""
        self.__ucsc_updater.tmp_file         = combivep_settings.UCSC_LIST_FILE_NAME
        self.__ucsc_updater.local_ref_db_dir = self.working_dir

    def test_update1(self):
#        self.individual_debug = True
        self.init_test('test_update1')
        self.init_ucsc_updater_instance()
        self.assertTrue(self.__ucsc_updater.check_new_file('135').endswith('.sql'), msg='incorrectly identify updating result')

    def test_update2(self):
        self.init_test('test_update2')
        self.init_ucsc_updater_instance()
        self.assertTrue(self.__ucsc_updater.check_new_file('136').endswith('.sql'), msg='incorrectly identify updating result')

    def test_not_update1(self):
        self.init_test('test_not_update1')
        self.init_ucsc_updater_instance()
        self.assertFalse(self.__ucsc_updater.check_new_file('137'), msg='incorrectly identify updating result')

    def test_not_update2(self):
        self.init_test('test_not_update2')
        self.init_ucsc_updater_instance()
        self.assertFalse(self.__ucsc_updater.check_new_file('138'), msg='incorrectly identify updating result')

    def test_full_update1(self):
        self.init_test('test_full_update1')
        self.init_ucsc_updater_instance()
        new_file = self.__ucsc_updater.check_new_file('135')
        self.assertTrue(new_file.endswith('.sql'), msg='some thing went wrong in UCSC updating process: new file is not the correct file')
        downloaded_file = self.__ucsc_updater.download_new_file()
        self.assertTrue(os.path.exists(downloaded_file), msg='some thing went wrong in UCSC updating process: file %s does not exist' % (downloaded_file))

#    def test_full_update2(self):
#        self.__ucsc_updater.files_pattern = combivep_settings.UCSC_FILES_PATTERN
#        new_file = self.__ucsc_updater.check_new_file('135')
#        self.assertTrue(new_file.endswith('.gz'), msg='some thing went wrong in UCSC updating process: new file is not the correct file')
#        ungz_file = self.__ucsc_updater.download_new_file()
#        self.assertTrue(os.path.exists(ungz_file), msg='"%s" file is missing' % (ungz_file))
#
    def test_parse(self):
        self.init_test('test_parse')
        self.init_ucsc_updater_instance()
        test_file = os.path.join(self.data_dir, 'dummy_ucsc_list_file')
        out       = self.__ucsc_updater.parse(test_file)
        self.assertEqual(out['135'], 'snp135.sql', msg='UCSC parser does not work correctly in finding UCSC files')

    def tearDown(self):
        self.remove_working_dir()


class TestLJBUpdater(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'ljb_updater'

    def init_ljb_updater_instance(self):
        self.__ljb_updater                  = combivep_updater.LjbUpdater(working_dir=self.working_dir)
        self.__ljb_updater.files_pattern    = r"""href="(?P<file_name>dbNSFPv[\d.]*.readme.txt)">"""
        self.__ljb_updater.tmp_file         = combivep_settings.LJB_LIST_FILE_NAME
        self.__ljb_updater.local_ref_db_dir = self.working_dir

    def test_update1(self):
        self.init_test('test_update1')
        self.init_ljb_updater_instance()
        self.assertTrue(self.__ljb_updater.check_new_file('1.2'), msg='incorrectly identify updating result')

    def test_not_update1(self):
        self.init_test('test_not_update1')
        self.init_ljb_updater_instance()
        self.assertFalse(self.__ljb_updater.check_new_file('1.3'), msg='incorrectly identify updating result')

    def test_not_update2(self):
        self.init_test('test_not_update2')
        self.init_ljb_updater_instance()
        self.assertFalse(self.__ljb_updater.check_new_file('1.4'), msg='incorrectly identify updating result')

    def test_full_update1(self):
        self.init_test('test_full_update1')
        self.init_ljb_updater_instance()
        new_file = self.__ljb_updater.check_new_file('1.2')
        self.assertTrue(new_file.endswith('.readme.txt'), msg='some thing went wrong in LJB updating process: new file is not the correct file')
        downloaded_file = self.__ljb_updater.download_new_file()
        self.assertTrue(os.path.exists(downloaded_file), msg='some thing went wrong in LJB updating process: file %s does not exist' % (downloaded_file))

#    @unittest.skip("temporary disable due to high bandwidth usage")
#    def test_full_update2(self):
#        self.__ljb_updater.files_pattern = combivep_settings.LJB_FILES_PATTERN
#        new_file = self.__ljb_updater.check_new_file('1.2')
#        self.assertTrue(new_file.endswith('.zip'), msg='some thing went wrong in LJB updating process: new file is not the correct file')
#        unzipped_files = self.__ljb_updater.download_new_file()
#        for unzipped_file in unzipped_files:
#            self.assertTrue(os.path.exists(unzipped_file), msg='"%s" file is missing' % (unzipped_file))

    def test_parse(self):
        self.init_test('test_parse')
        self.init_ljb_updater_instance()
        test_file    = os.path.join(self.data_dir, 'dummy_ljb_list_file')
        out = self.__ljb_updater.parse(test_file)
        self.assertEqual(out['1.3'], 'dbNSFPv1.3.readme.txt', msg='LJB parser does not work correctly in finding LJB files')

    def tearDown(self):
        self.remove_working_dir()


class TestMisc(template.SafeRefDBTester):
    """ test (a few) miscellaneous function(s) """


    def setUp(self):
        self.test_class = 'misc'

    def test_unzip(self):
        self.init_test('test_unzip')
        test_file = os.path.join(self.data_dir, 'dummy_ljb.zip')
        out = combivep_updater.unzip(test_file, self.working_dir)
        self.assertEqual(out[0], os.path.join(self.working_dir, 'try.in'), msg='some files are missing')
        self.assertEqual(out[1], os.path.join(self.working_dir, 'search_dbNSFP_light_v1.3.readme.pdf'), msg='some files are missing')
        self.assertEqual(out[2], os.path.join(self.working_dir, 'search_dbNSFP_light_v1.3.readme.doc'), msg='some files are missing')
        self.assertEqual(out[3], os.path.join(self.working_dir, 'search_dbNSFP_light13.class'), msg='some files are missing')
        self.assertEqual(out[4], os.path.join(self.working_dir, 'dbNSFP_light_v1.3.readme.txt'), msg='some files are missing')
        self.assertEqual(out[5], os.path.join(self.working_dir, 'abc/tryhg19.in'), msg='some files are missing')
        for out_file in out:
            self.assertTrue(os.path.exists(out_file), msg='"%s" file is missing' % (out_file))

    def test_gz(self):
        self.init_test('test_gz')
        test_file    = os.path.join(self.data_dir, 'test_gz.txt.gz')
        working_file = os.path.join(self.working_dir, 'test_gz.txt.gz')
        self.copy_file(test_file, working_file)
        out = combivep_updater.ungz(working_file)
        self.assertTrue(out, 'no output file from "ungz" function')
        self.assertTrue(os.path.exists(out), 'ungz function does not work properly')

    def test_ljb_parse(self):
        self.init_test('test_ljb_parse')
        test_file = os.path.join(self.data_dir, 'test_ljb_parse.txt')
        out_file  = os.path.join(self.working_dir, 'test_ljb_parsed.txt')
        error     = combivep_updater.ljb_parse(test_file, out_file)
        self.assertFalse(error)
        self.assertTrue(os.path.exists(out_file), 'ljb_parsse function does not work properly')

    def tearDown(self):
        self.remove_working_dir()


