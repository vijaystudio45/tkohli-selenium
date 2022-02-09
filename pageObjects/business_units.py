from time import sleep

class BusinessUnitClass:
    business_units_href_link = "Business Units"
    create_business_units_href_link = "Create Business Units"
    textbox_unit_name = "unit_name"
    textbox_unit_website = "unit_website"
    textbox_unit_phone_number = "unit_phone_number"
    dropdown_organization_name ="org_id"
    click_qc_btn_link = "add_representative_multiple"
    textbox_unit_qc_phoneno = "phone_number[1]"
    active_checkbox_name = "require_status_qc[1]"
    textbox_unit_f_name = "unit_f_name"
    textbox_unit_l_name = "unit_l_name"
    textbox_unit_email = "unit_email"
    textbox_unit_contact_phoneno = "unit_contact_phone_number"
    active_unit_checkbox_name = "active_business_unit"
    active_phonelookup_checkbox_name = "phone_lockup_flag"
    unit_create_btn_class = "create_bus_unit_btn"
    unit_edit_btn_class = "action_btns"
    unit_update_btn_class = "update_unit_btn"
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

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated ']").click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()

    def click_qc_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_qc_btn_link).click()

    def setUnitQcPhoneno(self, unit_qc_Phoneno):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_unit_qc_phoneno).clear()
        self.driver.find_element_by_name(self.textbox_unit_qc_phoneno).send_keys(unit_qc_Phoneno)

    def clickActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_checkbox_name).click()

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

    def clickphonelookupCheckbox(self):
        self.driver.find_element_by_name(self.active_phonelookup_checkbox_name).click()

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
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()