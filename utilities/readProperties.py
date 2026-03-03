import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():  # ✅ No 'self' param for staticmethod
        return config.get('common info', 'baseURL')

    @staticmethod
    def getFirstname():
        return config.get('common info', 'firstname')

    @staticmethod
    def getLastname():
        return config.get('common info', 'lastname')

    @staticmethod
    def getEmail():
        return config.get('common info', 'email')

    @staticmethod
    def getAddress1():
        return config.get('common info', 'address1')

    @staticmethod
    def getCity():
        return config.get('common info', 'city')

    @staticmethod
    def getCountry():
        return config.get('common info', 'country_name')

    @staticmethod
    def getState():
        return config.get('common info', 'state_name')

    @staticmethod
    def getZipcode():
        return config.get('common info', 'zipcode')

    @staticmethod
    def getLoginname():
        return config.get('common info', 'login_name')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')

    @staticmethod
    def getConfirmPassword():
        return config.get('common info', 'confirm_password')
