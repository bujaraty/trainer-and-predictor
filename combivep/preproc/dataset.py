import math
import random
import combivep.template as main_template
import combivep.settings as combivep_settings
import combivep.preproc.reader as combivep_reader
import combivep.preproc.referer as combivep_referer


class DatasetManager(main_template.CombiVEPBase):


    def __init__(self):
        main_template.CombiVEPBase.__init__(self)

        self.referer = combivep_referer.Referer()
        self.referer.load_config()

        self.array_data = []
        self.shuffle_seed = None
        self.__clear_data()

    def __clear_data(self):
        del self.array_data[:]
#        self.validated  = False
#        self.has_scores = False

    def load_data(self, file_name, file_type='VCF'):
        if file_type == 'VCF':
            return self.__load_vcf_data(file_name)

    def __load_vcf_data(self, file_name):
        self.__clear_data()
        vcf_reader = combivep_reader.VcfReader()
        vcf_reader.read(file_name)
        for rec in vcf_reader.fetch_hash_snps():
            snp_data = {combivep_settings.KEY_CHROM : rec[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_VCF_CHROM],
                        combivep_settings.KEY_POS   : rec[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_VCF_POS],
                        combivep_settings.KEY_REF   : rec[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_VCF_REF],
                        combivep_settings.KEY_ALT   : rec[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_VCF_ALT],
                        }
            self.array_data.append({combivep_settings.KEY_SNP_INFO_SECTION : snp_data})

    def validate_data(self):
        #remove items from self.array_data if they are not valid
        self.array_data[:] = [item for item in self.array_data if self.referer.validate_snp(item[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_CHROM],
                                                                                            item[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_POS],
                                                                                            item[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_REF],
                                                                                            item[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_ALT]
                                                                                            )]

    def calculate_scores(self):
        #get scores from LJB database
        for item in self.array_data:
            item[combivep_settings.KEY_SCORES_SECTION] = self.referer.get_scores(item[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_CHROM],
                                                                                 item[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_POS],
                                                                                 item[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_REF],
                                                                                 item[combivep_settings.KEY_SNP_INFO_SECTION][combivep_settings.KEY_ALT]
                                                                                 )
        #remove items from self.array_data if they don't have scores
        self.array_data[:] = [item for item in self.array_data if item[combivep_settings.KEY_SCORES_SECTION] is not None]

    def shuffle_data(self):
        random.seed(self.shuffle_seed)
        random.shuffle(self.array_data)

    def partition_data(self,
                       proportion_training_data   = combivep_settings.PROPORTION_TRAINING_DATA,
                       proportion_validation_data = combivep_settings.PROPORTION_VALIDATION_DATA,
                       proportion_test_data       = combivep_settings.PROPORTION_TEST_DATA,
                       ):
        total_proportion = proportion_training_data + proportion_validation_data + proportion_test_data
        self.training_data_size   = int(math.floor(len(self.array_data) * proportion_training_data / total_proportion))
        self.validation_data_size = int(math.floor(len(self.array_data) * proportion_validation_data / total_proportion))
        self.test_data_size       = len(self.array_data) - self.training_data_size - self.validation_data_size

    def fetch_training_data(self):
#        print self.array_data(0:self.training_data_size)
        for i in  xrange(0, self.training_data_size):
            yield self.array_data[i]

    def fetch_validation_data(self):
        for i in xrange(self.training_data_size, self.training_data_size + self.validation_data_size):
            yield self.array_data[i]

    def fetch_test_data(self):
        for i in xrange(self.training_data_size + self.validation_data_size, len(self.array_data)):
            yield self.array_data[i]






