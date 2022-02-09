from time import sleep

class SenderUserachSetupClass:
    sender_profile_href_link = "Manage Profile"
    sender_user_ach_href_link = "ACH Setup"
    textbox_sender_ach_first_name = "f_name"
    textbox_sender_ach_last_name = "l_name"
    textbox_sender_ach_middelware = "m_name"
    textbox_sender_ach_suffix = "suffix"
    textbox_sender_ach_email = "email"
    textbox_sender_ach_phone_number = "phone_number"
    textbox_sender_ach_address_line1 = "address_line_1"
    textbox_sender_ach_address_line2 = "address_line_2"
    textbox_sender_ach_city = "city"
    textbox_sender_ach_postal_code = "zip"
    click_select_dropdown_sender_ach_state = "state_code"
    textbox_sender_ach_country = "country"
    textbox_sender_ach_security_number = "ssn"
    sender_ach_submit_btn_class = "ach_submit_button"
    click_select_dropdown_sender_ach_type = "type"
    textbox_sender_ach_account_number = "accountNumber"
    textbox_sender_ach_Routing_number = "routingNumber"
    textbox_sender_ach_confirm_Routing_number = "routingNumberconf"
    sender_ach_update_btn_class = "ach_with_bank_link_button"

    def __init__(self, driver):
        self.driver = driver

    def clicksenderProfile(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sender_profile_href_link).click()

    def clicksenderAchbtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sender_user_ach_href_link).click()

    def setsenderAchFirstName(self, sender_ach_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_first_name).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_first_name).send_keys(sender_ach_first_name)

    def setsenderAchMiddleWare(self, sender_ach_middelware):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_middelware).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_middelware).send_keys(sender_ach_middelware)

    def setsenderAchLastName(self, sender_ach_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_last_name).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_last_name).send_keys(sender_ach_last_name)

    def setsenderAchsuffix(self, sender_ach_suffix):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_suffix).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_suffix).send_keys(sender_ach_suffix)

    def setsenderAchEmail(self, sender_ach_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_email).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_email).send_keys(sender_ach_email)

    def setsenderAchPhonenumber(self, sender_ach_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_phone_number).send_keys(sender_ach_phone_number)

    def setsenderAchAddressLine1(self, sender_ach_address_line1):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_address_line1).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_address_line1).send_keys(sender_ach_address_line1)

    def setsenderAchAddressLine2(self, sender_ach_address_line2):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_address_line2).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_address_line2).send_keys(sender_ach_address_line2)

    def setsenderAchcity(self, sender_ach_city):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_city).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_city).send_keys(sender_ach_city)


    def clickSelectsenderAchState(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_sender_ach_state).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='state_code']/option[7]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_select_dropdown_sender_ach_state).click()

    def setsenderAchpostalcode(self, sender_ach_postal_code):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_postal_code).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_postal_code).send_keys(sender_ach_postal_code)

    def setsenderAchcountry(self, sender_ach_country):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_country).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_country).send_keys(sender_ach_country)

    def setsenderAchsocialsecurityNumber(self, sender_ach_social_security_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_security_number).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_security_number).send_keys(sender_ach_social_security_number)

    def click_sender_ach_submit_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.sender_ach_submit_btn_class).click()

    def clickSelectsenderAchType(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_sender_ach_type).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='type']/option[2]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_select_dropdown_sender_ach_type).click()

    def setsenderAchAccountNumber(self, sender_ach_account_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_account_number).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_account_number).send_keys(sender_ach_account_number)

    def setsenderAchRoutingNumber(self, sender_ach_Routing_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_Routing_number).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_Routing_number).send_keys(sender_ach_Routing_number)

    def setsenderAchConfirmRoutingNumber(self, sender_ach_confirm_Routing_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_ach_confirm_Routing_number).clear()
        self.driver.find_element_by_name(self.textbox_sender_ach_confirm_Routing_number).send_keys(sender_ach_confirm_Routing_number)

    def click_sender_update_ach_submit_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.sender_ach_update_btn_class).click()