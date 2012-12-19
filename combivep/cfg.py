import os
import combivep.settings as combivep_settings


class Configure(object):
    """ CombiVEP base class """


    def __init__(self):
        self.config_file = combivep_settings.COMBIVEP_CONFIGURATION_FILE
        self.__values      = {}

    def load(self):
        self.__values.clear()
        f = open(self.config_file, 'r')
        for line in f:
            rec = line.strip().split('=')
            if rec[0] == combivep_settings.LATEST_UCSC_DATABASE_VERSION:
                self.__values[combivep_settings.LATEST_UCSC_DATABASE_VERSION] = rec[1]
            elif rec[0] == combivep_settings.LATEST_UCSC_FILE_NAME:
                self.__values[combivep_settings.LATEST_UCSC_FILE_NAME] = rec[1]
            elif rec[0] == combivep_settings.LATEST_LJB_DATABASE_VERSION:
                self.__values[combivep_settings.LATEST_LJB_DATABASE_VERSION] = rec[1]
            elif rec[0] == combivep_settings.LATEST_LJB_FILE_NAMES:
                self.__values[combivep_settings.LATEST_LJB_FILE_NAMES] = rec[1].split(',')
        return self.__values


    def save(self):
        f = open(self.config_file, 'w')
        f.write("%s=%s\n" % (combivep_settings.LATEST_UCSC_DATABASE_VERSION, self.__values[combivep_settings.LATEST_UCSC_DATABASE_VERSION]))
        f.write("%s=%s\n" % (combivep_settings.LATEST_UCSC_FILE_NAME, self.__values[combivep_settings.LATEST_UCSC_FILE_NAME]))
        f.write("%s=%s\n" % (combivep_settings.LATEST_LJB_DATABASE_VERSION, self.__values[combivep_settings.LATEST_LJB_DATABASE_VERSION]))
        f.write("%s=%s\n" % (combivep_settings.LATEST_LJB_FILE_NAMES, ','.join(self.__values[combivep_settings.LATEST_LJB_FILE_NAMES])))
        f.close()

    def write_ljb_config(self, version, file_list):
        self.__values[combivep_settings.LATEST_LJB_DATABASE_VERSION] = version
        self.__values[combivep_settings.LATEST_LJB_FILE_NAMES]       = file_list
        self.save()

    def write_ucsc_config(self, version, file_name):
        self.__values[combivep_settings.LATEST_UCSC_DATABASE_VERSION] = version
        self.__values[combivep_settings.LATEST_UCSC_FILE_NAME]        = file_name
        self.save()






