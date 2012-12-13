import unittest
import os.path
import glob
import shutil
import combivep.template as combivep_template
import combivep.config as combivep_config
import combivep.utils.refdb as combivep_refdb

@unittest.skipIf(not combivep_config.DEBUG_MODE, "not tested in production mode")
class TestDownloader(combivep_template.Tester):


    def setUp(self):
        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
                                            'downloader')
        if os.path.exists(self.__working_dir):
            shutil.rmtree(self.__working_dir)
        if not os.path.exists(self.__working_dir):
            os.makedirs(self.__working_dir)

    def test_download(self):
        downloader  = combivep_refdb.Downloader()
        target_url  = 'http://dbnsfp.houstonbioinformatics.org/dbNSFPzip/dbNSFP_light_v1.3.readme.txt'
        target_file = os.path.join(self.__working_dir, os.path.basename(target_url))
        downloader.download(target_url, self.__working_dir)
        self.assertGreater(os.stat(target_file).st_size, 3397, msg='Download does not functional properly')

    def tearDown(self):
        if not combivep_config.DEBUG_MODE:
            shutil.rmtree(self.__working_dir)


@unittest.skipIf(not combivep_config.DEBUG_MODE, "not tested in production mode")
class TestUpdater(combivep_template.Tester):


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'updater')
        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
                                            'updater')

    def test_ready1(self):
        updater = combivep_refdb.Updater(working_dir=self.__working_dir)
        self.assertFalse(updater.update('135'), msg='Something went wrong in checking if the updater is ready to work')

    def test_ready2(self):
        updater = combivep_refdb.Updater(working_dir=self.__working_dir)
        updater.folder_url      = combivep_config.UCSC_FOLDER_URL
        updater.version_pattern = combivep_config.UCSC_VERSION_PATTERN
        self.assertFalse(updater.update('135'), msg='Something went wrong in checking if the updater is ready to work')

    def test_ready3(self):
        updater = combivep_refdb.Updater(working_dir=self.__working_dir)
        updater.files_pattern   = r"""href="(?P<file_name>snp\d{3}.sql)">.*>.*(?P<date>\d{2}-[a-zA-Z]{3}-\d{4})"""
        updater.version_pattern = combivep_config.UCSC_VERSION_PATTERN
        self.assertFalse(updater.update('135'), msg='Something went wrong in checking if the updater is ready to work')

    def tearDown(self):
        #clear garbage from tmp directory
        if not combivep_config.DEBUG_MODE:
            shutil.rmtree(self.__working_dir)

        #clear sql (test) file from database directory
        for file_name in os.listdir(combivep_config.COMBIVEP_MASTER_DB_DIR):
            if file_name.endswith('.sql'):
                os.remove(os.path.join(combivep_config.COMBIVEP_MASTER_DB_DIR, file_name))


@unittest.skipIf(not combivep_config.DEBUG_MODE, "not tested in production mode")
class TestUcscUpdater(combivep_template.Tester):


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'ucsc_updater')
        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
                                            'ucsc_updater')
        if not os.path.exists(self.__working_dir):
            os.makedirs(self.__working_dir)
        self.__ucsc_updater               = combivep_refdb.UcscUpdater(working_dir=self.__working_dir)
        self.__ucsc_updater.files_pattern = r"""href="(?P<file_name>snp\d{3}.sql)">.*>.*(?P<date>\d{2}-[a-zA-Z]{3}-\d{4})"""
#        self.__gz_files_pattern  = combivep_config.UCSC_FILES_PATTERN
        self.__ucsc_updater.tmp_file      = combivep_config.UCSC_LIST_FILE_NAME

    def test_update1(self):
        self.assertTrue(self.__ucsc_updater.update('135').endswith('.sql'), msg='incorrectly identify updating result')

    def test_update2(self):
        self.assertTrue(self.__ucsc_updater.update('136').endswith('.sql'), msg='incorrectly identify updating result')

    def test_not_update1(self):
        self.assertFalse(self.__ucsc_updater.update('137'), msg='incorrectly identify updating result')

    def test_not_update2(self):
        self.assertFalse(self.__ucsc_updater.update('138'), msg='incorrectly identify updating result')

    def test_full_update1(self):
        self.__ucsc_updater.update('135')
        sql_file_found = False
        for file_name in os.listdir(self.__ucsc_updater.local_ref_db_dir):
            if file_name.endswith('.sql'):
                sql_file_found = True
        self.assertTrue(sql_file_found, msg='some thing went wrong in LJB updating process')

    def test_full_update2(self):
        #similar to above but with real gz file?
        pass

    def test_parse(self):
        test_file    = os.path.join(self.__test_data_dir, 'dummy_ucsc_list_file')
        out = self.__ucsc_updater.parse(test_file)
        self.assertEqual(out['135'], 'snp135.sql', msg='UCSC parser does not work correctly in finding UCSC files')

    def tearDown(self):
        #clear garbage from tmp directory
        if not combivep_config.DEBUG_MODE:
            shutil.rmtree(self.__working_dir)

        #clear sql (test) file from database directory
        for file_name in os.listdir(combivep_config.COMBIVEP_MASTER_DB_DIR):
            if file_name.endswith('.sql'):
                os.remove(os.path.join(combivep_config.COMBIVEP_MASTER_DB_DIR, file_name))


