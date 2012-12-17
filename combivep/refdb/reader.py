import pysam
import combivep.config as combivep_config
import combivep.template as template


class UcscReader(template.CombiVEPBase):
    """to read UCSC file in tabix format"""


    def read(self, tabix_file):
        self.file_name = tabix_file

    def fetch_snps(self, chromosome, start_pos, end_pos):
        tabix_file = pysam.Tabixfile(self.file_name)
        if chromosome.isdigit():
            chrom = 'chr' + chromosome
        else:
            chrom = chromosome
        for line in tabix_file.fetch(chrom, start_pos, end_pos):
            rec = line.rstrip('\n').split('\t')
            if len(rec) != combivep_config.UCSC_EXPECTED_LENGTH :
                raise Exception("Invalid formatting is found in file '%s'>> Chrom : %s\tStart pos : %s\tEnd pos : %s" % (self.file_name, rec[combivep_config.UCSC_INDEX_CHROM], rec[combivep_config.UCSC_INDEX_START_POS], rec[combivep_config.UCSC_INDEX_END_POS]))
            yield {combivep_config.CHROM     : rec[combivep_config.UCSC_INDEX_CHROM], 
                   combivep_config.START_POS : rec[combivep_config.UCSC_INDEX_START_POS],
                   combivep_config.END_POS   : rec[combivep_config.UCSC_INDEX_END_POS],
                   combivep_config.STRAND    : rec[combivep_config.UCSC_INDEX_STRAND],
                   combivep_config.REF       : rec[combivep_config.UCSC_INDEX_REF],
                   combivep_config.OBSERVED  : rec[combivep_config.UCSC_INDEX_OBSERVED],
                   }


class LjbReader(template.CombiVEPBase):
    """to read LJB file"""


    def read(self, tabix_file):
        self.file_name = tabix_file

    def fetch_snps(self):
        for line in open(self.file_name):
            rec = line.rstrip().split('\t')
            if len(rec) != combivep_config.LJB_EXPECTED_LENGTH :
                raise Exception("Invalid formatting is found in file '%s'>> Chrom : %s\tStart pos : %s" % (self.file_name, rec[combivep_config.LJB_INDEX_CHROM], rec[combivep_config.LJB_INDEX_START_POS]))
            yield {combivep_config.CHROM        : 'chr'+rec[combivep_config.LJB_INDEX_CHROM], 
                   combivep_config.START_POS    : str(int(rec[combivep_config.LJB_INDEX_START_POS])-1),
                   combivep_config.END_POS      : rec[combivep_config.LJB_INDEX_START_POS],
                   combivep_config.ALT          : rec[combivep_config.LJB_INDEX_ALT],
                   combivep_config.REF          : rec[combivep_config.LJB_INDEX_REF],
                   combivep_config.PHYLOP_SCORE : rec[combivep_config.LJB_INDEX_PHYLOP_SCORE],
                   combivep_config.SIFT_SCORE   : rec[combivep_config.LJB_INDEX_SIFT_SCORE],
                   combivep_config.PP2_SCORE    : rec[combivep_config.LJB_INDEX_PP2_SCORE],
                   combivep_config.LRT_SCORE    : rec[combivep_config.LJB_INDEX_LRT_SCORE],
                   combivep_config.MT_SCORE     : rec[combivep_config.LJB_INDEX_MT_SCORE],
                   combivep_config.GERP_SCORE   : rec[combivep_config.LJB_INDEX_GERP_SCORE],
                   }










