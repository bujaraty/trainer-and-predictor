import unittest
import shutil
import os
import combivep.engine.dataset as combivep_dataset
import combivep.engine.test.template as test_template
#import combivep.template as co_template
import combivep.settings as combivep_settings
import combivep.engine.wrapper as combivep_wrapper

class TestTrainer(test_template.SafeEngineTester):


    def __init__(self, test_name):
        test_template.SafeEngineTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'trainer'

    def init_trainer_instance(self):
        pass
#        self.__trainer = combivep_wrapper.Trainer()

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
        trainer = combivep_wrapper.Trainer(training_dataset, validation_dataset, seed=20, figure_dir=self.working_dir)
        trainer.train(iteration=50)

        params_file  = os.path.join(self.working_dir, 'params.npz')
        trainer.export_best_parameters(params_file=params_file)
        self.assertEqual(os.stat(params_file).st_size, 666, msg='Trainer does not functional properly')
        figure_file  = os.path.join(self.working_dir, '04.eps')
        self.assertEqual(os.stat(figure_file).st_size, 21497, msg='Trainer does not functional properly')

    def tearDown(self):
        self.remove_working_dir()

#class TestTrainer(combivep_template.Tester):
#    """ to test Trainer class in wrapper.py"""
#
#
#    def setUp(self):
#        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
#                                            'trainer')
#        self.__working_dir   = os.path.join(self.get_root_working_dir(__file__),
#                                            'trainer')
#        if not os.path.exists(self.__working_dir):
#            os.makedirs(self.__working_dir)
#
#    def test_trainer(self):
#        """
#
#        to see if it can produce parameters file and produce figure
#
#        """
#        training_dataset   = combivep_dataset.DataSet(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
#                                                                   'training_dataset'))
#        validation_dataset = combivep_dataset.DataSet(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
#                                                                   'validation_dataset'))
#        trainer = combivep_wrapper.Trainer(training_dataset, validation_dataset, seed=20, figure_dir=self.__working_dir)
#        trainer.train(iteration=50)
#
#        params_file  = os.path.join(self.__working_dir, 'params.npz')
#        trainer.export_best_parameters(params_file=params_file)
#        self.assertEqual(os.stat(params_file).st_size, 666, msg='Trainer does not functional properly')
#        figure_file  = os.path.join(self.__working_dir, '04.eps')
#        self.assertEqual(os.stat(figure_file).st_size, 21484, msg='Trainer does not functional properly')
#
#    def tearDown(self):
#        if not combivep_settings.DEBUG_MODE:
#            shutil.rmtree(self.__working_dir)
#
#class TestPredictor(combivep_template.Tester):
#    """ to test Predictor class in wrapper.py"""
#
#
#    def setUp(self):
#        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
#                                            'predictor')
#
#    def test_predictor(self):
#        """
#
#        to see if it can correctly predict SNPs in feature-vector format
#
#        """
#        predictor = combivep_wrapper.Predictor()
#        test_dataset = combivep_dataset.DataSet(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_DATASET_DIR,
#                                                             'test_dataset'))
#        params_file  = os.path.join(self.__test_data_dir, 'params.npz')
#        predictor.import_parameters(params_file=params_file)
#        out = predictor.predict(test_dataset)
#        self.assertEqual(round(out[0][0], 4), 0.2729, msg='Predictor does not functional properly')


