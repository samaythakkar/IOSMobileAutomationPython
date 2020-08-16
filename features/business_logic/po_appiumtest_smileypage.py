from features.business_logic.locators.appiumtest_smileypage import ATSmileyPageLocaters
from features.common_utilities.yaml_handler import YamlHandler
from features.common_utilities.file_folder_constants import FileFolderConstants
from features.common_utilities.driver_handler import DriverHandle
import time

class ATSmileyPage:

    def __init__(self):

        self.smileypage_locaters = ATSmileyPageLocaters()
        self.config_data = YamlHandler(FileFolderConstants.CONFIG_FILE)
        self.driver_handler = DriverHandle()

    def is_smiley_visible(self):
        try:
            return self.driver_handler.is_element_visible(self.smileypage_locaters.smiley_element)
        except Exception as e:
            raise Exception("Exception occured while checking if the smiley is visible -->",e)
