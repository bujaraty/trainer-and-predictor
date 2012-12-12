import unittest
import os.path
import glob
import shutil
import combivep.template as combivep_template
import combivep.config as combivep_config
import combivep.utils.db as combivep_db

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
        downloader  = combivep_db.Downloader()
        target_url  = 'http://dbnsfp.houstonbioinformatics.org/dbNSFPzip/dbNSFP_light_v1.3.readme.txt'
        target_file = os.path.join(self.__working_dir, os.path.basename(target_url))
        downloader.download(target_url, self.__working_dir)
        self.assertGreater(os.stat(target_file).st_size, 3397)

    def tearDown(self):
        if not combivep_config.DEBUG_MODE:
            shutil.rmtree(self.__working_dir)


@unittest.skipIf(not combivep_config.DEBUG_MODE, "not tested in production mode")
class TestUcscUpdater(combivep_template.Tester):


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'updater')
        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
                                            'updater')
        if not os.path.exists(self.__working_dir):
            os.makedirs(self.__working_dir)
        self.__folder_url        = combivep_config.UCSC_FOLDER_URL
        self.__sql_files_pattern = r"""href="(?P<file_name>snp\d{3}.sql)">.*>.*(?P<date>\d{2}-[a-zA-Z]{3}-\d{4})"""
        self.__gz_files_pattern  = combivep_config.UCSC_FILES_PATTERN
        self.__version_pattern   = combivep_config.UCSC_VERSION_PATTERN
        self.__tmp_file          = combivep_config.UCSC_LIST_FILE_NAME
    def test_update(self):
        ucsc_updater = combivep_db.Updater(working_dir=self.__working_dir)
        self.assertEqual(ucsc_updater.update('135',
                                             self.__folder_url,
                                             self.__sql_files_pattern,
                                             self.__version_pattern,
                                             tmp_file=self.__tmp_file
                                             ),
                         True
                         )

    def test_not_update(self):
        ucsc_updater = combivep_db.Updater(working_dir=self.__working_dir)
        self.assertEqual(ucsc_updater.update('137',
                                             self.__folder_url,
                                             self.__sql_files_pattern,
                                             self.__version_pattern,
                                             tmp_file=self.__tmp_file
                                             ),
                         False
                         )

    def test_full_update1(self):
        ucsc_updater = combivep_db.Updater(working_dir=self.__working_dir)
        ucsc_updater.update('135',
                            self.__folder_url,
                            self.__sql_files_pattern,
                            self.__version_pattern,
                            tmp_file=self.__tmp_file
                            )
        sql_file_found = False
        for file_name in os.listdir(combivep_config.COMBIVEP_MASTER_DB_DIR):
            if file_name.endswith('.sql'):
                sql_file_found = True
        self.assertTrue(sql_file_found)

    def test_full_update2(self):
        #similar to above but with real gz file?
        pass

    def test_parse(self):
        ucsc_updater = combivep_db.Updater(working_dir=self.__working_dir)
        test_file    = os.path.join(self.__test_data_dir, 'dummy_ucsc_list_file')
        out = ucsc_updater.parse(test_file,
                                 self.__sql_files_pattern,
                                 self.__version_pattern)
        self.assertEqual(out['135'], 'snp135.sql')

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
                                            'updater')
        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
                                            'updater')
        if not os.path.exists(self.__working_dir):
            os.makedirs(self.__working_dir)
        self.__folder_url           = combivep_config.LJB_FOLDER_URL
        self.__readme_files_pattern = r"""href="(?P<file_name>dbNSFPv[\d.]*.readme.txt)">"""
        self.__light_files_pattern  = combivep_config.LJB_FILES_PATTERN
        self.__version_pattern      = combivep_config.LJB_VERSION_PATTERN
        self.__tmp_file             = combivep_config.LJB_LIST_FILE_NAME

    def test_update(self):
        ljb_updater = combivep_db.Updater(working_dir=self.__working_dir)
        self.assertEqual(ljb_updater.update('1.2',
                                             self.__folder_url,
                                             self.__readme_files_pattern,
                                             self.__version_pattern,
                                             tmp_file=self.__tmp_file
                                             ),
                         True
                         )

    def test_not_update(self):
        ljb_updater = combivep_db.Updater(working_dir=self.__working_dir)
        self.assertEqual(ljb_updater.update('1.3',
                                             self.__folder_url,
                                             self.__readme_files_pattern,
                                             self.__version_pattern,
                                             tmp_file=self.__tmp_file
                                             ),
                         False
                         )

    def test_full_update1(self):
        ljb_updater = combivep_db.Updater(working_dir=self.__working_dir)
        ljb_updater.update('1.2',
                            self.__folder_url,
                            self.__readme_files_pattern,
                            self.__version_pattern,
                            tmp_file=self.__tmp_file
                            )
        sql_file_found = False
        for file_name in os.listdir(combivep_config.COMBIVEP_MASTER_DB_DIR):
            if file_name.endswith('.readme.txt'):
                sql_file_found = True
        self.assertTrue(sql_file_found)

    def test_full_update2(self):
        #similar to above but with real zip file?
        pass

    def test_parse(self):
        ljb_updater = combivep_db.Updater(working_dir=self.__working_dir)
        test_file   = os.path.join(self.__test_data_dir, 'dummy_ljb_list_file')
        out = ljb_updater.parse(test_file,
                                self.__readme_files_pattern,
                                self.__version_pattern)
        self.assertEqual(out['1.3'], 'dbNSFPv1.3.readme.txt')

    def tearDown(self):
        #clear garbage from tmp directory
        if not combivep_config.DEBUG_MODE:
            shutil.rmtree(self.__working_dir)

        #clear readme (test) file from database directory
        for file_name in os.listdir(combivep_config.COMBIVEP_MASTER_DB_DIR):
            if file_name.endswith('.readme.txt'):
                os.remove(os.path.join(combivep_config.COMBIVEP_MASTER_DB_DIR, file_name))


