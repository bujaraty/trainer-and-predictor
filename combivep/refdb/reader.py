import pysam
import combivep.settings as combivep_settings
import combivep.template as template


class UcscReader(template.CombiVEPBase):
    """to read UCSC parsed file in tabix format"""

    def __init__(self):
        template.CombiVEPBase.__init__(self)

    def read(self, tabix_file):
        self.db_file_name = tabix_file

    def fetch_array_snps(self, chromosome, start_pos, end_pos):
        tabix_file = pysam.Tabixfile(self.db_file_name)
        if chromosome.isdigit():
            chrom = 'chr' + chromosome
        else:
            chrom = chromosome
        for line in tabix_file.fetch(chrom, start_pos, end_pos):
            yield line.rstrip('\n').split('\t')

    def fetch_hash_snps(self, chromosome, start_pos, end_pos):
        for rec in self.fetch_array_snps(chromosome, start_pos, end_pos):
            if len(rec) != combivep_settings.UCSC_EXPECTED_LENGTH :
                raise Exception("Invalid formatting is found in file '%s'>> Chrom : %s\tStart pos : %s\tEnd pos : %s" % (self.db_file_name, rec[combivep_settings.UCSC_0_INDEX_CHROM], rec[combivep_settings.UCSC_0_INDEX_START_POS], rec[combivep_settings.UCSC_0_INDEX_END_POS]))
            yield {combivep_settings.KEY_UCSC_CHROM     : rec[combivep_settings.UCSC_0_INDEX_CHROM], 
                   combivep_settings.KEY_UCSC_START_POS : rec[combivep_settings.UCSC_0_INDEX_START_POS],
                   combivep_settings.KEY_UCSC_END_POS   : rec[combivep_settings.UCSC_0_INDEX_END_POS],
                   combivep_settings.KEY_UCSC_STRAND    : rec[combivep_settings.UCSC_0_INDEX_STRAND],
                   combivep_settings.KEY_UCSC_REF       : rec[combivep_settings.UCSC_0_INDEX_REF],
                   combivep_settings.KEY_UCSC_OBSERVED  : rec[combivep_settings.UCSC_0_INDEX_OBSERVED],
#                   combivep_settings.JOIN_KEY  : rec[combivep_settings.UCSC_PARSED_INDEX_CHROM]+'|'+rec[combivep_settings.UCSC_PARSED_INDEX_START_POS],
                   }


class LjbReader(template.CombiVEPBase):
    """to read parsed LJB file"""


    def __init__(self):
        template.CombiVEPBase.__init__(self)

    def read(self, ljb_file):
        self.db_file_name = ljb_file

    def fetch_array_snps(self, chromosome, start_pos, end_pos):
        tabix_file = pysam.Tabixfile(self.db_file_name)
        for line in tabix_file.fetch(chromosome, start_pos, end_pos):
            yield line.rstrip('\n').split('\t')

    def fetch_hash_snps(self, chromosome, start_pos, end_pos):
        for rec in self.fetch_array_snps(chromosome, start_pos, end_pos):
            if len(rec) != combivep_settings.LJB_PARSED_EXPECTED_LENGTH :
                raise Exception("Invalid formatting is found in file '%s'>> Chrom : %s\tStart pos : %s\tEnd pos : %s" % (self.db_file_name, rec[combivep_settings.LJB_0_INDEX_CHROM], rec[combivep_settings.LJB_PARSED_INDEX_START_POS], rec[combivep_settings.LJB_PARSED_INDEX_END_POS]))
            yield {combivep_settings.KEY_LJB_CHROM     : rec[combivep_settings.LJB_PARSED_0_INDEX_CHROM],
                   combivep_settings.KEY_LJB_START_POS : rec[combivep_settings.LJB_PARSED_0_INDEX_START_POS],
                   combivep_settings.KEY_LJB_ALT       : rec[combivep_settings.LJB_PARSED_0_INDEX_ALT],
                   combivep_settings.KEY_LJB_REF       : rec[combivep_settings.LJB_PARSED_0_INDEX_REF],
                   combivep_settings.PHYLOP_SCORE      : rec[combivep_settings.LJB_PARSED_0_INDEX_PHYLOP_SCORE],
                   combivep_settings.SIFT_SCORE        : rec[combivep_settings.LJB_PARSED_0_INDEX_SIFT_SCORE],
                   combivep_settings.PP2_SCORE         : rec[combivep_settings.LJB_PARSED_0_INDEX_PP2_SCORE],
                   combivep_settings.LRT_SCORE         : rec[combivep_settings.LJB_PARSED_0_INDEX_LRT_SCORE],
                   combivep_settings.MT_SCORE          : rec[combivep_settings.LJB_PARSED_0_INDEX_MT_SCORE],
                   combivep_settings.GERP_SCORE        : rec[combivep_settings.LJB_PARSED_0_INDEX_GERP_SCORE],
#                   combivep_settings.JOIN_KEY     : 'chr'+rec[combivep_settings.LJB_PARSED_INDEX_CHROM]+'|'+str(int(rec[combivep_settings.LJB_PARSED_INDEX_START_POS])-1),
                   }









