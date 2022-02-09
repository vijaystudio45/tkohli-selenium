from time import sleep

class orgadmin_OrganizationsClass:
    organizations_href_link = "Manage Organizations"
    textbox_organization_name = "org_name"
    textbox_organization_website = "org_website"
    textbox_organization_phone_numer = "org_phone_number"
    click_select_dropdown_timezone = "default_timezone"
    textbox_organization_first_name = "org_f_name"
    textbox_organization_last_name = "org_l_name"
    textbox_organization_email = "org_email"
    textbox_org_contact_phone_number = "org_contact_phone_number"
    active_checkbox_name = "active_org"
    org_update_btn_class = "update_org_btns"
    org_edit_btn_class = "glyphiconedit"

    def __init__(self, driver):
        self.driver = driver

    def clickorganization(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.organizations_href_link).click()

    def setorgadmin_organizationName(self, org_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_organization_name).clear()
        self.driver.find_element_by_name(self.textbox_organization_name).send_keys(org_name)

    def setorgadmin_organizationWebsite(self, org_website):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_organization_website).clear()
        self.driver.find_element_by_name(self.textbox_organization_website).send_keys(org_website)

    def setorgadmin_organizationPhone_Number(self, org_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_organization_phone_numer).clear()
        self.driver.find_element_by_name(self.textbox_organization_phone_numer).send_keys(org_phone_number)

    def clickSelecttimezone(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_timezone).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='timezone']/option[3]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_timezone).click()


    def setorgadmin_organization_first_name(self, org_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_organization_first_name).clear()
        self.driver.find_element_by_name(self.textbox_organization_first_name).send_keys(org_first_name)

    def setorgadmin_organization_last_name(self, org_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_organization_last_name).clear()
        self.driver.find_element_by_name(self.textbox_organization_last_name).send_keys(org_last_name)

    def setorgadmin_organization_email(self, org_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_organization_email).clear()
        self.driver.find_element_by_name(self.textbox_organization_email).send_keys(org_email)

    def setorgadmin_organization_contact_phone_number(self, org_contact_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_org_contact_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_org_contact_phone_number).send_keys(org_contact_phone_number)

    def clickActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_checkbox_name).click()

    def clickeditorgbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.org_edit_btn_class).click()

    def clickupdateorgbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.org_update_btn_class).click()