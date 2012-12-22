import unittest
import os
import combivep.refdb.test.template as template
import combivep.settings as combivep_settings
import combivep.refdb.reader as combivep_reader


class TestUcscReader(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'ucsc_reader'

    def init_ucsc_reader_instance(self):
        self.__ucsc_reader = combivep_reader.UcscReader()

    def test_fetch_snps1(self):
        self.init_test('test_fetch_snps1')
        self.init_ucsc_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ucsc_reader.txt.gz')
        self.__ucsc_reader.read(test_file)
        records = list(self.__ucsc_reader.fetch_hash_snps('chr3', 110030150, 110030300))
        self.assertEqual(len(list(records)), 3, "Incorrect number of records are being fetched")

    def test_fetch_snps2(self):
        self.init_test('test_fetch_snps2')
        self.init_ucsc_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ucsc_reader.txt.gz')
        self.__ucsc_reader.read(test_file)
        records = list(self.__ucsc_reader.fetch_hash_snps('3', 110030150, 110030300))
        self.assertEqual(len(records), 3, "Incorrect number of records are being fetched")

    def test_formatting(self):
        self.init_test('test_formatting')
        self.init_ucsc_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ucsc_reader.txt.gz')
        self.__ucsc_reader.read(test_file)
        readable = False
        for rec in self.__ucsc_reader.fetch_hash_snps('3', 110030157, 110030158):
            readable = True
            self.assertEqual(rec[combivep_settings.KEY_UCSC_CHROM], 'chr3', "Incorrect UCSC formatting")
            self.assertEqual(rec[combivep_settings.KEY_UCSC_START_POS], '110030157', "Incorrect UCSC formatting")
            self.assertEqual(rec[combivep_settings.KEY_UCSC_END_POS], '110030158', "Incorrect UCSC formatting")
            self.assertEqual(rec[combivep_settings.KEY_UCSC_STRAND], '+', "Incorrect UCSC formatting")
            self.assertEqual(rec[combivep_settings.KEY_UCSC_REF], 'C', "Incorrect UCSC formatting")
            self.assertEqual(rec[combivep_settings.KEY_UCSC_OBSERVED], 'C/T', "Incorrect UCSC formatting")
#            self.assertEqual(rec[combivep_settings.JOIN_KEY], 'chr3|110030157', "Incorrect UCSC formatting")
            break
        self.assertTrue(readable, "UCSC database is not readable")

    def test_valid_indexing1(self):
        self.init_test('test_valid_indexing1')
        self.init_ucsc_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ucsc_reader.txt.gz')
        self.__ucsc_reader.read(test_file)
        records = list(self.__ucsc_reader.fetch_hash_snps('3', 110030330, 110030332))
        self.assertEqual(len(records), 2, "Incorrect number of records are being fetched")

    def test_valid_indexing2(self):
        self.init_test('test_valid_indexing2')
        self.init_ucsc_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ucsc_reader.txt.gz')
        self.__ucsc_reader.read(test_file)
        records = list(self.__ucsc_reader.fetch_hash_snps('3', 110030330, 110030331))
        self.assertEqual(len(records), 1, "Incorrect number of records are being fetched")

    def test_valid_indexing3(self):
        self.init_test('test_valid_indexing3')
        self.init_ucsc_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ucsc_reader.txt.gz')
        self.__ucsc_reader.read(test_file)
        records = list(self.__ucsc_reader.fetch_hash_snps('3', 110030331, 110030332))
        self.assertEqual(len(records), 1, "Incorrect number of records are being fetched")

    def tearDown(self):
        self.remove_working_dir()


class TestLjbReader(template.SafeRefDBTester):


    def setUp(self):
        self.test_class = 'ljb_reader'

    def init_ljb_reader_instance(self):
        self.__ljb_reader = combivep_reader.LjbReader()

    def test_valid_indexing1(self):
        self.init_test('test_valid_indexing1')
        self.init_ljb_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ljb_reader.txt.gz')
        self.__ljb_reader.read(test_file)
        records = list(self.__ljb_reader.fetch_hash_snps('3', 108541777, 108541779))
        self.assertEqual(len(records), 3, "Incorrect number of records are being fetched")

    def test_valid_indexing2(self):
        self.init_test('test_valid_indexing1')
        self.init_ljb_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ljb_reader.txt.gz')
        self.__ljb_reader.read(test_file)
        records = list(self.__ljb_reader.fetch_hash_snps('3', 108541777, 108541778))
        self.assertEqual(len(records), 2, "Incorrect number of records are being fetched")

    def test_valid_indexing3(self):
        self.init_test('test_valid_indexing1')
        self.init_ljb_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ljb_reader.txt.gz')
        self.__ljb_reader.read(test_file)
        records = list(self.__ljb_reader.fetch_hash_snps('3', 108541778, 108541779))
        self.assertEqual(len(records), 1, "Incorrect number of records are being fetched")

    def test_formatting(self):
        self.init_test('test_formatting')
        self.init_ljb_reader_instance()
        test_file = os.path.join(self.data_dir, 'test_ljb_reader.txt.gz')
        self.__ljb_reader.read(test_file)
        for rec in self.__ljb_reader.fetch_hash_snps('3', 108541777, 108541779):
            self.assertEqual(rec[combivep_settings.KEY_LJB_CHROM], '3', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.KEY_LJB_START_POS], '108541778', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.KEY_LJB_REF], 'T', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.KEY_LJB_ALT], 'C', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.PHYLOP_SCORE], '0.102322', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.SIFT_SCORE], '0.91', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.PP2_SCORE], '0', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.LRT_SCORE], '0.312516', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.MT_SCORE], '0.000000', "Incorrect LJB formatting")
            self.assertEqual(rec[combivep_settings.GERP_SCORE], '-3.16', "Incorrect LJB formatting")
#            self.assertEqual(rec[combivep_settings.JOIN_KEY], 'chr3|110024464', "Incorrect UCSC formatting")
            break

    def tearDown(self):
        self.remove_working_dir()




