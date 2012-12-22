import subprocess
import sys
import os
import pysam
import combivep.settings as combivep_settings
import combivep.template as template
import combivep.refdb.reader as combivep_reader


class UcscController(combivep_reader.UcscReader):
    """UCSC database controller"""


    def __init__(self):
        #the raw db file is the output from updating process
        self.__raw_db_file         = None
        #the clean db file can be any temporary file.
        #this file connects the 'clean' and 'transform' processes
        self.__clean_db_file       = None


    def transform_database(self, file_name):
        """ interface for testing purpose """
        self.__raw_db_file = file_name
        self.__transform_database()

    def __transform_database(self):
        return self.__tabix(self.__raw_db_file)

    def __tabix(self, file_name):
        """ tabix into gz and tbi file """
        print >> sys.stderr, 'indexing ucsc database . . . . . '
        return pysam.tabix_index(file_name,
                                 force     = True,
                                 seq_col   = combivep_settings.UCSC_0_INDEX_CHROM,
                                 start_col = combivep_settings.UCSC_0_INDEX_START_POS,
                                 end_col   = combivep_settings.UCSC_0_INDEX_END_POS,
                                 zerobased = True)


class LjbController(combivep_reader.LjbReader):
    """LJB database controller"""


#    def __clean_raw_databases(self, in_files, out_files):
#        for i in xrange(len(in_files)):
#            self.__clean_raw_database(in_files[i], out_files[i])

    def clean_raw_database(self, input_file, output_file):
        """ interface for testing purpose """
        return self.__clean_raw_database(input_file, output_file)

    def __clean_raw_database(self, input_file, output_file):
        cmd = []
        #remove records that any of the scores are 'NA'
        cmd.append('awk -F\'\\t\' \'($')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_PHYLOP_SCORE))
        cmd.append(' !~ /[A-Z]/) && ($')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_SIFT_SCORE))
        cmd.append(' !~ /[A-Z]/) && ($')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_PP2_SCORE))
        cmd.append(' !~ /[A-Z]/) && ($')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_LRT_SCORE))
        cmd.append(' !~ /[A-Z]/) && ($')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_MT_SCORE))
        cmd.append(' !~ /[A-Z]/) && ($')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_GERP_SCORE))
        cmd.append(' !~ /[A-Z]/)\' ')
        cmd.append(input_file)
        #reformat the columns
        cmd.append(' | awk -F\'\\t\' \'{printf "%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\t%s\\n", $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_CHROM))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_START_POS))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_REF))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_ALT))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_PHYLOP_SCORE))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_SIFT_SCORE))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_PP2_SCORE))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_LRT_SCORE))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_MT_SCORE))
        cmd.append(', $')
        cmd.append(str(combivep_settings.LJB_RAW_1_INDEX_GERP_SCORE))
        cmd.append('}\' ')
        #redirect output to a file
        cmd.append(' > ')
        cmd.append(output_file)
        print >> sys.stderr, 'cleaning database . . . . . '
        return self.exec_sh(''.join(cmd))
#        return ''.join(cmd)

    def transform_database(self, file_name):
        """ interface for testing purpose """
        self.__transform_database(file_name)

    def __transform_database(self, file_name):
        return self.__tabix(file_name)

    def __tabix(self, file_name):
        """ tabix into gz and tbi file """
        print >> sys.stderr, 'indexing ljb database . . . . . '
        return pysam.tabix_index(file_name,
                                 force     = True,
                                 seq_col   = combivep_settings.LJB_PARSED_0_INDEX_CHROM,
                                 start_col = combivep_settings.LJB_PARSED_0_INDEX_START_POS,
                                 end_col   = combivep_settings.LJB_PARSED_0_INDEX_START_POS,
                                 zerobased = False)








