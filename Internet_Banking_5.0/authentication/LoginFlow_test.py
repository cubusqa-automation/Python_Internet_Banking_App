from selenium import webdriver
import pytest
import logging
import time

logging.basicConfig(
    filename="../Logs/Authentication.log",
    format='%(asctime)s: %(levelname)s: %(message)s',
    level=logging.DEBUG)


class Test_LoginFlow:
    driver = None

    @pytest.yield_fixture()
    def startup(self):
        self.invoke_browser(self)
        yield
        self.close_browser(self)

    @staticmethod
    def invoke_browser(self):

        deployment_Type = "cloud"
        deployment_Environment = "osx"
        browser = "chrome"
        remote_Machine = 'http://localhost:4444/wd/hub'

        logging.info(
            "Started:Internet Banking Login Work Flow. FileName: LoginFlow_test.py, ClassName:Test_LoginFlow, TestName:test_LoginFlow")

        if deployment_Type == "cloud":
            if deployment_Environment == "osx":
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-OSX-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-OSX-Firefox Browser has been launched.")

            elif deployment_Environment == "linux":
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Linux-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Linux-Firefox Browser has been launched.")

            else:  # windows
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'chrome',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Windows-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Remote(command_executor=remote_Machine,
                                                   desired_capabilities={'browserName': 'firefox',
                                                                         'javascriptEnabled': True})
                    logging.debug("Cloud-Windows-Firefox Browser has been launched.")

        else:  # on premise
            if deployment_Environment == "osx":
                if browser == "chrome":
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
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/geckodriver")
                    logging.debug("On Premise-OSX-Firefox Browser has been launched.")

            elif deployment_Environment == "linux":
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/chromedriver")
                    logging.debug("On Premise-Linux-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/geckodriver")
                    # logging.debug("On Premise-Linux-Firefox Browser has been launched.")

            else:  # windows
                if browser == "chrome":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/OSX/chromedriver.exe")
                    logging.debug("On Premise-Windows-Chrome Browser has been launched.")

                else:  # firefox
                    options = webdriver.FirefoxOptions()
                    options.add_argument("--ignore-certificate-errors")
                    options.add_argument("--ignore-ssl-errors")
                    # options.add_experimental_option("detach", True)
                    self.driver = webdriver.Chrome(options=options,
                                                   executable_path="../Browser_Drivers/Windows/geckodriver.exe")
                    logging.debug("On Premise-Windows-Firefox Browser has been launched.")

        self.driver.maximize_window()
        self.driver.get("https://192.168.200.196:30642")
        logging.debug("Internet Banking URL has been passed to the browser.")
        time.sleep(5)

    @staticmethod
    def close_browser(self):
        self.driver.close()
        logging.info(
            "Ended:Internet Banking Login Work Flow. FileName: LoginFlow_test.py, ClassName:Test_LoginFlow, TestName:test_LoginFlow")

    def test_LoginFlow(self, startup):

        try:
            # UserName/Password Screen
            self.driver.find_element_by_xpath("//input[@name='username']").send_keys("cubusdemo")
            self.driver.find_element_by_xpath("//input[@name='password']").send_keys("@Cu2010bus")
            self.driver.find_element_by_xpath("//body/form/div[@id='LoginContainer']/input[1]").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//div[@class='containerBlock']//div//a//img").click()
            time.sleep(5)
        except Exception as e:
            logging.error("ERROR: Issue in --test_LoginFlow() Method.--", e)
