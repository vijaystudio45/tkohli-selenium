from time import sleep

class LongcodesClass:
    longcode_href_link = "Longcodes"
    Org_longcode_link_text = "Automation-organization-updated"
    create_longcodes_href_link = "Create longcodes"
    textbox_longcode_number = "number"
    textbox_longcode_notes = "notes"
    click_select_business_unit = "business_unit_id"
    textbox_longcode_provider = "provider"
    active_checkbox_name = "active_long"
    longcodes_create_btn_class = "create_longcodes_btn"
    edit_longcode_link_class = "action_btns"
    longcodes_update_btn_class = "update_longcodes_btn"
    remove_longcodes_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickLongcode(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.longcode_href_link).click()

    def clickOrgLongcodeBtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.Org_longcode_link_text).click()

    def clickCreateLongcode(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_longcodes_href_link).click()

    def setlongcodeNumber(self, longcode_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_longcode_number).clear()
        self.driver.find_element_by_name(self.textbox_longcode_number).send_keys(longcode_number)

    def setlongcodeNotes(self, longcode_notes):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_longcode_notes).clear()
        self.driver.find_element_by_name(self.textbox_longcode_notes).send_keys(longcode_notes)

    def clickSelectbusinessUnit(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_business_unit).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='custom_inputs']/option[2]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_business_unit).click()

    def setlongcodeProvider(self, longcode_provider):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_longcode_provider).clear()
        self.driver.find_element_by_name(self.textbox_longcode_provider).send_keys(longcode_provider)

    def clickActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_checkbox_name).click()

    def clickcreatelongcodebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.longcodes_create_btn_class).click()


    def clickLongcodesEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_longcode_link_class).click()

    def clickupdatelongcodebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.longcodes_update_btn_class).click()

    def clickRemovelongcodeLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_longcodes_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div[3]/div[2]/button').click()