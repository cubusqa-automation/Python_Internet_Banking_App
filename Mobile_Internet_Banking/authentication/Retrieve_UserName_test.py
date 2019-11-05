import os
import sys
import pytest
import logging
import time

sys.path.insert(0, os.path.join(os.getcwd(), '..', '..'))

from Mobile_Internet_Banking.helper.TestData import *
from Mobile_Internet_Banking.Object_Repository.Mobile_Object_Repository import *
from selenium import webdriver

logging.basicConfig(
    filename="../Logs/Authentication.log",
    format='%(asctime)s: %(levelname)s: %(message)s',
    level=logging.DEBUG)

class Test_Retrieve_UserName:
    driver = None

    @pytest.yield_fixture()
    def startup(self):
        self.invoke_browser(self)
        yield
        self.close_browser(self)

    @staticmethod
    def invoke_browser(self):
        test_data = TestData()
        general_data = test_data.get_general_test_data()

        logging.info("Start:Internet Banking Retrieve User Name Flow. FileName: Retrieve_UserName_test.py, ClassName:Test_Retrieve_UserName, TestName:test_Retrieve_UserName")
        if general_data.deployment_Type == "cloud":
            if general_data.deployment_Environment == "osx":
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-OSX-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    #options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-OSX-Firefox Browser has been launched.")

            elif general_data.deployment_Environment == "linux":
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Linux-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    #options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Linux-Firefox Browser has been launched.")

            else:  # windows
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Windows-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    #options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Windows-Firefox Browser has been launched.")

        else:  # on premise
            if general_data.deployment_Environment == "osx":
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/chromedriver")
                    logging.debug("On Premise-OSX-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    #options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/geckodriver")
                    logging.debug("On Premise-OSX-Firefox Browser has been launched.")

            elif general_data.deployment_Environment == "linux":
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Linux/chromedriver")
                    logging.debug("On Premise-Linux-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    #options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Linux/geckodriver")
                    logging.debug("On Premise-Linux-Firefox Browser has been launched.")

            else:  # windows
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/chromedriver.exe")
                    logging.debug("On Premise-Windows-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    #options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/geckodriver.exe")
                    logging.debug("On Premise-Windows-Firefox Browser has been launched.")

        self.driver.maximize_window()
        self.driver.get(general_data.mobile_URL)
        logging.debug("Internet Banking URL has been passed to the browser.")
        time.sleep(5)

    @staticmethod
    def close_browser(self):
        self.driver.close()
        logging.info("End:Internet Banking Retrieve User Name Flow. FileName: Retrieve_UserName_test.py, ClassName:Test_Retrieve_UserName, TestName:test_Retrieve_UserName")

    def test_Retrieve_UserName(self, startup):

        try:
            test_Login_data = TestData()
            login_data = test_Login_data.get_authentication_test_data()

            mobile_signIn_screen = Mobile_SignIn(self.driver)
            mobile_signIn_screen.click_retrieve_user_name_link()

            time.sleep(10)

            mobile_retrieve_user_name = Mobile_ForgotUsername(self.driver)
            mobile_retrieve_user_name.enter_retrieve_user_name_captcha(login_data.retrieveUserName_MemberNo, "valid captcha")

            time.sleep(10)

            mobile_common = Mobile_Common(self.driver)
            mobile_common.click_submit_btn()

            time.sleep(10)

            retrieve_user_name_password = Mobile_RetrieveUsernamePasswordVerify(self.driver)
            retrieve_user_name_password.enter_retrieve_user_name_password(login_data.retrieveUserName_Password)

            time.sleep(10)

            mobile_common = Mobile_Common(self.driver)
            mobile_common.click_submit_btn()

            time.sleep(10)

        except Exception as e:
            logging.error("ERROR: Issue in --test_Retrieve_UserName() Method.--", e)



