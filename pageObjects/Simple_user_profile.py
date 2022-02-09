from time import sleep

class SimpleUserprofileClass:
    simple_user_profile_href_link = "Manage Profile"
    textbox_simple_user_first_name = "f_name"
    textbox_simple_user_last_name = "l_name"
    textbox_simple_user_phone_number = "phone_number"
    textbox_simple_user_group_assignment = "group_assignment"
    textbox_simple_user_profile_social_security_number = "social"
    textbox_simple_user_profile_current_password = "current_password"
    textbox_simple_user_profile_new_password = "new_pass"
    textbox_simple_user_profile_confirm_password = "confirm_pass"
    checkbox_simple_user_profile_active = "check"

    def __init__(self, driver):
        self.driver = driver

    def click_simple_user_profile_page_link(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.simple_user_profile_href_link).click()

    def setSimpleUser_First_Name(self, simple_user_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_first_name).clear()
        self.driver.find_element_by_name(self.textbox_simple_user_first_name).send_keys(simple_user_first_name)

    def setSimpleUser_Last_Name(self, simple_user_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_last_name).clear()
        self.driver.find_element_by_name(self.textbox_simple_user_last_name).send_keys(simple_user_last_name)

    def setSimpleUser_Phone_number(self, simple_user_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_simple_user_phone_number).send_keys(simple_user_phone_number)

    def clickSimple_user_profile_date(self):
        sleep(2)
        self.driver.find_element_by_id("date_content").click()
        self.driver.find_element_by_id("date_content").clear()
        self.driver.find_element_by_css_selector("#datepickers-container > div > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(7)").click()

    def setSimpleUser_group_assignment(self, simple_user_group_assignment):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_group_assignment).clear()
        self.driver.find_element_by_name(self.textbox_simple_user_group_assignment).send_keys(simple_user_group_assignment)

    def clickSimple_user_profile_Selectstate(self):
        sleep(2)
        self.driver.find_element_by_name("state_code").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='state_code']/option[8]").click()
        sleep(1)
        self.driver.find_element_by_name("state_code").click()

    def setSimpleUser_social_security_number(self, simple_user_profile_social_security_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_profile_social_security_number).clear()
        self.driver.find_element_by_name(self.textbox_simple_user_profile_social_security_number).send_keys(simple_user_profile_social_security_number)

    def setSimpleUser_current_password(self, simple_user_profile_current_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_profile_current_password).clear()
        self.driver.find_element_by_name(self.textbox_simple_user_profile_current_password).send_keys(simple_user_profile_current_password)


    def setSimpleUser_new_password(self, simple_user_profile_new_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_profile_new_password).clear()
        self.driver.find_element_by_name(self.textbox_simple_user_profile_new_password).send_keys(simple_user_profile_new_password)


    def setSimpleUser_confirm_password(self, simple_user_profile_confirm_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_profile_confirm_password).clear()
        self.driver.find_element_by_name(self.textbox_simple_user_profile_confirm_password).send_keys(simple_user_profile_confirm_password)


    def clickprofileActiveCheckbox(self):
        self.driver.find_element_by_name(self.checkbox_simple_user_profile_active).click()

    def clicksimpleuserupdatebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name("updateUserProfileBtn").click()