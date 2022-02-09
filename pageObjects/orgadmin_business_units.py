from time import sleep

class orgadminBusinessUnitClass:
    business_units_href_link = "Business Units"
    create_business_units_href_link = "Create Business Units"
    textbox_unit_name = "unit_name"
    textbox_unit_website = "unit_website"
    textbox_unit_phone_number = "unit_phone_number"
    textbox_unit_f_name = "unit_f_name"
    textbox_unit_l_name = "unit_l_name"
    textbox_unit_email = "unit_email"
    textbox_unit_contact_phoneno = "unit_contact_phone_number"
    active_unit_checkbox_name = "active_business_unit"
    unit_create_btn_class = "create_unit_btns"
    unit_edit_btn_class = "glyphiconedit"
    unit_update_btn_class = "update_unit_btns"
    remove_unit_link = "Remove"
    def __init__(self, driver):
        self.driver = driver


    def clickBuisnessUnit(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.business_units_href_link).click()

    def clickcreateBuisnessUnit(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_business_units_href_link).click()

    def setUnitName(self, unit_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_unit_name).clear()
        self.driver.find_element_by_name(self.textbox_unit_name).send_keys(unit_name)

    def setUnitWebsite(self, unit_website):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_unit_website).clear()
        self.driver.find_element_by_name(self.textbox_unit_website).send_keys(unit_website)

    def setUnitPhoneno(self, unit_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_unit_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_unit_phone_number).send_keys(unit_phone_number)

    def setUnitFirstName(self, unit_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_unit_f_name).clear()
        self.driver.find_element_by_name(self.textbox_unit_f_name).send_keys(unit_first_name)

    def setUnitLastName(self, unit_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_unit_l_name).clear()
        self.driver.find_element_by_name(self.textbox_unit_l_name).send_keys(unit_last_name)

    def setUnitEmail(self, unit_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_unit_email).clear()
        self.driver.find_element_by_name(self.textbox_unit_email).send_keys(unit_email)

    def setUnitContactPhoneNo(self, unit_phone_no):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_unit_contact_phoneno).clear()
        self.driver.find_element_by_name(self.textbox_unit_contact_phoneno).send_keys(unit_phone_no)

    def clickunitActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_unit_checkbox_name).click()

    def clickcreatbusinessUnitbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.unit_create_btn_class).click()

    def clickunitEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.unit_edit_btn_class).click()

    def clickunitUpdateBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.unit_update_btn_class).click()

    def clickRemoveunitLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_unit_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/button').click()