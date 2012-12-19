#import os
#import re
import combivep.config as combivep_config
import combivep.refdb.updater as combivep_updater
import combivep.template as template
import combivep.refdb.reader as combivep_reader


class ScoresDB(template.CombiVEPBase):
    """

    This database is to produce feature vectors and to aid cleaning data

    """


    def __init__(self):
        pass

    def update(self):
        pass

    def load(self):
        pass

    def join(self, ljb_file, ucsc_file, output_file):
        """

        Input are two files
        - one is ljb file in normal text format
        - one is ucsc file in tabix format

        """
        #init LJB reader
        ljb_reader = combivep_reader.LjbReader()
        ljb_reader.read(ljb_file)

        #init UCSC reader
        ucsc_reader = combivep_reader.UcscReader()
        ucsc_reader.read(ucsc_file)

        #write file header
        f = open(output_file, 'w')
        tmp_buffer = []
        tmp_buffer.append(combivep_config.KEY_UCSC_CHROM)
        tmp_buffer.append(combivep_config.KEY_UCSC_START_POS)
        tmp_buffer.append(combivep_config.KEY_UCSC_END_POS)
        tmp_buffer.append(combivep_config.KEY_UCSC_STRAND)
        tmp_buffer.append(combivep_config.KEY_UCSC_REF)
        tmp_buffer.append(combivep_config.KEY_UCSC_OBSERVED)
        tmp_buffer.append(combivep_config.KEY_LJB_CHROM)
        tmp_buffer.append(combivep_config.KEY_LJB_START_POS)
        tmp_buffer.append(combivep_config.KEY_LJB_REF)
        tmp_buffer.append(combivep_config.KEY_LJB_ALT)
        tmp_buffer.append(combivep_config.PHYLOP_SCORE)
        tmp_buffer.append(combivep_config.SIFT_SCORE)
        tmp_buffer.append(combivep_config.PP2_SCORE)
        tmp_buffer.append(combivep_config.LRT_SCORE)
        tmp_buffer.append(combivep_config.MT_SCORE)
        tmp_buffer.append(combivep_config.GERP_SCORE)
        f.write('#' + '\t'.join(tmp_buffer) + '\n')

        #join by looking up ucsc file
        ucsc_rec      = {}
        file_buffer = []
        counter     = 0
        for ljb_rec in ljb_reader.fetch_snps():
            ucsc_rec.clear()
            tmp_buffer[:] = []
            for ucsc_rec in ucsc_reader.fetch_snps('chr'+ljb_rec[combivep_config.KEY_LJB_CHROM],
                                                   int(ljb_rec[combivep_config.KEY_LJB_START_POS])-2,
                                                   int(ljb_rec[combivep_config.KEY_LJB_START_POS])-1):
                tmp_buffer.append(ucsc_rec[combivep_config.KEY_UCSC_CHROM])
                tmp_buffer.append(ucsc_rec[combivep_config.KEY_UCSC_START_POS])
                tmp_buffer.append(ucsc_rec[combivep_config.KEY_UCSC_END_POS])
                tmp_buffer.append(ucsc_rec[combivep_config.KEY_UCSC_STRAND])
                tmp_buffer.append(ucsc_rec[combivep_config.KEY_UCSC_REF])
                tmp_buffer.append(ucsc_rec[combivep_config.KEY_UCSC_OBSERVED])
                tmp_buffer.append(ljb_rec[combivep_config.KEY_LJB_CHROM])
                tmp_buffer.append(ljb_rec[combivep_config.KEY_LJB_START_POS])
                tmp_buffer.append(ljb_rec[combivep_config.KEY_LJB_REF])
                tmp_buffer.append(ljb_rec[combivep_config.KEY_LJB_ALT])
                tmp_buffer.append(ljb_rec[combivep_config.PHYLOP_SCORE])
                tmp_buffer.append(ljb_rec[combivep_config.SIFT_SCORE])
                tmp_buffer.append(ljb_rec[combivep_config.PP2_SCORE])
                tmp_buffer.append(ljb_rec[combivep_config.LRT_SCORE])
                tmp_buffer.append(ljb_rec[combivep_config.MT_SCORE])
                tmp_buffer.append(ljb_rec[combivep_config.GERP_SCORE])
                file_buffer.append('\t'.join(tmp_buffer) + '\n')
                counter += 1
                if counter == 100:
                    f.write(''.join(file_buffer))
                    file_buffer[:] = []
                    counter        = 0
                break
        if counter > 0:
            f.write(''.join(file_buffer))
            file_buffer[:] = []
            counter        = 0
        f.close()

    def tabix(self, file_name):
        """to create the tabix index for UCSC SNPs file"""
        cmd = 'bgzip ' + file_name
        self.exec_sh(cmd)
        cmd = 'tabix -s 2 -b 3 -e 3 ' + file_name + '.gz'
        self.exec_sh(cmd)





