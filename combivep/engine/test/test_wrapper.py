import unittest
import os.path
import shutil
import combivep.engine.dataset as combivep_dataset
import combivep.template as combivep_template
import combivep.config as combivep_config
import combivep.engine.wrapper as combivep_wrapper

class TestTrainer(combivep_template.Tester):
    """ to test Trainer class in wrapper.py"""


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'trainer')
        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
                                            'trainer')
        if not os.path.exists(self.__working_dir):
            os.makedirs(self.__working_dir)

    def test_trainer_dummy(self):
        training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR,
                                                                   'training_dataset'))
        validation_dataset = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR,
                                                                   'validation_dataset'))
#        __trainer = combivep_wrapper.Trainer(__training_dataset, __validation_dataset, seed=20)
        trainer = combivep_wrapper.Trainer(training_dataset, validation_dataset, seed=20, figure_dir=self.__working_dir)
#        __trainer = combivep_wrapper.Trainer(__training_dataset, __validation_dataset)
        trainer.train(iteration=50)

        params_file  = os.path.join(self.__working_dir, 'params.npz')
        trainer.export_best_parameters(params_file=params_file)

    def tearDown(self):
        if not combivep_config.DEBUG_MODE:
            shutil.rmtree(self.__working_dir)

class TestPredictor(combivep_template.Tester):
    """ to test Predictor class in wrapper.py"""


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'predictor')

    def test_predictor_dummy(self):
        predictor = combivep_wrapper.Predictor()
        test_dataset = combivep_dataset.DataSet(os.path.join(combivep_config.COMBIVEP_MASTER_DATASET_DIR,
                                                             'test_dataset'))
        params_file  = os.path.join(self.__test_data_dir, 'params.npz')
        predictor.import_parameters(params_file=params_file)
        out = predictor.predict(test_dataset)
        self.assertEqual(round(out[0][0], 4), 0.2729)


