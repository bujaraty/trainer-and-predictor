import os.path


PROJECT_ROOT                = os.path.dirname(os.path.dirname(__file__))
COMBIVEP_MASTER_DATA_ROOT   = os.path.join(PROJECT_ROOT, 'combivep/data')
COMBIVEP_MASTER_DATASET_DIR = os.path.join(COMBIVEP_MASTER_DATA_ROOT, 'dataset')

MLP_COEFFICIENT = 0.9
STEP_SIZE       = 0.00016
MAXIMUM_ALLOWED_ERROR = 0.35
MINIMUM_IMPROVEMENT   = 0.0000001

