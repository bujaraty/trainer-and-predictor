import unittest
import os
import shutil
import filecmp
import combivep.refdb.test.template as template
import combivep.settings as combivep_settings
import combivep.refdb.scoresdb as combivep_scoresdb
import combivep.refdb.reader as combivep_reader


class TestScoresDB(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'scores_db'

    def init_scores_db_instance(self):
        self.__scores_db = combivep_scoresdb.ScoresDB()

    def test_tabix(self):
        #init
        self.init_test('test_tabix')
        self.init_scores_db_instance()
        test_file    = os.path.join(self.data_dir, 'test_tabix.txt')
        working_file = os.path.join(self.working_dir, 'test_tabix.txt')
        self.copy_file(test_file, working_file)

        #test if the 'tabix' files are produced
        self.__scores_db.tabix(working_file)
        self.assertTrue(os.path.exists(working_file+'.gz'))
        self.assertTrue(os.path.exists(working_file+'.gz.tbi'))

        #test if it is readable by UcscReader
        reader = combivep_reader.UcscReader()
        reader.read(working_file+'.gz')
        for rec in reader.fetch_snps('chr3', 138211840, 138212000):
            self.assertEqual(rec[combivep_settings.KEY_UCSC_START_POS], '138211844', "Tabix doesn't work correctly")
            break

    def test_join(self):
        #init
        self.individual_debug = True
        self.init_test('test_join')
        self.init_scores_db_instance()
        ljb_file  = os.path.join(self.data_dir, 'test_ljb_join.txt')
        ucsc_file = os.path.join(self.data_dir, 'test_ucsc_join.txt.gz')
        out_file  = os.path.join(self.working_dir, 'join_result.txt')
        expected_out_file = os.path.join(self.data_dir, 'expected_join_result.txt')

        #test if the output file is correctly produced
        self.__scores_db.join(ljb_file, ucsc_file, out_file)
        self.assertTrue(filecmp.cmp(out_file, expected_out_file), "Incorrect join result")

    def tearDown(self):
        self.remove_working_dir()


