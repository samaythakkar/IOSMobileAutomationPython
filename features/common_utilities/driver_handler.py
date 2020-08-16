import os

from appium.webdriver.common import mobileby
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
import pytest
class DriverHandle():

    # config_file_properties = YamlHandler(PathProperties().get_config_path())



    def get_url(self,pstr_url):
        '''
        Open URL
        :param pstr_url: URL
        :return:
        '''
        try:
            pytest.driver.get(pstr_url)
        except Exception as e:
            raise Exception("Error occured while opening the url " + pstr_url + "-->", e)

    def send_keys(self,locater, pstr_text_to_send):
        '''
        Send keys to element
        :param locater: locater of element
        :param pstr_text_to_send: text to send to elemenet
        :return:
        '''
        try:
            self.wait_for_element_to_dispaly(locater)
            self.get_element(locater).send_keys(pstr_text_to_send)
        except Exception as e:
            raise Exception("Exception occured while sending text to element :", locater, "-->", e)

    def get_by(self, locater_type):
        try:
            if locater_type.lower() == "aid":
                locater_by = mobileby.MobileBy.ACCESSIBILITY_ID
            else:
                raise Exception("By of Locater not found for -->", locater_type)
            return locater_by
        except Exception as e:
            raise Exception("Error occurred while getting the by -->", e)

    def get_element(self, pstr_element_locater):
        try:
            split_locater = pstr_element_locater.split("=", 1)
            locater_type_by = self.get_by(split_locater[0])
            locater_identifer = split_locater[1]
            return pytest.driver.find_element(locater_type_by, locater_identifer)
        except Exception as e:
            raise Exception("Error occurred while getting the element :" + pstr_element_locater + "-->", e)


    def wait_for_element_to_dispaly(self,pstr_locater):
        try:
            WebDriverWait(pytest.driver, 20).until(EC.visibility_of(self.get_element(pstr_locater)))
        except Exception as e:
            raise Exception("Exception occured while waitinf for element to be located :",pstr_locater," --> ",e)

    def click_element(self,pstr_locater):
        try:
            self.wait_for_element_to_dispaly(pstr_locater)
            self.get_element(pstr_locater).click()
        except Exception as e:
            raise Exception("Exception occured while clicking element :",pstr_locater,"-->",e)

    def is_element_visible(self,pstr_locater):
        try:
            return self.get_element(pstr_locater).is_displayed()
        except Exception as e:
            raise Exception("Exception occured while checking if element :",pstr_locater," is visible -->",e)
