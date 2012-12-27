import os

"""

This module is all about constant value that are used in this application

"""

DEBUG_MODE = 0

# > > > > > > > > > > > > > development files & folders < < < < < < < < < <
PROJECT_ROOT                      = os.path.dirname(os.path.dirname(__file__))

#'central' data for testing and for demo. 'central' is for preventing redundancy
COMBIVEP_CENTRAL_TEST_DATA_ROOT   = os.path.join(PROJECT_ROOT, 'combivep/data')
COMBIVEP_CENTRAL_TEST_DATASET_DIR = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'dataset')
COMBIVEP_CENTRAL_TEST_VCF_DIR     = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'vcf')
COMBIVEP_CENTRAL_TEST_UCSC_DIR    = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'UCSC')
COMBIVEP_CENTRAL_TEST_LJB_DIR     = os.path.join(COMBIVEP_CENTRAL_TEST_DATA_ROOT, 'LJB')


# > > > > > > > > > > > > > User files & folders < < < < < < < < < <
USER_DATA_ROOT               = os.path.expanduser('~/.CombiVEP')

#to keep user data produced by CombiVEP engine
USER_PARAMETERS_DIR          = os.path.join(USER_DATA_ROOT, 'params')
USER_PARAMETERS_FILE         = os.path.join(USER_PARAMETERS_DIR, 'params.npz')

#to keep the reference database from UCSC and LJB
USER_UCSC_REF_DB_DIR         = os.path.join(USER_DATA_ROOT, 'ref/UCSC')
USER_LJB_REF_DB_DIR          = os.path.join(USER_DATA_ROOT, 'ref/LJB')


# > > > > > > > > > > > > > status file < < < < < < < < < <
COMBIVEP_CONFIGURATION_FILE  = os.path.join(USER_DATA_ROOT, 'config.txt')

#key
LATEST_UCSC_DATABASE_VERSION = 'latest_ucsc_database_version'
LATEST_UCSC_FILE_NAME        = 'latest_ucsc_file_name'
LATEST_LJB_DATABASE_VERSION  = 'latest_ljb_database_version'
LATEST_LJB_FILE_PREFIX       = 'latest_ljb_file_prefix'


# > > > > > > > > > > > > > temporay files and folder < < < < < < < < < <
#the only temporay working folder used for processing data
COMBIVEP_WORKING_DIR         = os.path.join(USER_DATA_ROOT, 'tmp')

#temporary files for reference database processing
TMP_UCSC_CLEAN_DB_FILE       = os.path.join(COMBIVEP_WORKING_DIR, 'tmp_ucsc_clean_db.txt')
TMP_LJB_CLEAN_DB_FILE        = os.path.join(COMBIVEP_WORKING_DIR, 'tmp_ljb_clean_db.txt')


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

#proportion of data partitioning
PROPORTION_TRAINING_DATA   = 70
PROPORTION_VALIDATION_DATA = 15
PROPORTION_TEST_DATA       = 15


# > > > > > > > > > > > > > Demo configuration < < < < < < < < < <
DEMO_SEED = 20


# > > > > > > > > > > > > > reference database configuration < < < < < < < < < <
#UCSC
UCSC_FOLDER_URL      = 'http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database'
UCSC_LIST_FILE_NAME  = 'ucsc_list_file'
UCSC_FILES_PATTERN   = r"""href="(?P<file_name>snp\d{3}.txt.gz)">.*>.*(?P<date>\d{2}-[a-zA-Z]{3}-\d{4})"""
UCSC_VERSION_PATTERN = r"""[a-zA-Z]*(?P<version>[\d]*)[a-zA-Z.]*"""

#LJB
LJB_FOLDER_URL       = 'http://dbnsfp.houstonbioinformatics.org/dbNSFPzip/'
LJB_LIST_FILE_NAME   = 'ljb_list_file'
LJB_FILES_PATTERN    = r"""href="(?P<file_name>dbNSFP_light.*.zip)">"""
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
#0-based index, used by python
UCSC_0_INDEX_CHROM     = 1
UCSC_0_INDEX_START_POS = 2
UCSC_0_INDEX_END_POS   = 3
UCSC_0_INDEX_STRAND    = 6
UCSC_0_INDEX_REF       = 8
UCSC_0_INDEX_OBSERVED  = 9
UCSC_EXPECTED_LENGTH   = 26


# > > > > > > > > > > > > > Dataset data structure < < < < < < < < < <
#key
KEY_SNP_INFO_SECTION      = 'snp_info'
KEY_SCORES_SECTION        = 'scores'
#KEY_TARGET_VALUE  = 'target_value'

#global SNP information key
KEY_CHROM = 'chrom'
KEY_POS   = 'pos'
KEY_REF   = 'ref'
KEY_ALT   = 'alt'


# > > > > > > > > > > > > > LJB format configuration < < < < < < < < < <
#SNP information key
KEY_LJB_CHROM     = 'ljb_chrom'
KEY_LJB_POS       = 'ljb_hg19_pos'
KEY_LJB_REF       = 'ljb_ref'
KEY_LJB_ALT       = 'ljb_alt'

#score key
KEY_PHYLOP_SCORE = 'phylop_score'
KEY_SIFT_SCORE   = 'sift_score'
KEY_PP2_SCORE    = 'pp2_score'
KEY_LRT_SCORE    = 'lrt_score'
KEY_MT_SCORE     = 'mt_score'
KEY_GERP_SCORE   = 'gerp_score'

#LJB index
#1-based index, used by awk for parsing
LJB_RAW_1_INDEX_CHROM        = 1
LJB_RAW_1_INDEX_POS          = 7
LJB_RAW_1_INDEX_REF          = 3
LJB_RAW_1_INDEX_ALT          = 4
LJB_RAW_1_INDEX_PHYLOP_SCORE = 8
LJB_RAW_1_INDEX_SIFT_SCORE   = 9
LJB_RAW_1_INDEX_PP2_SCORE    = 10
LJB_RAW_1_INDEX_LRT_SCORE    = 11
LJB_RAW_1_INDEX_MT_SCORE     = 13
LJB_RAW_1_INDEX_GERP_SCORE   = 17

#0-based index, used by python for reading
LJB_PARSED_0_INDEX_CHROM        = 0
LJB_PARSED_0_INDEX_POS          = 1
LJB_PARSED_0_INDEX_REF          = 2
LJB_PARSED_0_INDEX_ALT          = 3
LJB_PARSED_0_INDEX_PHYLOP_SCORE = 4
LJB_PARSED_0_INDEX_SIFT_SCORE   = 5
LJB_PARSED_0_INDEX_PP2_SCORE    = 6
LJB_PARSED_0_INDEX_LRT_SCORE    = 7
LJB_PARSED_0_INDEX_MT_SCORE     = 8
LJB_PARSED_0_INDEX_GERP_SCORE   = 9
LJB_PARSED_EXPECTED_LENGTH      = 10


# > > > > > > > > > > > > > VCF format configuration < < < < < < < < < <
#SNP information key
KEY_VCF_CHROM = 'vcf_chrom'
KEY_VCF_POS   = 'vcf_pos'
KEY_VCF_REF   = 'vcf_ref'
KEY_VCF_ALT   = 'vcf_ALT'

#VCF index
#0-based index, used by python
VCF_0_INDEX_CHROM = 0
VCF_0_INDEX_POS   = 1
VCF_0_INDEX_REF   = 3
VCF_0_INDEX_ALT   = 4



