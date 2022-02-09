from time import sleep

class orgadmin_vcardclass:
    vcard_href_link = "Manage Vcard"
    create_vcard_href_link = "Create Vcard"
    textbox_vcard_name = "name"
    textbox_display_vcard_name = "display_name"
    textbox_vcard_website= "website"
    textbox_vcard_telephone = "telephone"
    textbox_vcard_first_name = "f_name"
    textbox_vcard_last_name = "l_name"
    textbox_vcard_email = "email"
    textbox_vcard_address = "address"
    click_select_dropdown_business_unit = "business_unit_id"
    create_vcard_btn_class = "create_vcard_btn"
    edit_vcard_btn_class = "glyphiconedit"
    update_vcard_btn_class = "update_vcard_btn"
    remove_vcard_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickvcard(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.vcard_href_link).click()

    def clickcreatevcard(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_vcard_href_link).click()

    def set_org_admin_vcard_name(self, vcard_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_name).clear()
        self.driver.find_element_by_name(self.textbox_vcard_name).send_keys(vcard_name)

    def set_org_admin_display_vcard_name(self, display_vcard_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_display_vcard_name).clear()
        self.driver.find_element_by_name(self.textbox_display_vcard_name).send_keys(display_vcard_name)

    def set_org_admin_vcard_website(self, vcard_website):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_website).clear()
        self.driver.find_element_by_name(self.textbox_vcard_website).send_keys(vcard_website)

    def set_org_admin_vcard_telephone(self, vcard_telephone):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_telephone).clear()
        self.driver.find_element_by_name(self.textbox_vcard_telephone).send_keys(vcard_telephone)


    def set_org_admin_vcard_first_name(self, vcard_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_first_name).clear()
        self.driver.find_element_by_name(self.textbox_vcard_first_name).send_keys(vcard_first_name)

    def set_org_admin_vcard_last_name(self, vcard_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_last_name).clear()
        self.driver.find_element_by_name(self.textbox_vcard_last_name).send_keys(vcard_last_name)

    def set_org_admin_vcard_email(self, vcard_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_email).clear()
        self.driver.find_element_by_name(self.textbox_vcard_email).send_keys(vcard_email)

    def set_org_admin_vcard_Address(self, vcard_address):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_address).clear()
        self.driver.find_element_by_name(self.textbox_vcard_address).send_keys(vcard_address)

    def clickSelectbusinessunit(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_business_unit).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='vcard_business_unit_id']/option[2]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_business_unit).click()

    def clickcreatevcardbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.create_vcard_btn_class).click()

    def clickeditvcardbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_vcard_btn_class).click()

    def clickupdatevcardbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.update_vcard_btn_class).click()

    def clickRemovevcard(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_vcard_link).click()


    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/button').click()

