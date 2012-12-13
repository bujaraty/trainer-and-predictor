import os.path
import vcf


class PreProc(object):
    """

    a class to load raw data and preprocess it so that it can be used by
    CombiVEP and Condel

    """

    def __init__(self):
        pass

    def load_vcf(self, vcf_file):
        vcf_reader = vcf.Reader(open(vcf_file, 'r'))
        for record in vcf_reader:
            pass
#            print "%10s%12s%12s%10s%10s" % (record.CHROM, record.POS, record.POS, record.REF, record.ALT)
#            print record.samples


