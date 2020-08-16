import pytest
# from selenium import webdriver
from appium import webdriver
from features.common_utilities.path_properties import PathProperties
from features.common_utilities.yaml_handler import YamlHandler
import allure
class Annotations:

    config_properties = YamlHandler(PathProperties().get_config_path())
    def common_config(self):
        """
        Description:
        	|  this method is to initialize the common_config

        """
        pytest.driver = None

    def before_scenario(self):
        """
        Description:
               	|  this method is to initialize webdriver and open browser
        """
        try:

            app = (
                self.config_properties.get_applicaiton_path())
            pytest.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'app': app,
                    'platformName': 'iOS',
                    'platformVersion': '13.6',
                    'deviceName': 'iPhone 8'
                }
            )

        except Exception as e:
            print('Error in before_scenario-->' + str(e))

    def pytest_take_screenshot(self):

        try:
            allure.attach(pytest.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print('Error in AFTER STEP-->' + str(e))

    def after_scenario(self):
        """
        Description:
                | This method is to initialize webdriver and open browser
        """
        # pytest.driver.close()