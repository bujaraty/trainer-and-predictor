import unittest
import os.path
import combivep.engine.dataset as combivep_dataset
import combivep.template as combivep_template
import combivep.config as combivep_config

class TestDataSet(combivep_template.Tester):
    """ to test dataset.py"""


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'dataset')

    def test_dataset_property(self):
        """
        
        check if number of rows, columns, and features are correctly counted.
        
        """
        dataset = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
                                                        'test_dataset'))
        self.assertEqual(dataset.n_data, 1718)
        self.assertEqual(dataset.n_cols, 8)
        self.assertEqual(dataset.n_features, 6)


