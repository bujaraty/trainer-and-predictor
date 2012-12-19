import unittest
import os
import shutil
import combivep.refdb.test.template as template
import combivep.config as combivep_config
import combivep.refdb.scoresdb as combivep_scoresdb
import combivep.refdb.reader as combivep_reader


"""

The purpose of these tests is to test scoresdb module with the environment
close to production environment as much as possible

In many cases, the input files are likely to are huge and be excluded from
application package. So please be awared if the errors said some files
are missing

Due to the enormous size of the input files, usually, the expected results
are 'runable'

"""


class TestScoresDB(template.RiskRefDBTester):


    def setUp(self):
        self.test_class = 'scores_db'

    def init_scores_db_instance(self):
        self.__scores_db = combivep_scoresdb.ScoresDB()

    def test_join(self):
        #init
        self.individual_debug = True
        self.init_scores_db_instance()
        ljb_file  = '/home/jessada/development/scilifelab/master_data/LJB/tmp1'
        ucsc_file = '/home/jessada/development/scilifelab/master_data/UCSC/snp137_chr3.txt.gz'
        out_file  = os.path.join(combivep_config.COMBIVEP_MASTER_DB_DIR, 'join_result.txt')
#        expected_out_file = os.path.join(self.data_dir, 'expected_join_result.txt')

        #test if the output file is correctly produced
        self.__scores_db.join(ljb_file, ucsc_file, out_file)
#        self.assertTrue(filecmp.cmp(out_file, expected_out_file), "Incorrect join result")

#    def tearDown(self):
#        self.remove_working_dir()


