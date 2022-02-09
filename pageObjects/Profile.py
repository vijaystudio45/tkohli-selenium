from time import sleep

class ProfileClass:
    profile_href_link = "Manage Profile"
    textbox_phone_number= "phone_number"
    click_select_dropdown_profile_state = "state_code"
    textbox_current_password = "current_password"
    textbox_new_password = "new_pass"
    textbox_confirm_password = "confirm_pass"
    profile_update_btn_class = "updateAdminProfileBtn"

    def __init__(self, driver):
        self.driver = driver

    def clickProfile(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.profile_href_link).click()

    def setProfilePhoneNumber(self, Profile_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_phone_number).send_keys(Profile_phone_number)

    def clickSelectProfileState(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_profile_state).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='state_code']/option[9]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_profile_state).click()

    def setProfilecurrentPassword(self, Profile_current_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_current_password).clear()
        self.driver.find_element_by_name(self.textbox_current_password).send_keys(Profile_current_password)

    def setProfileNewPassword(self, Profile_new_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_new_password).clear()
        self.driver.find_element_by_name(self.textbox_new_password).send_keys(Profile_new_password)


    def setProfilconfirmPassword(self, Profile_confirm_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_confirm_password).clear()
        self.driver.find_element_by_name(self.textbox_confirm_password).send_keys(Profile_confirm_password)

    def clickdatepickertest(self):
        sleep(2)
        self.driver.find_element_by_id("date_content").clear()
        self.driver.find_element_by_css_selector("#datepickers-container > div > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(4)").click()

    def clickupdateprofilebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.profile_update_btn_class).click()