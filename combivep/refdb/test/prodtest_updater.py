import unittest
import os
import combivep.refdb.test.template as template
import combivep.settings as combivep_settings
import combivep.refdb.updater as combivep_updater


class TestLJBUpdater(template.RiskyRefDBTester):


    def setUp(self):
        self.test_class = 'ljb_updater'

    def init_ljb_updater_instance(self):
        self.__ljb_updater                  = combivep_updater.LjbUpdater()

    @unittest.skip("temporary disable due to high bandwidth usage")
    def test_full_update(self):
        #init
        self.init_test('test_full_update')
        self.init_ljb_updater_instance()

        new_file, new_version = self.__ljb_updater.check_new_file('1.2')
        self.assertTrue(new_file.endswith('.zip'), msg='some thing went wrong in LJB updating process: new file is not the correct file')
        self.assertEqual(new_version, '1.3', msg='some thing went wrong in LJB updating process: incorrect new version number')
        unzipped_files = self.__ljb_updater.download_new_file()
        for unzipped_file in unzipped_files:
            print unzipped_file
            self.assertTrue(os.path.exists(unzipped_file), msg='"%s" file is missing' % (unzipped_file))


    def tearDown(self):
        self.remove_working_dir()


