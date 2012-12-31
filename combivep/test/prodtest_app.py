import os
import unittest
import combivep.test.template as test_template
import combivep.settings as combivep_settings
import combivep.app as combivep_app


class TestApp(test_template.RiskyGeneralTester):


    def __init__(self, test_name):
        test_template.RiskyGeneralTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'app'

    def init_configure_instance(self):
        pass

    def test_demo_train_combivep_using_cvf_data(self):
        #init
        self.individual_debug = True
        self.init_test('demo_train_combivep_using_cvf_data')
        training_file = os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_CVF_DIR, 'training.cvf')
        #run test
        combivep_app.train_combivep_using_cvf_data(training_file, random_seed=20, figure_dir=self.working_dir)
        self.assertTrue(combivep_settings.COMBIVEP_CONFIGURATION_FILE, msg='Trainer does not functional properly')
        figure_file  = os.path.join(self.working_dir, '%02d.eps' % int(combivep_settings.DEFAULT_HIDDEN_NODES))
        self.assertTrue(os.path.exists(figure_file), msg='Trainer does not functional properly')

    def tearDown(self):
        self.remove_working_dir()


