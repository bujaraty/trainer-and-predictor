import subprocess
import os
import re
import combivep.config as combivep_config

class Downloader:
    """to download file"""


    def __init__(self):
        pass

    def download(self, target_url, output_dir, output_file_name=None):
        """

        to download file from the target url and save it at the specified
        output directory

        """
        current_working_dir = os.getcwd()
        os.chdir(output_dir)
        args = []
        args.append('wget')
        args.append('-q')
        args.append('-N')
        if output_file_name:
            args.append('--output-document=%s' % (output_file_name))
        args.append(target_url)
        error_code = subprocess.call(args)
        os.chdir(current_working_dir)

        return error_code


class Updater(Downloader):


    def __init__(self, working_dir):
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
        self.__working_dir = working_dir

    def update(self, last_version,
                     folder_url,
                     files_pattern,
                     version_pattern,
                     tmp_file='tmp_list'):
        tmp_list_file  = os.path.join(self.__working_dir, tmp_file)
#        self.download(folder_url,
#                      self.__working_dir,
#                      output_file_name=tmp_list_file)
        files_list  = self.parse(tmp_list_file, files_pattern, version_pattern)
        max_version = max(sorted(files_list.keys()))
        if max_version <= last_version:
            return False
        else:
            error_code = self.download(os.path.join(folder_url, 
                                                    files_list[max_version]),
                                       combivep_config.COMBIVEP_MASTER_DB_DIR)
            return not error_code

    def parse(self, list_file, files_pattern, version_pattern):
        out          = {}
        files_parser = re.compile(files_pattern)
        matches      = files_parser.finditer(open(list_file).read())
        for match in matches:
            version_parser  = re.compile(version_pattern)
            version         = version_parser.match(match.group('file_name')).group('version')
            out[version]    = match.group('file_name')

        return out


#class UcscUpdater(Downloader):
#
#
#    def __init__(self, working_dir=combivep_config.COMBIVEP_UPDATER_WORKING_DIR):
#        if not os.path.exists(working_dir):
#            os.makedirs(working_dir)
#        self.__working_dir = working_dir
#
#    def update(self, last_version,
#                     ucsc_folder=combivep_config.UCSC_FOLDER_URL,
#                     file_pattern=combivep_config.UCSC_FILE_PATTERN):
#        list_file  = os.path.join(self.__working_dir, combivep_config.UCSC_LIST_FILE_NAME)
##        self.download(ucsc_folder,
##                      self.__working_dir,
##                      output_file_name=list_file)
#        file_names  = self.parse(list_file, file_pattern)
#        max_version = max(sorted(file_names.keys()))
#        if max_version <= last_version:
#            return False
#        else:
#            error_code = self.download(os.path.join(combivep_config.UCSC_FOLDER_URL, file_names[max_version]),
#                                       combivep_config.COMBIVEP_MASTER_DB_DIR)
#            return not error_code
#
#    def parse(self, file_name, file_pattern):
#        out         = {}
#        file_parser = re.compile(file_pattern)
#        matches     = file_parser.finditer(open(file_name).read())
#        for match in matches:
#            name_parser  = re.compile(r"""[a-zA-Z]*(?P<version>[\d]*)[a-zA-Z.]*""")
#            version      = name_parser.match(match.group('filename')).group('version')
#            out[version] = match.group('filename')
#
#        return out

#class LjbUpdater(Downloader):
#
#
#    def __init__(self, working_dir=combivep_config.COMBIVEP_UPDATER_WORKING_DIR):
#        if not os.path.exists(working_dir):
#            os.makedirs(working_dir)
#        self.__working_dir = working_dir
#
#    def update(self, last_version,
#                     ljb_folder=combivep_config.LJB_FOLDER_URL,
#                     file_pattern=combivep_config.LJB_FILE_PATTERN):
#        list_file  = os.path.join(self.__working_dir, combivep_config.LJB_LIST_FILE_NAME)
##        self.download(ucsc_folder,
##                      self.__working_dir,
##                      output_file_name=list_file)
#        file_names  = self.parse(list_file, file_pattern)
#        max_version = max(sorted(file_names.keys()))
#        if max_version <= last_version:
#            return False
#        else:
#            error_code = self.download(os.path.join(combivep_config.UCSC_FOLDER_URL, file_names[max_version]),
#                                       combivep_config.COMBIVEP_MASTER_DB_DIR)
#            return not error_code






