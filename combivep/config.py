import os.path

DEBUG_MODE = 0

PROJECT_ROOT                = os.path.dirname(os.path.dirname(__file__))

#to keep system DB-like data produced by application
COMBIVEP_SYSTEM_DATA_ROOT   = os.path.join(PROJECT_ROOT, 'dat')
COMBIVEP_PARAMETERS_FILE    = os.path.join(COMBIVEP_SYSTEM_DATA_ROOT, 'params.npz')

#to keep 'master' data for testing and for demo. 'master' is for preventing redundancy.
COMBIVEP_MASTER_DATA_ROOT   = os.path.join(PROJECT_ROOT, 'combivep/data')
COMBIVEP_MASTER_DATASET_DIR = os.path.join(COMBIVEP_MASTER_DATA_ROOT, 'dataset')

#general model configuration
MLP_COEFFICIENT       = 0.9
STEP_SIZE             = 0.00016
MAXIMUM_ALLOWED_ERROR = 0.35
MINIMUM_IMPROVEMENT   = 0.0000001

#default model argument values
DEFAULT_HIDDEN_NODES  = 4
DEFAULT_SEED          = None
DEFAULT_FIGURE_DIR    = None

