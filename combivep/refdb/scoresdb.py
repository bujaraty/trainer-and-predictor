import combivep.settings as combivep_settings
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
#        tmp_buffer.append(combivep_settings.KEY_UCSC_CHROM)
#        tmp_buffer.append(combivep_settings.KEY_UCSC_START_POS)
#        tmp_buffer.append(combivep_settings.KEY_UCSC_END_POS)
#        tmp_buffer.append(combivep_settings.KEY_UCSC_STRAND)
#        tmp_buffer.append(combivep_settings.KEY_UCSC_REF)
#        tmp_buffer.append(combivep_settings.KEY_UCSC_OBSERVED)
        tmp_buffer.append(combivep_settings.KEY_LJB_CHROM)
        tmp_buffer.append(combivep_settings.KEY_LJB_START_POS)
        tmp_buffer.append(combivep_settings.KEY_LJB_REF)
        tmp_buffer.append(combivep_settings.KEY_LJB_ALT)
        tmp_buffer.append(combivep_settings.PHYLOP_SCORE)
        tmp_buffer.append(combivep_settings.SIFT_SCORE)
        tmp_buffer.append(combivep_settings.PP2_SCORE)
        tmp_buffer.append(combivep_settings.LRT_SCORE)
        tmp_buffer.append(combivep_settings.MT_SCORE)
        tmp_buffer.append(combivep_settings.GERP_SCORE)
        f.write('#' + '\t'.join(tmp_buffer) + '\n')

        #join by looking up ucsc file
        ucsc_rec      = {}
        file_buffer = []
        counter     = 0
        for ljb_rec in ljb_reader.fetch_snps():
            ucsc_rec.clear()
            tmp_buffer[:] = []
            for ucsc_rec in ucsc_reader.fetch_snps('chr'+ljb_rec[combivep_settings.KEY_LJB_CHROM],
                                                   int(ljb_rec[combivep_settings.KEY_LJB_START_POS])-2,
                                                   int(ljb_rec[combivep_settings.KEY_LJB_START_POS])-1):
                ucsc_alt = ucsc_rec[combivep_settings.KEY_UCSC_OBSERVED].split('/')
                if (ucsc_alt[0] != ljb_rec[combivep_settings.KEY_LJB_ALT]) and (ucsc_alt[1] != ljb_rec[combivep_settings.KEY_LJB_ALT]):
                    continue
#                tmp_buffer.append(ucsc_rec[combivep_settings.KEY_UCSC_CHROM])
#                tmp_buffer.append(ucsc_rec[combivep_settings.KEY_UCSC_START_POS])
#                tmp_buffer.append(ucsc_rec[combivep_settings.KEY_UCSC_END_POS])
#                tmp_buffer.append(ucsc_rec[combivep_settings.KEY_UCSC_STRAND])
#                tmp_buffer.append(ucsc_rec[combivep_settings.KEY_UCSC_REF])
#                tmp_buffer.append(ucsc_rec[combivep_settings.KEY_UCSC_OBSERVED])
                tmp_buffer.append(ljb_rec[combivep_settings.KEY_LJB_CHROM])
                tmp_buffer.append(ljb_rec[combivep_settings.KEY_LJB_START_POS])
                tmp_buffer.append(ljb_rec[combivep_settings.KEY_LJB_REF])
                tmp_buffer.append(ljb_rec[combivep_settings.KEY_LJB_ALT])
                tmp_buffer.append(ljb_rec[combivep_settings.PHYLOP_SCORE])
                tmp_buffer.append(ljb_rec[combivep_settings.SIFT_SCORE])
                tmp_buffer.append(ljb_rec[combivep_settings.PP2_SCORE])
                tmp_buffer.append(ljb_rec[combivep_settings.LRT_SCORE])
                tmp_buffer.append(ljb_rec[combivep_settings.MT_SCORE])
                tmp_buffer.append(ljb_rec[combivep_settings.GERP_SCORE])
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





