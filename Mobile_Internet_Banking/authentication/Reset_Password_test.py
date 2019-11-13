import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.getcwd(), '..', '..'))

from Mobile_Internet_Banking.helper.TestData import *
from Mobile_Internet_Banking.Object_Repository.Mobile_Object_Repository import *
from selenium import webdriver


@allure.testcase("Mobile Reset Password Test Case")
@allure.description(
    "Start:Internet Banking Reset Password Flow. FileName: Reset_Password.py, ClassName:Test_Reset_Password, TestName:test_Rest_Password")
class Test_Reset_Password:
    driver = None

    @pytest.yield_fixture()
    def startup(self):
        self.invoke_browser(self)
        yield
        self.close_browser(self)

    @staticmethod
    def invoke_browser(self):
        with allure.step("STEP-1: Call Mongo DB and get the Test Data."):
            test_data = TestData()
            general_data = test_data.get_general_test_data()

        with allure.step("STEP-2: Open a Browser"):

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

                    else:  # firefox
                        options = webdriver.FirefoxOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        # options.add_experimental_option("detach", True)
                        self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                       desired_capabilities={'browserName': 'firefox',
                                                                             'javascriptEnabled': True})

                elif general_data.deployment_Environment == "linux":
                    if general_data.mobile_Browser == "chrome":
                        options = webdriver.ChromeOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        options.add_experimental_option("detach", True)
                        self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                       desired_capabilities={'browserName': 'chrome',
                                                                             'javascriptEnabled': True})

                    else:  # firefox
                        options = webdriver.FirefoxOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        # options.add_experimental_option("detach", True)
                        self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                       desired_capabilities={'browserName': 'firefox',
                                                                             'javascriptEnabled': True})

                else:  # windows
                    if general_data.mobile_Browser == "chrome":
                        options = webdriver.ChromeOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        options.add_experimental_option("detach", True)
                        self.driver = webdriver.Remote(command_executor=general_data.remote_Machine,
                                                       desired_capabilities={'browserName': 'chrome',
                                                                             'javascriptEnabled': True})

                    else:  # firefox
                        options = webdriver.FirefoxOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        # options.add_experimental_option("detach", True)
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
                        self.driver = webdriver.Chrome(options=options,
                                                       executable_path="../Browser_Drivers/OSX/chromedriver")

                    else:  # firefox
                        options = webdriver.FirefoxOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        # options.add_experimental_option("detach", True)
                        self.driver = webdriver.Chrome(options=options,
                                                       executable_path="../Browser_Drivers/OSX/geckodriver")

                elif general_data.deployment_Environment == "linux":
                    if general_data.mobile_Browser == "chrome":
                        options = webdriver.ChromeOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        options.add_experimental_option("detach", True)
                        self.driver = webdriver.Chrome(options=options,
                                                       executable_path="../Browser_Drivers/Linux/chromedriver")

                    else:  # firefox
                        options = webdriver.FirefoxOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        # options.add_experimental_option("detach", True)
                        self.driver = webdriver.Chrome(options=options,
                                                       executable_path="../Browser_Drivers/Linux/geckodriver")

                else:  # windows
                    if general_data.mobile_Browser == "chrome":
                        options = webdriver.ChromeOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        options.add_experimental_option("detach", True)
                        self.driver = webdriver.Chrome(options=options,
                                                       executable_path="../Browser_Drivers/Windows/chromedriver.exe")

                    else:  # firefox
                        options = webdriver.FirefoxOptions()
                        options.add_argument("--ignore-certificate-errors")
                        options.add_argument("--ignore-ssl-errors")
                        # options.add_experimental_option("detach", True)
                        self.driver = webdriver.Chrome(options=options,
                                                       executable_path="../Browser_Drivers/Windows/geckodriver.exe")
        with allure.step("STEP-3: Launch the Mobile Site."):
            self.driver.maximize_window()
            self.driver.get(general_data.mobile_URL)

        time.sleep(5)

    @staticmethod
    def close_browser(self):
        with allure.step("STEP-8: Close the Browser."):
            self.driver.close()

    def test_Rest_Password(self, startup):

        wait = 5

        with allure.step("STEP-4: Call get_authentication_test_data() method."):
            test_Login_data = TestData()
            login_data = test_Login_data.get_authentication_test_data()

        time.sleep(wait)

        with allure.step("STEP-5: Click on Rest Password Link."):
            mobile_signIn_screen = Mobile_SignIn(self.driver)
            isElementExist = mobile_signIn_screen.click_reset_password_link()
            assert isElementExist, "Unable to Locate Element. Issue in --click_reset_password_link()---method."

        time.sleep(wait)

        with allure.step("STEP-6: Pass User Name and Captcha."):
            mobile_retrieve_user_name = Mobile_ForgotPassword(self.driver)
            isElementExist = mobile_retrieve_user_name.enter_rest_password_user_name_captcha(login_data.resetPassword_UserName, "valid captcha")
            assert isElementExist, "Unable to Locate Element. Issue in --enter_rest_password_user_name_captcha()---method."

            mobile_common = Mobile_Common(self.driver)
            isElementExist = mobile_common.click_submit_btn()
            assert isElementExist, "Unable to Locate Element. Issue in --click_submit_btn()---method."

        time.sleep(wait)

        with allure.step("STEP-7: Pass New Password and Confirm New Password."):
            reset_password = Mobile_ForgotResetPassword(self.driver)
            isElementExist = reset_password.enter_new_confirm_password(login_data.resetPassword_New_Confirm_Password)
            assert isElementExist, "Unable to Locate Element. Issue in --enter_new_confirm_password()---method."

            mobile_common = Mobile_Common(self.driver)
            isElementExist = mobile_common.click_submit_btn()
            assert isElementExist, "Unable to Locate Element. Issue in --click_submit_btn()---method."

        time.sleep(wait)
