import os
import unittest
import combivep.test.template as test_template
import combivep.settings as combivep_settings
import combivep.app as combivep_app


class TestApp(test_template.SafeGeneralTester):


    def __init__(self, test_name):
        test_template.SafeGeneralTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'app'

    def init_configure_instance(self):
        pass

    def test_train_combivep_using_cvf_data(self):
        #init
        self.individual_debug = True
        self.init_test('train_combivep_using_cvf_data')
        test_file    = os.path.join(self.data_dir, 'test_train_combivep.cvf')
        params_file  = os.path.join(self.working_dir, 'params.npz')
        #run test
        combivep_app.train_combivep_using_cvf_data(test_file,
                                                   random_seed=20,
                                                   n_hidden_nodes=7,
                                                   iterations=50,
                                                   figure_dir=self.working_dir,
                                                   params_out_file=params_file,
                                                   config_file=combivep_settings.COMBIVEP_CENTRAL_TEST_CONFIGURATION_FILE)
        self.assertTrue(os.path.exists(params_file), msg='Trainer does not functional properly')
        figure_file  = os.path.join(self.working_dir, '07.eps')
        self.assertTrue(os.path.exists(figure_file), msg='Trainer does not functional properly')

    def test_predict_deleterious_probability_cvf(self):
        #init
        self.individual_debug = True
        self.init_test('predict_deleterious_probability_cvf')
        test_file = os.path.join(self.data_dir, 'test_test_combivep.cvf')
        output_file  = os.path.join(self.working_dir, 'cvf_output.txt')
        #run test
        combivep_app.predict_deleterious_probability(test_file,
                                                     params_file=combivep_settings.COMBIVEP_CENTRAL_TEST_PARAMETER_FILE,
                                                     file_type=combivep_settings.FILE_TYPE_CVF,
                                                     config_file=combivep_settings.COMBIVEP_CENTRAL_TEST_CONFIGURATION_FILE,
                                                     output_file=output_file,
                                                     )

    def test_predict_deleterious_probability_vcf(self):
        #init
        self.individual_debug = True
        self.init_test('predict_deleterious_probability_vcf')
        test_file = os.path.join(self.data_dir, 'test_test_combivep.vcf')
        output_file  = os.path.join(self.working_dir, 'vcf_output.txt')
        #run test
        combivep_app.predict_deleterious_probability(test_file,
                                                     params_file=combivep_settings.COMBIVEP_CENTRAL_TEST_PARAMETER_FILE,
                                                     file_type=combivep_settings.FILE_TYPE_VCF,
                                                     config_file=combivep_settings.COMBIVEP_CENTRAL_TEST_CONFIGURATION_FILE,
                                                     output_file=output_file,
                                                     )


    def tearDown(self):
        self.remove_working_dir()


