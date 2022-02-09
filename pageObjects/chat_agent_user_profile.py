from time import sleep

class chatagentUserprofileClass:
    chat_agent_profile_href_link = "Manage Profile"
    textbox_chat_agent_first_name = "f_name"
    textbox_chat_agent_last_name = "l_name"
    textbox_chat_agent_phone_number = "phone_number"
    textbox_chatagent_group_assignment = "group_assignment"
    textbox_chatagent_social_security_number = "social"
    textbox_chat_agent_profile_current_password = "current_password"
    textbox_chatagent_new_password = "new_pass"
    textbox_chatagent_profile_confirm_password = "confirm_pass"
    checkbox_chatagent_profile_profile_active = "check"



    def __init__(self, driver):
        self.driver = driver

    def click_chat_agent_profile_page_link(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.chat_agent_profile_href_link).click()

    def set_chatagent_First_Name(self, chat_agent_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chat_agent_first_name).clear()
        self.driver.find_element_by_name(self.textbox_chat_agent_first_name).send_keys(chat_agent_first_name)

    def set_chatagent_Last_Name(self, chat_agent_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chat_agent_last_name).clear()
        self.driver.find_element_by_name(self.textbox_chat_agent_last_name).send_keys(chat_agent_last_name)

    def set_chatagent_Phone_number(self, chat_agent_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chat_agent_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_chat_agent_phone_number).send_keys(chat_agent_phone_number)

    def click_chat_agent_profile_date(self):
        sleep(2)
        self.driver.find_element_by_id("date_content").click()
        self.driver.find_element_by_id("date_content").clear()
        self.driver.find_element_by_css_selector("#datepickers-container > div > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(7)").click()

    def set_chat_agent_group_assignment(self, chatagent_group_assignment):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chatagent_group_assignment).clear()
        self.driver.find_element_by_name(self.textbox_chatagent_group_assignment).send_keys(chatagent_group_assignment)

    def chatagent_profile_Selectstate(self):
        sleep(2)
        self.driver.find_element_by_name("state_code").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='state_code']/option[8]").click()
        sleep(1)
        self.driver.find_element_by_name("state_code").click()

    def setchatagent_current_password(self, chat_agent_profile_current_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chat_agent_profile_current_password).clear()
        self.driver.find_element_by_name(self.textbox_chat_agent_profile_current_password).send_keys(chat_agent_profile_current_password)


    def setchatagent_new_password(self, chatagent_profile_new_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chatagent_new_password).clear()
        self.driver.find_element_by_name(self.textbox_chatagent_new_password).send_keys(chatagent_profile_new_password)


    def setchatagent_confirm_password(self, chatagent_profile_confirm_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chatagent_profile_confirm_password).clear()
        self.driver.find_element_by_name(self.textbox_chatagent_profile_confirm_password).send_keys(chatagent_profile_confirm_password)


    def clickprofileActiveCheckbox(self):
        self.driver.find_element_by_name(self.checkbox_chatagent_profile_profile_active).click()

    def clickchatagentupdatebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name("updateUserProfileBtn").click()