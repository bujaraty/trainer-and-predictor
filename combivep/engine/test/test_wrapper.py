import unittest
import shutil
import os
import combivep.engine.dataset as combivep_dataset
import combivep.engine.test.template as test_template
import combivep.settings as combivep_settings
import combivep.engine.wrapper as combivep_wrapper

class TestTrainer(test_template.SafeEngineTester):


    def __init__(self, test_name):
        test_template.SafeEngineTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'trainer'

    def init_trainer_instance(self):
        pass

    def test_trainer(self):
        """

        to see if it can produce parameters file and produce figure

        """
        self.individual_debug = True
        self.init_test('test_trainer')
        self.init_trainer_instance()
        training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
                                                                   'training_dataset'))
        validation_dataset = combivep_dataset.DataSet(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
                                                                   'validation_dataset'))
        trainer = combivep_wrapper.Trainer(training_dataset, validation_dataset, seed=20, n_hidden_nodes=7, figure_dir=self.working_dir)
        trainer.train(iterations=50)

        params_file  = os.path.join(self.working_dir, 'params.npz')
        trainer.export_best_parameters(params_file=params_file)
        self.assertTrue(os.path.exists(params_file), msg='Trainer does not functional properly')
        figure_file  = os.path.join(self.working_dir, '07.eps')
        self.assertTrue(os.path.exists(figure_file), msg='Trainer does not functional properly')

    def tearDown(self):
        self.remove_working_dir()

class TestPredictor(test_template.SafeEngineTester):


    def __init__(self, test_name):
        test_template.SafeEngineTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'predictor'

    def init_predictor_instance(self):
        pass

    def test_predictor(self):
        """

        to see if it can correctly predict SNPs in feature-vector format

        """
        self.individual_debug = True
        self.init_test('test_predictor')
        self.init_predictor_instance()

        predictor = combivep_wrapper.Predictor()
        test_dataset = combivep_dataset.DataSet(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
                                                             'test_dataset'))
        params_file  = os.path.join(self.data_dir, 'params.npz')
        predictor.import_parameters(params_file=params_file)
        out = predictor.predict(test_dataset)
        self.assertEqual(round(out[0][0], 4), 0.2729, msg='Predictor does not functional properly')


