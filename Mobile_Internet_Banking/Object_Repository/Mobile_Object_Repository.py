class Mobile_SignIn:
    def __init__(self, driver):
        self.driver = driver

        self.username_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Textbox_UserName']"
        self.password_txt_box_xpath = "//input[@id='ctl00_CPHSectionContent_Text_Password']"

    def combined_user_name_password_enabled(self, username, password):
        self.driver.find_element_by_xpath(self.username_txt_box_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.password_txt_box_xpath).send_keys(password)


class Mobile_Common:
    def __init__(self, driver):
        self.driver = driver

        self.submit_btn_xpath = "//input[@id='ctl00_CPHSectionContent_Button_DummySubmit']"

    def click_submit_btn(self):
        self.driver.find_element_by_xpath(self.submit_btn_xpath).click()

class Mobile_Dashboard:
    def __init__(self, driver):
        self.driver = driver

        self.logout_btn_xpath = "/html[1]/body[1]/form[1]/div[3]/main[1]/div[1]/header[1]/div[1]/a[3]"

    def click_logout_btn(self):
        self.driver.find_element_by_xpath(self.logout_btn_xpath).click()
