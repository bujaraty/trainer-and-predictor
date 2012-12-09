import unittest
import os.path
import numpy as np
import combivep.engine.mlp as combivep_mlp
import combivep.engine.dataset as combivep_dataset
import combivep.template as combivep_template
import combivep.config as combivep_config

class TestMlp(combivep_template.Tester):
    """ to test mlp.py"""


    def setUp(self):
        self.test_data_dir = os.path.join(self.root_test_data_dir, 'mlp')

    def test_fix_random_weight(self):
        """
        
        check if the initial random values of weight matrixes are likely to be
        random.
        
        """
        __training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR, 'dummy_training_dataset'))
        __mlp = combivep_mlp.Mlp(__training_dataset.n_features, seed=20)
        self.assertEqual(round(__mlp.get_weights1()[0][1], 4), 0.0090)
        self.assertEqual(round(__mlp.get_weights1()[0][0], 4), 0.0059)

    def test_forward_propagation(self):
        """
        
        check if the matrix multiplications in forward propagationin are 
        working properly.
        
        """
        __training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR, 'dummy_training_dataset'))
        __mlp = combivep_mlp.Mlp(__training_dataset.n_features, seed=20)
        __out = __mlp.forward_propagation(__training_dataset)
        self.assertEqual(round(__out[0][0], 4), 0.5008)

    def test_one_round_forward_backward_weight_update(self):
        __training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR, 'dummy_training_dataset'))
        __mlp = combivep_mlp.Mlp(__training_dataset.n_features, seed=20)
        __mlp.forward_propagation(__training_dataset)
        __mlp.backward_propagation(__training_dataset)
        __mlp.weight_update(__training_dataset)


