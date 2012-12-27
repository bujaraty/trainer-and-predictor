import unittest
import os
import combivep.preproc.test.template as test_template
import combivep.settings as combivep_settings
import combivep.preproc.dataset as combivep_dataset


class TestDatasetManager(test_template.SafePreProcTester):


    def __init__(self, test_name):
        test_template.SafePreProcTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'dataset'

    def init_dataset_instance(self):
        self.__dataset_manager = combivep_dataset.DatasetManager()

    def test_vcf_load(self):
        self.init_test('test_validate_snp')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_vcf_load.vcf')
        self.__dataset_manager.load_data(test_file)
        self.assertEqual(len(self.__dataset_manager.array_data), 10, 'DatasetManager does not load VCF data correctly')

    def test_validate_data(self):
        self.init_test('test_validate_data')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_vcf_load.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.assertEqual(len(self.__dataset_manager.array_data), 7, 'DatasetManager does not clean data correctly')

    def test_calculate_scores(self):
        self.init_test('test_calculate_scores')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_calculate_scores.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.__dataset_manager.calculate_scores()
        self.assertEqual(len(self.__dataset_manager.array_data), 3, 'DatasetManager does not calculate scores properly')

    def test_shuffle_data(self):
        self.init_test('test_shuffle_data')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_shuffle.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.__dataset_manager.calculate_scores()
        self.assertEqual(self.__dataset_manager.array_data[5][combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_POS], '190999917', 'DatasetManager does not calculate scores properly')
        self.__dataset_manager.shuffle_seed = combivep_settings.DEMO_SEED
        self.__dataset_manager.shuffle_data()
        self.assertNotEqual(self.__dataset_manager.array_data[5][combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_POS], '190999917', 'DatasetManager may not shuffle data correctly')

    def test_partition_data(self):
        self.init_test('test_partition_data')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_shuffle.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.__dataset_manager.calculate_scores()
        self.__dataset_manager.shuffle_seed = combivep_settings.DEMO_SEED
        self.__dataset_manager.shuffle_data()
        self.__dataset_manager.partition_data()
        self.assertEqual(len(list(self.__dataset_manager.fetch_training_data())), 7, 'DatasetManager does not correctly partition data')
        self.assertEqual(len(list(self.__dataset_manager.fetch_validation_data())), 1, 'DatasetManager does not correctly partition data')
        self.assertEqual(len(list(self.__dataset_manager.fetch_test_data())), 2, 'DatasetManager does not correctly partition data')

    def tearDown(self):
        self.remove_working_dir()






