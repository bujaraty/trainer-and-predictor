import unittest
import os
import combivep.preproc.test.template as test_template
import combivep.settings as combivep_settings
import combivep.preproc.dataset as combivep_dataset


class TestDataSetManager(test_template.SafePreProcTester):


    def __init__(self, test_name):
        test_template.SafePreProcTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'dataset_manager'

    def init_dataset_instance(self):
        self.__dataset_manager = combivep_dataset.DataSetManager()

    def test_vcf_load(self):
        self.init_test('test_vcf_load')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_vcf_load.vcf')
        self.__dataset_manager.load_data(test_file)
        self.assertEqual(len(self.__dataset_manager.dataset), 10, 'DataSetManager does not load VCF data correctly')

    def test_varibench_load(self):
        self.init_test('test_varibench_load')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_varibench_load.varibench')
        self.__dataset_manager.load_data(test_file, file_type=combivep_settings.FILE_TYPE_VARIBENCH)
        self.assertEqual(len(self.__dataset_manager.dataset), 11, 'DataSetManager does not load VariBench data correctly')

    def test_validate_data(self):
        self.init_test('test_validate_data')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_vcf_load.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.assertEqual(len(self.__dataset_manager.dataset), 7, 'DataSetManager does not clean data correctly')

    def test_calculate_scores(self):
        self.init_test('test_calculate_scores')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_calculate_scores.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.__dataset_manager.calculate_scores()
        self.assertEqual(len(self.__dataset_manager.dataset), 3, 'DataSetManager does not calculate scores properly')

    def test_shuffle_data(self):
        self.init_test('test_shuffle_data')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_shuffle.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.__dataset_manager.calculate_scores()
        self.assertEqual(self.__dataset_manager.dataset[5][combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_POS], '190999917', 'DataSetManager does not calculate scores properly')
        self.__dataset_manager.set_shuffle_seed(combivep_settings.DEMO_SEED)
        self.__dataset_manager.shuffle_data()
        self.assertNotEqual(self.__dataset_manager.dataset[5][combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_POS], '190999917', 'DataSetManager may not shuffle data correctly')

    def test_partition_data(self):
        self.init_test('test_partition_data')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_shuffle.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.__dataset_manager.calculate_scores()
        self.__dataset_manager.set_shuffle_seed(combivep_settings.DEMO_SEED)
        self.__dataset_manager.shuffle_data()
        self.__dataset_manager.partition_data()
        self.assertEqual(len(self.__dataset_manager.get_training_data()), 7, 'DataSetManager does not correctly partition data')
        self.assertEqual(len(self.__dataset_manager.get_validation_data()), 1, 'DataSetManager does not correctly partition data')
        self.assertEqual(len(self.__dataset_manager.get_test_data()), 2, 'DataSetManager does not correctly partition data')

    def test_vcf_dataset(self):
        self.init_test('test_dataset')
        self.init_dataset_instance()
        test_file = os.path.join(self.data_dir, 'test_shuffle.vcf')
        self.__dataset_manager.load_data(test_file)
        self.__dataset_manager.validate_data()
        self.__dataset_manager.calculate_scores()
        self.__dataset_manager.set_shuffle_seed(combivep_settings.DEMO_SEED)
        self.__dataset_manager.shuffle_data()
        self.__dataset_manager.partition_data()
        training_dataset = self.__dataset_manager.get_training_data()
#        print training_dataset.feature_vectors
#        print training_dataset.targets
        self.assertEqual(training_dataset.n_features, 6, msg='Dataset does not functional properly')
        self.assertEqual(training_dataset.n_data, 7, msg='Dataset does not functional properly')

    def test_varibench_dataset(self):
        self.init_test('test_dataset')
        self.init_dataset_instance()
#        test_file = os.path.join(self.data_dir, 'pathogenic_snp.varibench')
#        test_file = os.path.join(self.data_dir, 'neutral_snp.varibench')
        test_file = os.path.join(self.data_dir, 'test_varibench_dataset.varibench')
        self.__dataset_manager.load_data(test_file, file_type=combivep_settings.FILE_TYPE_VARIBENCH)
#        print 'after load', len(self.__dataset_manager.dataset)
#        for item in self.__dataset_manager.dataset:
#            print item
        self.__dataset_manager.validate_data
#        print 'after validate data', len(self.__dataset_manager.dataset)
#        for item in self.__dataset_manager.dataset:
#            print item
        self.__dataset_manager.calculate_scores()
#        print 'after calculate scores', len(self.__dataset_manager.dataset)
#        for item in self.__dataset_manager.dataset:
#            print item
#        print self.__dataset_manager.dataset.feature_vectors
        self.__dataset_manager.set_shuffle_seed(combivep_settings.DEMO_SEED)
        self.__dataset_manager.shuffle_data()
        self.__dataset_manager.partition_data()
        training_dataset = self.__dataset_manager.get_training_data()
#        print 'after calculate scores', len(training_dataset)
#        print training_dataset.feature_vectors
#        print training_dataset.targets
        self.assertEqual(training_dataset.n_features, 6, msg='Dataset does not functional properly')
        self.assertEqual(training_dataset.n_data, 13, msg='Dataset does not functional properly')

    def test_add_dataset(self):
        self.init_test('test_add_dataset')
        test_file = os.path.join(self.data_dir, 'test_add_dataset1.varibench')
        self.dataset_manager1 = combivep_dataset.DataSetManager()
        self.dataset_manager1.load_data(test_file, file_type=combivep_settings.FILE_TYPE_VARIBENCH)
#        print 'after load', len(self.dataset_manager1.dataset)
        self.dataset_manager1.validate_data()
#        print 'after validate', len(self.dataset_manager1.dataset)
        self.dataset_manager1.calculate_scores()
        self.dataset_manager1.shuffle_data()
        self.dataset_manager1.partition_data()
        training_dataset1 = self.dataset_manager1.get_training_data()
#        print 'dataset1'
#        print training_dataset1.feature_vectors
#        print training_dataset1.targets
        test_file = os.path.join(self.data_dir, 'test_add_dataset2.varibench')
        self.dataset_manager2 = combivep_dataset.DataSetManager()
        self.dataset_manager2.load_data(test_file, file_type=combivep_settings.FILE_TYPE_VARIBENCH)
        self.dataset_manager2.validate_data()
        self.dataset_manager2.calculate_scores()
        self.dataset_manager2.shuffle_data()
        self.dataset_manager2.partition_data()
        training_dataset2 = self.dataset_manager2.get_training_data()
#        print 'dataset2'
#        print training_dataset2.feature_vectors
#        print training_dataset2.targets
        combine_dataset = training_dataset1 + training_dataset2
        self.assertEqual(len(combine_dataset), 9, 'DataSetManager does not load VCF data correctly')
#        print 'combine'
#        print combine_dataset.feature_vectors
#        print combine_dataset.targets
#        print 'dataset1'
#        print training_dataset1.feature_vectors
#        print training_dataset1.targets

    def tearDown(self):
        self.remove_working_dir()






