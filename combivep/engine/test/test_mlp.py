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
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'mlp')

    def test_fix_random_weight(self):
        """

        check if the initial random values of weight matrixes are likely to be
        random.

        """
        training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
                                                                   'dummy_training_dataset'))
        mlp = combivep_mlp.Mlp(training_dataset.n_features, seed=20)
        self.assertEqual(round(mlp.get_weights1()[0][1], 4), 0.0090)
        self.assertEqual(round(mlp.get_weights1()[0][0], 4), 0.0059)

    def test_forward_propagation(self):
        """

        check if the matrix multiplications in forward propagationin are 
        working properly.

        """
        training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
                                                                   'dummy_training_dataset'))
        mlp = combivep_mlp.Mlp(training_dataset.n_features, seed=20)
        out = mlp.forward_propagation(training_dataset)
        self.assertEqual(round(out[0][0], 4), 0.5008)

    def test_one_round_forward_backward_weight_update(self):
        """

        to see if can correctly run one round of "forward", "backward" and
        "weight update"

        """
        training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
                                                                   'dummy_training_dataset'))
        mlp = combivep_mlp.Mlp(training_dataset.n_features, seed=20)
        mlp.forward_propagation(training_dataset)
        mlp.backward_propagation(training_dataset)
        weights1, weights2 = mlp.weight_update(training_dataset)
        self.assertEqual(round(weights1[0][0], 4), 0.0059)


