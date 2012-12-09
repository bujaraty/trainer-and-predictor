import unittest
import os.path
import combivep.engine.dataset as combivep_dataset
import combivep.template as combivep_template
import combivep.config as combivep_config

class TestDataSet(combivep_template.Tester):
    """ to test dataset.py"""


    def setUp(self):
        self.test_data_dir = os.path.join(self.root_test_data_dir, 'dataset')

    def test_general(self):
        """
        
        check if number of rows, columns, and features are correctly counted.
        
        """
        __dataset = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR, 'test_dataset'))
        self.assertEqual(__dataset.n_data, 1718)
        self.assertEqual(__dataset.n_cols, 8)
        self.assertEqual(__dataset.n_features, 6)


