import os
from combivep.devtools.utils import filter_cbv_data
from combivep.app import train_combivep_using_cbv_data
import combivep.settings as combivep_settings
import combivep.devtools.settings as devtools_settings


def filter_all_cbv():
    filter_cbv_data(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_CBV_DIR, 'training.cbv'))
    filter_cbv_data(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_CBV_DIR, 'test.cbv'))

def generate_model_resources():
    train_combivep_using_cbv_data(os.path.join(combivep_settings.COMBIVEP_CENTRAL_TEST_CBV_DIR, 'training.cbv.scores'),
                                  params_out_file=devtools_settings.PUBLICATION_PARAMETER_FILE,
                                  random_seed=combivep_settings.DEMO_SEED,
                                  figure_dir=devtools_settings.PUBLICATION_FIGURES_DIR,
                                  )







