import os.path

"""

Please don't change the value of DEBUG_MODE if you are in the production environment.
This value is for testing purpose.

"""
DEBUG_MODE = 0

# > > > > > > > > > > > > > permanent global data & folder < < < < < < < < < <
PROJECT_ROOT                      = os.path.dirname(os.path.dirname(__file__))

#to keep master data produced by application
COMBIVEP_MASTER_DATA_ROOT         = os.path.join(PROJECT_ROOT, 'dat')
COMBIVEP_MASTER_PARAMETERS_DIR    = os.path.join(COMBIVEP_MASTER_DATA_ROOT, 'params')
COMBIVEP_MASTER_PARAMETERS_FILE   = os.path.join(COMBIVEP_MASTER_PARAMETERS_DIR, 'params.npz')
COMBIVEP_MASTER_DB_DIR            = os.path.join(COMBIVEP_MASTER_DATA_ROOT, 'DB')

#to keep the new update file from UCSC and LJB
COMBIVEP_MASTER_UCSC_REF_DB_DIR   = os.path.join(COMBIVEP_MASTER_DB_DIR, 'ref/UCSC')
COMBIVEP_MASTER_LJB_REF_DB_DIR    = os.path.join(COMBIVEP_MASTER_DB_DIR, 'ref/LJB')

#the only temporay working folder used for processing data
COMBIVEP_UPDATER_WORKING_DIR      = os.path.join(COMBIVEP_MASTER_DB_DIR, 'tmp')

#to keep 'central' data for testing and for demo. 'central' is for preventing redundancy
COMBIVEP_CENTRAL_TEST_DATA_ROOT   = os.path.join(PROJECT_ROOT, 'combivep/data')
COMBIVEP_CENTRAL_TEST_DATASET_DIR = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'dataset')
COMBIVEP_CENTRAL_TEST_VCF_DIR     = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'vcf')
COMBIVEP_CENTRAL_TEST_UCSC_DIR    = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'UCSC')
COMBIVEP_CENTRAL_TEST_LJB_DIR     = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'LJB')


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


# > > > > > > > > > > > > > reference database configuration < < < < < < < < < <
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


# > > > > > > > > > > > > > UCSC format configuration < < < < < < < < < <
#general key
KEY_UCSC_CHROM     = 'ucsc_chrom'
KEY_UCSC_START_POS = 'ucsc_start_pos'
KEY_UCSC_END_POS   = 'ucsc_end_pos'
KEY_UCSC_STRAND    = 'ucsc_strand'
KEY_UCSC_REF       = 'ucsc_ref'
KEY_UCSC_OBSERVED  = 'ucsc_observed'

#UCSC index
UCSC_INDEX_CHROM     = 1
UCSC_INDEX_START_POS = 2
UCSC_INDEX_END_POS   = 3
UCSC_INDEX_STRAND    = 6
UCSC_INDEX_REF       = 8
UCSC_INDEX_OBSERVED  = 9
UCSC_EXPECTED_LENGTH = 26

# > > > > > > > > > > > > > LJB format configuration < < < < < < < < < <
#general key
KEY_LJB_CHROM     = 'ljb_chrom'
KEY_LJB_START_POS = 'ljb_start_pos'
KEY_LJB_REF       = 'ljb_ref'
KEY_LJB_ALT       = 'ljb_alt'

#score key
PHYLOP_SCORE = 'phylop_score'
SIFT_SCORE   = 'sift_score'
PP2_SCORE    = 'pp2_score'
LRT_SCORE    = 'lrt_score'
MT_SCORE     = 'mt_score'
GERP_SCORE   = 'gerp_score'

#LJB index
LJB_INDEX_CHROM        = 0
LJB_INDEX_START_POS    = 1
LJB_INDEX_REF          = 2
LJB_INDEX_ALT          = 3
LJB_INDEX_PHYLOP_SCORE = 4
LJB_INDEX_SIFT_SCORE   = 5
LJB_INDEX_PP2_SCORE    = 6
LJB_INDEX_LRT_SCORE    = 7
LJB_INDEX_MT_SCORE     = 8
LJB_INDEX_GERP_SCORE   = 9
LJB_EXPECTED_LENGTH    = 10


