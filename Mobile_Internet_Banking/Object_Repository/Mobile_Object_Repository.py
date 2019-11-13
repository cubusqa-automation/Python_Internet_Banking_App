import time

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException


class Mobile_SignIn:
    def __init__(self, driver):
        self.driver = driver

        self.username_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Textbox_UserName']"
        self.password_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Text_Password']"
        self.submit_btn_xpath = "//input[@id='ctl00_CPHSectionContent_Button_DummySubmit']"

        self.retrieve_user_name_link_xpath = "//a[@id='ctl00_CPHSectionContent_Link_ForgotUserName']"
        self.reset_password_link_xpath = "//a[@id='ctl00_CPHSectionContent_Link_ForgotPassword']"

    def combined_user_name_password_enabled(self, username, password):

        try:
            self.driver.find_element_by_xpath(self.username_txt_box_xpath).send_keys(username)
            self.driver.find_element_by_xpath(self.password_txt_box_xpath).send_keys(password)
            time.sleep(3)
            self.driver.find_element_by_xpath(self.submit_btn_xpath).click()
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="combined_user_name_password_enabled", attachment_type=AttachmentType.PNG)
            return False

    def click_retrieve_user_name_link(self):
        try:
            self.driver.find_element_by_xpath(self.retrieve_user_name_link_xpath).click()
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="click_retrieve_user_name_link", attachment_type=AttachmentType.PNG)
            return False

    def click_reset_password_link(self):
        try:
            self.driver.find_element_by_xpath(self.reset_password_link_xpath).click()
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="click_reset_password_link", attachment_type=AttachmentType.PNG)
            return False


class Mobile_ForgotUsername:
    def __init__(self, driver):
        self.driver = driver

        self.member_number_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Textbox_MemberNo']"
        self.captcha_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Textbox_OneTimePassCode']"

    def enter_retrieve_user_name_captcha(self, retrieve_user_name_member_number, captcha):
        try:
            self.driver.find_element_by_xpath(self.member_number_txt_box_xpath).send_keys(
                retrieve_user_name_member_number)
            self.driver.find_element_by_xpath(self.captcha_txt_box_xpath).send_keys(captcha)
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="enter_retrieve_user_name_captcha", attachment_type=AttachmentType.PNG)
            return False


class Mobile_RetrieveUsernamePasswordVerify:
    def __init__(self, driver):
        self.driver = driver

        self.retrieve_user_name_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Textbox_Password']"

    def enter_retrieve_user_name_password(self, retrieve_user_name_password):

        try:
            self.driver.find_element_by_xpath(self.retrieve_user_name_txt_box_xpath).send_keys(
                retrieve_user_name_password)
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="enter_retrieve_user_name_password", attachment_type=AttachmentType.PNG)
            return False


class Mobile_ForgotPassword:
    def __init__(self, driver):
        self.driver = driver

        self.user_name_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Textbox_Username']"
        self.captcha_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Textbox_OneTimePassCode']"

    def enter_rest_password_user_name_captcha(self, reset_password_user_name, captcha):
        try:
            self.driver.find_element_by_xpath(self.user_name_txt_box_xpath).send_keys(reset_password_user_name)
            self.driver.find_element_by_xpath(self.captcha_txt_box_xpath).send_keys(captcha)
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="enter_rest_password_user_name_captcha", attachment_type=AttachmentType.PNG)
            return False


class Mobile_ForgotResetPassword:

    def __init__(self, driver):
        self.driver = driver

        self.new_password = "//input[@id='ctl00_CPHSectionContent_Textbox_NewPassword']"
        self.confirm_new_password = "//input[@id='ctl00_CPHSectionContent_Textbox_RetPassword']"

    def enter_new_confirm_password(self, reset_password_new_confirm_password):
        try:
            self.driver.find_element_by_xpath(self.new_password).send_keys(reset_password_new_confirm_password)
            self.driver.find_element_by_xpath(self.confirm_new_password).send_keys(reset_password_new_confirm_password)
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="enter_new_confirm_password", attachment_type=AttachmentType.PNG)
            return False


class Mobile_Common:
    def __init__(self, driver):
        self.driver = driver

        self.submit_btn_xpath = "//input[@id='ctl00_CPHSectionContent_Button_Submit']"

    def click_submit_btn(self):
        try:
            self.driver.find_element_by_xpath(self.submit_btn_xpath).click()
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="click_submit_btn", attachment_type=AttachmentType.PNG)
            return False


class Mobile_Dashboard:
    def __init__(self, driver):
        self.driver = driver

        self.logout_btn_xpath = "/html[1]/body[1]/form[1]/div[3]/main[1]/div[1]/header[1]/div[1]/a[3]"

    def click_logout_btn(self):
        try:
            self.driver.find_element_by_xpath(self.logout_btn_xpath).click()
            return True
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="click_logout_btn", attachment_type=AttachmentType.PNG)
            return False
