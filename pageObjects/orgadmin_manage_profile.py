from time import sleep


class orgadminManageProfileClass:
    manage_profile_href_link = "Manage Profile"
    textbox_first_name = "f_name"
    textbox_last_name = "l_name"
    textbox_phone_number = "phone_number"
    click_select_dropdown_dob = "date_content"
    textbox_group_assignment = "group_assignment"
    click_select_dropdown_profile_state = "state_code"
    textbox_profile_current_password = "current_password"
    textbox_profile_new_password = "new_pass"
    textbox_profile_confirm_password = "confirm_pass"
    profile_update_btn_class = "updateUserProfileBtn"

    def __init__(self, driver):
        self.driver = driver

    def click_manage_profile_btn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.manage_profile_href_link).click()

    def set_manage_profile_name(self, Profile_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_first_name).clear()
        self.driver.find_element_by_name(self.textbox_first_name).send_keys(Profile_name)

    def set_manage_profile_last_name(self, Profile_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_last_name).clear()
        self.driver.find_element_by_name(self.textbox_last_name).send_keys(Profile_last_name)

    def set_manage_profile_phone_number(self, Profile_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_phone_number).send_keys(Profile_phone_number)

    def click_manage_profile_dob(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_dob).click()
        self.driver.find_element_by_id(self.click_select_dropdown_dob).clear()
        self.driver.find_element_by_css_selector("#datepickers-container > div > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(4)").click()

    def set_manage_group_assignment(self, group_assignment):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_group_assignment).clear()
        self.driver.find_element_by_name(self.textbox_group_assignment).send_keys(group_assignment)

    def manage_profile_click_state(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_profile_state).click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="state_code"]/option[35]').click()
        sleep(1)

    def set_manage_profile_current_password(self, current_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_profile_current_password).clear()
        self.driver.find_element_by_name(self.textbox_profile_current_password).send_keys(current_password)

    def set_manage_profile_new_password(self, new_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_profile_new_password).clear()
        self.driver.find_element_by_name(self.textbox_profile_new_password).send_keys(new_password)

    def set_manage_profile_confirm_password(self,confirm_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_profile_confirm_password).clear()
        self.driver.find_element_by_name(self.textbox_profile_confirm_password).send_keys(confirm_password)

    def click_update_account_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.profile_update_btn_class).click()