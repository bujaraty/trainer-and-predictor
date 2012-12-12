import os.path

"""

Please don't change the value of DEBUG_MODE if you are in the production environment.
This value is for testing purpose.

"""
DEBUG_MODE = 1

# > > > > > > > > > > > > > global data & folder < < < < < < < < < < 
PROJECT_ROOT                      = os.path.dirname(os.path.dirname(__file__))

#to keep master data produced by application
COMBIVEP_MASTER_DATA_ROOT         = os.path.join(PROJECT_ROOT, 'dat')
COMBIVEP_MASTER_PARAMETERS_DIR    = os.path.join(COMBIVEP_MASTER_DATA_ROOT, 'params')
COMBIVEP_MASTER_PARAMETERS_FILE   = os.path.join(COMBIVEP_MASTER_PARAMETERS_DIR, 'params.npz')
COMBIVEP_MASTER_DB_DIR            = os.path.join(COMBIVEP_MASTER_DATA_ROOT, 'DB')
COMBIVEP_UPDATER_WORKING_DIR      = os.path.join(COMBIVEP_MASTER_DB_DIR, 'tmp')

#to keep 'central' data for testing and for demo. 'central' is for preventing redundancy.
COMBIVEP_CENTRAL_TEST_DATA_ROOT   = os.path.join(PROJECT_ROOT, 'combivep/data')
COMBIVEP_CENTRAL_TEST_DATASET_DIR = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'dataset')
COMBIVEP_CENTRAL_TEST_VCF_DIR     = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'vcf')


# > > > > > > > > > > > > > MLP configuration < < < < < < < < < < 
#general model configuration
MLP_COEFFICIENT       = 0.9
STEP_SIZE             = 0.00016
MAXIMUM_ALLOWED_ERROR = 0.35
MINIMUM_IMPROVEMENT   = 0.0000001

#default model argument values
DEFAULT_HIDDEN_NODES  = 4
DEFAULT_SEED          = None
DEFAULT_FIGURE_DIR    = None


# > > > > > > > > > > > > > database configuration < < < < < < < < < < 
#UCSC
UCSC_FOLDER_URL      = 'http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database'
UCSC_LIST_FILE_NAME  = 'ucsc_list_file'
UCSC_FILES_PATTERN   = r"""href="(?P<file_name>snp\d{3}.txt.gz)">.*>.*(?P<date>\d{2}-[a-zA-Z]{3}-\d{4})"""
UCSC_VERSION_PATTERN = r"""[a-zA-Z]*(?P<version>[\d]*)[a-zA-Z.]*"""

#LJB
LJB_FOLDER_URL       = 'http://dbnsfp.houstonbioinformatics.org/dbNSFPzip/'
LJB_LIST_FILE_NAME   = 'ljb_list_file'
LJB_FILES_PATTERN    = r"""href="(?P<file_name>dbNSFP_.*.zip)">"""
LJB_VERSION_PATTERN  = r"""[a-zA-Z_]*(?P<version>[\d.]*)[.][a-zA-Z.]*"""