@unittest.skipIf(not combivep_config.DEBUG_MODE, "not tested in production mode")
class TestLJBUpdater(combivep_template.Tester):


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'ljb_updater')
        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
                                            'ljb_updater')
        if not os.path.exists(self.__working_dir):
            os.makedirs(self.__working_dir)
        self.__ljb_updater               = combivep_refdb.LjbUpdater(working_dir=self.__working_dir)
        self.__ljb_updater.files_pattern = r"""href="(?P<file_name>dbNSFPv[\d.]*.readme.txt)">"""
#        self.__light_files_pattern  = combivep_config.LJB_FILES_PATTERN
        self.__ljb_updater.tmp_file      = combivep_config.LJB_LIST_FILE_NAME

    def test_update1(self):
        self.assertTrue(self.__ljb_updater.update('1.2'), msg='incorrectly identify updating result')

    def test_not_update1(self):
        self.assertFalse(self.__ljb_updater.update('1.3'), msg='incorrectly identify updating result')

    def test_not_update2(self):
        self.assertFalse(self.__ljb_updater.update('1.4'), msg='incorrectly identify updating result')

    def test_full_update1(self):
        self.__ljb_updater.update('1.2')
        readme_file_found = False
        for file_name in os.listdir(self.__ljb_updater.local_ref_db_dir):
            if file_name.endswith('.readme.txt'):
                readme_file_found = True
        self.assertTrue(readme_file_found, msg='some thing went wrong in LJB updating process')

    def test_full_update2(self):
        #similar to above but with real zip file?
        pass

    def test_parse(self):
        test_file    = os.path.join(self.__test_data_dir, 'dummy_ljb_list_file')
        out = self.__ljb_updater.parse(test_file)
        self.assertEqual(out['1.3'], 'dbNSFPv1.3.readme.txt', msg='LJB parser does not work correctly in finding LJB files')

    def tearDown(self):
        #clear garbage from tmp directory
        if not combivep_config.DEBUG_MODE:
            shutil.rmtree(self.__working_dir)

        #clear readme (test) file from database directory
        for file_name in os.listdir(combivep_config.COMBIVEP_MASTER_DB_DIR):
            if file_name.endswith('.readme.txt'):
                os.remove(os.path.join(combivep_config.COMBIVEP_MASTER_DB_DIR, file_name))


class TestMisc(combivep_template.Tester):
    """ test (a few) miscellaneous function(s) """


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'misc')
        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
                                            'misc')

    def test_unzip(self):
        test_file = os.path.join(self.__test_data_dir, 'dummy_ljb.zip')
        if os.path.exists(self.__working_dir):
            shutil.rmtree(self.__working_dir)
        out = combivep_refdb.unzip(test_file, self.__working_dir)
        self.assertEqual(out[0], os.path.join(self.__working_dir, 'try.in'), msg='some files are missing')
        self.assertEqual(out[1], os.path.join(self.__working_dir, 'search_dbNSFP_light_v1.3.readme.pdf'), msg='some files are missing')
        self.assertEqual(out[2], os.path.join(self.__working_dir, 'search_dbNSFP_light_v1.3.readme.doc'), msg='some files are missing')
        self.assertEqual(out[3], os.path.join(self.__working_dir, 'search_dbNSFP_light13.class'), msg='some files are missing')
        self.assertEqual(out[4], os.path.join(self.__working_dir, 'dbNSFP_light_v1.3.readme.txt'), msg='some files are missing')
        self.assertEqual(out[5], os.path.join(self.__working_dir, 'dbNSFP_light1.3.chrY'), msg='some files are missing')
        self.assertEqual(out[6], os.path.join(self.__working_dir, 'abc/tryhg19.in'), msg='some files are missing')
        for out_file in out:
            self.assertTrue(os.path.exists(out_file), msg='"%s" file is missing' % (out_file))



