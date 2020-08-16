import yaml
class YamlHandler:

    def __init__(self,pstr_file_path):
        '''
        Read the YAML File
        :param pstr_file_path: Path of the YAML File
        '''
        with open(pstr_file_path,mode='r') as file:
            self.documents = yaml.full_load(file)
            print(self.documents)

    def get_property(self,property_name):
        '''
        Returns the value of the property
        :param property_name: name of the property
        :return: Value of the property
        '''
        try:
            return self.documents.get(property_name)
        except Exception as e:
            raise Exception("Error while fetching value of the property -->",property_name,"-->",e)

    def get_base_config(self):
        '''
        Returns the base config file
        :return:
        '''
        try:
            return self.documents
        except Exception as e:
            raise Exception("error while fetching the base Config -->",e)

    def base_config_parameters(self):
        '''
        Returns the Config paramters
        :return: Config parameters
        '''
        try:
            return self.get_base_config()[self.get_base_config()["env"]]
        except Exception as e:
            raise Exception("error while fetching the Config parameters from base config -->",e)

    def get_user_credentials(self,pstr_user_type="default_user"):
        try:
            username = self.get_base_config()[self.get_base_config()["env"]][pstr_user_type]["username"]
            password = self.get_base_config()[self.get_base_config()["env"]][pstr_user_type]["password"]
            return username,password
        except Exception as e:
            raise Exception("Error occured while fetching user credentials from config file -->",e)

    def get_base_url(self):
        try:
            return self.get_base_config()[self.get_base_config()["env"]]["url"]
        except Exception as e:
            raise Exception("Error occured while fetching base url from config file -->",e)

    def get_browser_config(self):
        try:
            return self.get_base_config()["browser"]
        except Exception as e:
            raise Exception("Error occured while fetching browser type  from config file -->",e)

    def get_applicaiton_path(self):
        try:
            application_path = self.get_base_config()["mobile"][self.get_base_config()["operating_system"]]["application_path"]
            print("appication path is :",application_path)
            return application_path
        except Exception as e:
            raise Exception("Error occured while fetching mobile applicaiton path from config file -->",e)

