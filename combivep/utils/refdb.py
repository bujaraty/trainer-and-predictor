import subprocess
import os
import re
import zipfile
import combivep.config as combivep_config

def unzip(zip_file, out_dir):
    unzip_files = zipfile.ZipFile(zip_file)
    out_files = []
    for unzip_file in unzip_files.namelist():
        (dir_name, file_name) = os.path.split(unzip_file)
        zip_out_dir = os.path.join(out_dir, dir_name)
        if not os.path.exists(zip_out_dir):
            os.makedirs(zip_out_dir)
        out_file  = os.path.join(zip_out_dir, file_name)
        zip_file  = os.path.join(dir_name, file_name)
        if not out_file.endswith('/'):
            fd = open(out_file,"w")
            fd.write(unzip_files.read(zip_file))
            fd.close()
            out_files.append(out_file)
    return out_files

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


    def __init__(self, working_dir=combivep_config.COMBIVEP_UPDATER_WORKING_DIR):
        #common configuration
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
        self.working_dir = working_dir

        #specific configuration
        #URL of the folder that contain target files
        self.folder_url       = None
        #pattern to find each target file
        self.files_pattern    = None
        #pattern to find the version in the file name
        self.version_pattern  = None
        #directory to store (new) reference DB
        self.local_ref_db_dir = None

        self.tmp_file         = 'tmp_list'
        self.new_file         = None

    def update(self, last_version):
        if self.local_ref_db_dir and (not os.path.exists(self.local_ref_db_dir)):
            os.makedirs(self.local_ref_db_dir)
        if not self.__ready():
            return False
        tmp_list_file  = os.path.join(self.working_dir, self.tmp_file)
#        self.download(self.folder_url,
#                      self.working_dir,
#                      output_file_name=tmp_list_file)
        files_list  = self.parse(tmp_list_file)
        max_version = max(sorted(files_list.keys()))
        if max_version <= last_version:
            return False
        else:
            error = self.download(os.path.join(self.folder_url, 
                                               files_list[max_version]),
                                  self.local_ref_db_dir)
            self.new_file = os.path.join(self.local_ref_db_dir, files_list[max_version])
            return self.new_file

    def parse(self, list_file):
        out          = {}
        files_parser = re.compile(self.files_pattern)
        matches      = files_parser.finditer(open(list_file).read())
        for match in matches:
            version_parser  = re.compile(self.version_pattern)
            version         = version_parser.match(match.group('file_name')).group('version')
            out[version]    = match.group('file_name')
        return out

    def __ready(self):
        return self.folder_url and self.files_pattern and self.version_pattern


class UcscUpdater(Updater):


    def __init__(self, working_dir):
        #common configuration
        Updater.__init__(self, working_dir)

        #specific configuration
        self.folder_url       = combivep_config.UCSC_FOLDER_URL
        self.files_pattern    = combivep_config.UCSC_FILES_PATTERN
        self.version_pattern  = combivep_config.UCSC_VERSION_PATTERN
        self.local_ref_db_dir = combivep_config.COMBIVEP_MASTER_UCSC_REF_DB_DIR


class LjbUpdater(Updater):


    def __init__(self, working_dir):
        #common configuration
        Updater.__init__(self, working_dir)

        #specific configuration
        self.folder_url      = combivep_config.LJB_FOLDER_URL
        self.files_pattern   = combivep_config.LJB_FILES_PATTERN
        self.version_pattern = combivep_config.LJB_VERSION_PATTERN
        self.local_ref_db_dir = combivep_config.COMBIVEP_MASTER_LJB_REF_DB_DIR

    def update(self, last_version):
        if not Updater.update(self, last_version):
            return False
        print self.new_file
        return True


class ScoresDatabase(object):
    """

    This database is to produce feature vectors and to aid cleaning data

    """


    def __init__(self):
        pass

    def update(self):
        pass

    def load(self):
        pass




