from time import sleep
import os
class PhoneLookupRuleClass:
    phone_loopup_href_link = "Phone Lookup Rules"
    create_phone_lookup_rule_href_link = "Create Phone Lookup Rules"
    textbox_title_name = "title"
    phone_lookup_message_name = "message"
    phone_lookup_error_triger_name = "error_trigger"
    dropdown_organization_name = "org_id"
    active_checkbox_name = "active"
    checkbox_message_name = "message_active"
    media_active_checkbox_name = "media_active"
    error_active_checkbox_name = "error_active"
    phn_lookup_create_btn_class = "create_phone_lookup_btn"

    phone_lookup_edit_href_link = "Edit"
    dropdown_organization_edit_name = "org_id"
    phn_lookup_update_btn_class = "update_phone_lookup_btn"

    delete_phn_lookup_link_text = "Remove"
    confirn_delete_phn_lookup_link_text = "Yes, delete it!"
    confirn_delete_phn_lookup_class="swal-button--confirm"
    run_phnlookup_class = "action_btns"
    


    def __init__(self, driver):
        self.driver = driver

    def clickPhoneLookup(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.phone_loopup_href_link).click()

    def clickCreatePhoneLookup(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_phone_lookup_rule_href_link).click()

    def setTitleName(self, title):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_title_name).clear()
        self.driver.find_element_by_name(self.textbox_title_name).send_keys(title)

    def setPhoneLookUpMessage(self, message):
        sleep(1)
        self.driver.find_element_by_name(self.phone_lookup_message_name).clear()
        self.driver.find_element_by_name(self.phone_lookup_message_name).send_keys(message)

    def setPhoneLookUpErrorTriger(self, error_triger):
        sleep(1)
        self.driver.find_element_by_name(self.phone_lookup_error_triger_name).clear()
        self.driver.find_element_by_name(self.phone_lookup_error_triger_name).send_keys(error_triger)

    def clickSelectOrg(self):
        self.driver.find_element_by_name(self.dropdown_organization_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()
        

    def clickActiveCheckbox(self):
        sleep(1)
        self.driver.find_element_by_name(self.active_checkbox_name).click()

    def clickMessageCheckbox(self):
        sleep(1)
        self.driver.find_element_by_name(self.checkbox_message_name).click()

    def clickMediaActiveCheckbox(self):
        sleep(1)
        self.driver.find_element_by_name(self.media_active_checkbox_name).click()

    def clickErrorActiveCheckbox(self):
        sleep(1)
        self.driver.find_element_by_name(self.error_active_checkbox_name).click()
    
    def clickCreatePhoneLookupbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.phn_lookup_create_btn_class).click()

    def clickPhoneLookupEditBtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.phone_lookup_edit_href_link).click()

    
    def setEditTitleName(self, title):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_title_name).clear()
        self.driver.find_element_by_name(self.textbox_title_name).send_keys(title)

    def setEditPhoneLookUpMessage(self, message):
        sleep(1)
        self.driver.find_element_by_name(self.phone_lookup_message_name).clear()
        self.driver.find_element_by_name(self.phone_lookup_message_name).send_keys(message)

    def setEditPhoneLookUpErrorTriger(self, error_triger):
        sleep(1)
        self.driver.find_element_by_name(self.phone_lookup_error_triger_name).clear()
        self.driver.find_element_by_name(self.phone_lookup_error_triger_name).send_keys(error_triger)

    def clickEditSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_organization_edit_name).click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_organization_edit_name).click()        
        self.driver.find_element_by_xpath("//*[@id='phone_lookup_select']/option[5]").click()
        sleep(1)

    def clickUpdatePhoneLookupbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.phn_lookup_update_btn_class).click()

    def clickDeletePhoneLookup(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.delete_phn_lookup_link_text).click()

    def clickConfirmDeletePhnLookup(self):
        sleep(3)
        # self.driver.find_element_by_link_text(self.confirn_delete_phn_lookup_link_text).click()
        self.driver.find_element_by_class_name(self.confirn_delete_phn_lookup_class).click()

    def clickRunLookup(self):
        self.driver.find_element_by_class_name(self.run_phnlookup_class).click()

    def clickuploadimage(self):
        sleep(2)
        upload_file = self.driver.find_element_by_css_selector('.dz-hidden-input')
        upload_file.send_keys(os.path.abspath("assets/upload_file/Bannerv2.png"))
        self. driver.find_element_by_css_selector('.dz-image').is_displayed()
