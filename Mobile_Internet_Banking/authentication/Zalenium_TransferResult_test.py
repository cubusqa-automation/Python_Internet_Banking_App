import os
import sys
import time

import pytest

sys.path.insert(0, os.path.join(os.getcwd(), '..', '..'))

from Mobile_Internet_Banking.helper.TestData import *
from selenium import webdriver


class Test_Zalenium_TransferResult:
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

        if general_data.deployment_Type == "cloud":
            if general_data.deployment_Environment == "osx":
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})

            elif general_data.deployment_Environment == "linux":
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})

            else:  # windows
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})

        else:  # on premise
            if general_data.deployment_Environment == "osx":
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/chromedriver")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/geckodriver")

            elif general_data.deployment_Environment == "linux":
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Linux/chromedriver")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Linux/geckodriver")

            else:  # windows
                if general_data.mobile_Browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/chromedriver.exe")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    options.add_argument("headless")
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/geckodriver.exe")

    @staticmethod
    def close_browser(self):
        self.driver.close()

    def test_TransferResult_Container_Server(self, startup):
        """
        time.sleep(60)

        self.driver.maximize_window()
        self.driver.get("http://192.168.200.170:8001/job/FT_Container_Server/build?token=FT_Container_Server")
        self.driver.find_element_by_xpath("//input[@id='j_username']").send_keys("superadmin")
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("@Cu2010bus")
        self.driver.find_element_by_xpath("//input[@name='Submit']").click()

        time.sleep(60)

        print("-----", self.driver.title, "-----")
        """
