import unittest
import os.path
import combivep.engine.dataset as combivep_dataset
import combivep.template as combivep_template
import combivep.config as combivep_config
import combivep.engine.wrapper as combivep_wrapper

class Testtrainer(combivep_template.Tester):
    """ to test Trainer class in wrapper.py"""


    def setUp(self):
        self.test_data_dir = os.path.join(self.root_test_data_dir, 'mlp')

    def test_trainer_dummy(self):
        __training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR, 'training_dataset'))
        __validation_dataset = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR, 'validation_dataset'))
#        __trainer = combivep_wrapper.Trainer(__training_dataset, __validation_dataset, seed=20)
        __trainer = combivep_wrapper.Trainer(__training_dataset, __validation_dataset, seed=20, figure_dir='/home/jessada/tmp/figures')
#        __trainer = combivep_wrapper.Trainer(__training_dataset, __validation_dataset)
#        __trainer.train()
        __trainer.train(iteration=500)

