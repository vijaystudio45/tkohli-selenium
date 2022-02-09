from time import sleep

class VcardClass:
    vcard_href_link = "Manage Vcard"
    create_vcard_href_link = "Create Vcard"
    textbox_vcard_name = "name"
    textbox_display_vcard_name = "display_name"
    textbox_vcard_website = "website"
    textbox_vcard_telephone = "telephone"
    textbox_vcard_f_name = "f_name"
    textbox_vcard_l_name = "l_name"
    textbox_vcard_email = "email"
    textbox_vcard_address = "address"
    click_select_org_name = "org_id"
    vcard_create_btn_class = "create_vcard_btn"
    edit_vcard_link_class = "action_btns"
    Update_vcard_link_class ="update_vcard_btn"
    remove_vcard_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickVcard(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.vcard_href_link).click()

    def clickcreateVcard(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_vcard_href_link).click()

    def setVcardName(self, vcard_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_name).clear()
        self.driver.find_element_by_name(self.textbox_vcard_name).send_keys(vcard_name)

    def displayVcardName(self, display_vcard_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_display_vcard_name).clear()
        self.driver.find_element_by_name(self.textbox_display_vcard_name).send_keys(display_vcard_name)

    def displayVcardWebsite(self, vcard_website):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_website).clear()
        self.driver.find_element_by_name(self.textbox_vcard_website).send_keys(vcard_website)

    def displayVcardTelephone(self, vcard_telephone):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_telephone).clear()
        self.driver.find_element_by_name(self.textbox_vcard_telephone).send_keys(vcard_telephone)

    def displayVcard_f_name(self, vcard_f_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_f_name).clear()
        self.driver.find_element_by_name(self.textbox_vcard_f_name).send_keys(vcard_f_name)

    def displayVcard_l_name(self, vcard_l_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_l_name).clear()
        self.driver.find_element_by_name(self.textbox_vcard_l_name).send_keys(vcard_l_name)

    def displayVcard_email(self, vcard_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_email).clear()
        self.driver.find_element_by_name(self.textbox_vcard_email).send_keys(vcard_email)

    def displayVcard_Address(self, vcard_address):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_vcard_address).clear()
        self.driver.find_element_by_name(self.textbox_vcard_address).send_keys(vcard_address)

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_org_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_org_name).click()

    def clickcreatevcardbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.vcard_create_btn_class).click()

    def clickVcardEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_vcard_link_class).click()

    def clickVcardUpdateBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.Update_vcard_link_class).click()

    def clickRemoveVcardLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_vcard_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()