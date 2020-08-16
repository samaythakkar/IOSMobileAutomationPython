from pathlib import Path
from features.common_utilities.file_folder_constants import FileFolderConstants
import os
class PathProperties:

    def __get_project_root(self):
        try:
            project_root_path = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent  # This is your Project Root
            return project_root_path
        except Exception as e:
            raise Exception("Exception occured while getting the project root path -->",e)

    def get_config_path(self):
        try:
            config_path = os.path.join(self.__get_project_root(), FileFolderConstants.CONFIG_FILE)
            return config_path
        except Exception as e:
            raise Exception("Exception occured while getting the config path -->",e)

