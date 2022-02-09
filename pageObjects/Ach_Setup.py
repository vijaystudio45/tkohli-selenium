from time import sleep

class AchSetupClass:
    profile_href_link = "Manage Profile"
    ach_href_link = "ACH Setup"
    textbox_middlename = "m_name"
    textbox_ach_suffix = "suffix"
    textbox_ach_AddressLine1 = "address_line_1"
    textbox_ach_AddressLine2 = "address_line_2"
    textbox_ach_city = "city"
    textbox_ach_postal_code = "zip"
    textbox_ach_security_number = "ssn"
    ach_submit_btn_class = "ach_submit_button"
    click_select_dropdown_ach_type = "type"
    textbox_ach_account_number = "accountNumber"
    textbox_ach_routing_number = "routingNumber"
    textbox_ach_confirm_routing_number = "routingNumberconf"
    ach_update_submit_btn_class = "ach_with_bank_link_button"


    def __init__(self, driver):
        self.driver = driver

    def clickProfile(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.profile_href_link).click()

    def clickAchbtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.ach_href_link).click()

    def setAchMiddleName(self, ach_middle_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_middlename).clear()
        self.driver.find_element_by_name(self.textbox_middlename).send_keys(ach_middle_name)

    def setAchSuffix(self, ach_suffix):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_suffix).clear()
        self.driver.find_element_by_name(self.textbox_ach_suffix).send_keys(ach_suffix)

    def setAchPhone_number(self, ach_phone_number):
        sleep(1)
        self.driver.find_element_by_name("phone_number").clear()
        self.driver.find_element_by_name("phone_number").send_keys(ach_phone_number)

    def setAchAddressLine1(self, ach_AddressLine1):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_AddressLine1).clear()
        self.driver.find_element_by_name(self.textbox_ach_AddressLine1).send_keys(ach_AddressLine1)


    def setAchAddressLine2(self, ach_AddressLine2):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_AddressLine2).clear()
        self.driver.find_element_by_name(self.textbox_ach_AddressLine2).send_keys(ach_AddressLine2)


    def setAchCity(self, ach_city):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_city).clear()
        self.driver.find_element_by_name(self.textbox_ach_city).send_keys(ach_city)

    def setAchPostalCode(self, ach_postal_code):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_postal_code).clear()
        self.driver.find_element_by_name(self.textbox_ach_postal_code).send_keys(ach_postal_code)

    def setAchSecurityNumber(self, ach_security_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_security_number).clear()
        self.driver.find_element_by_name(self.textbox_ach_security_number).send_keys(ach_security_number)

    def clicksubmitAchbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.ach_submit_btn_class).click()

    def clickSelectACHtype(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_ach_type).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='type']/option[2]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_ach_type).click()


    def setAchaccountNumber(self, ach_account_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_account_number).clear()
        self.driver.find_element_by_name(self.textbox_ach_account_number).send_keys(ach_account_number)


    def setAchRoutingNumber(self, ach_routing_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_routing_number).clear()
        self.driver.find_element_by_name(self.textbox_ach_routing_number).send_keys(ach_routing_number)

    def setAchConfirmRoutingNumber(self, ach_confirm_routing_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_ach_confirm_routing_number).clear()
        self.driver.find_element_by_name(self.textbox_ach_confirm_routing_number).send_keys(ach_confirm_routing_number)

    def clickupdatesubmitAchbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.ach_update_submit_btn_class).click()

    def clickdatepickertest(self):
        sleep(2)
        self.driver.find_element_by_id("dob").clear()
        self.driver.find_element_by_css_selector("#datepickers-container > div > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(13)").click()