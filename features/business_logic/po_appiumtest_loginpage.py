from features.business_logic.locators.appiumtest_loginpage import ATLoginPageLocaters
from features.common_utilities.yaml_handler import YamlHandler
from features.common_utilities.file_folder_constants import FileFolderConstants
from features.common_utilities.driver_handler import DriverHandle
import time
import pytest

class ATLoginaPage():


    def __init__(self):

        self.loginpage_locaters = ATLoginPageLocaters()
        self.config_data = YamlHandler(FileFolderConstants.CONFIG_FILE)
        self.driver_handler = DriverHandle()



    def login(self,pstr_user="default_user"):
        try:
            time.sleep(3)
            username,password = self.config_data.get_user_credentials(pstr_user)
            self.driver_handler.send_keys(self.loginpage_locaters.username_textbox, username)
            self.driver_handler.send_keys(self.loginpage_locaters.password_textbox, password)
            self.driver_handler.click_element(self.loginpage_locaters.submit_btn)
        except Exception as e:
            raise Exception("Exception occured while login -->",e)