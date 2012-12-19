import unittest
import os.path
import combivep.template as combivep_template
import combivep.settings as combivep_settings
import combivep.utils.preproc as combivep_preproc

class TestPreproc(combivep_template.Tester):


    def setUp(self):
        self.__test_data_dir = os.path.join(self.get_root_data_dir(__file__),
                                            'preproc')

    def test_preproc_dummy(self):
        preproc = combivep_preproc.PreProc()
        preproc.load_vcf(os.path.join(self.__test_data_dir, 'sample.vcf'))


