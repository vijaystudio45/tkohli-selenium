from time import sleep

class ManagemessagesClass:
    manage_messages_href_link = "Manage Messages"
    change_state_href_link = "Change State"
    dropdown_organization_name = "organizationId"
    click_edit_manage_messages_btn = "action_btns"
    click_filter_org_btn = "Seach_by_organization"
    remove_manage_messages_link = "Remove"
    textbox_unsend_messages_phone_number = "tbl_val"
    update_unsend_messages_btn = "update_unsent_message_btn"
    state_update_unsend_messages_btn = "update_subscreen_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickManagemessagebtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.manage_messages_href_link).click()


    def clickManagemessagestatebtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.change_state_href_link).click()

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_id(self.dropdown_organization_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='organizationId']/option[24]").click()
        sleep(1)
        self.driver.find_element_by_id(self.dropdown_organization_name).click()


    def click_filter_org_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_filter_org_btn).click()

    def click_edit_manage_messages_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_edit_manage_messages_btn).click()

    def setunsendmessagesphonenumber(self, unsend_messages_phone_number):
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='update_unsent_message_form']/div[2]/input[2]").clear()
        self.driver.find_element_by_xpath("//*[@id='update_unsent_message_form']/div[2]/input[2]").send_keys(unsend_messages_phone_number)

    def setunsendmessages_replay(self, unsend_messages_replay):
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='update_unsent_message_form']/div[3]/input[2]").clear()
        self.driver.find_element_by_xpath("//*[@id='update_unsent_message_form']/div[3]/input[2]").send_keys(unsend_messages_replay)


    def click_update_unsend_messages_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.update_unsend_messages_btn).click()

    def clickRemovemanagemessageLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_manage_messages_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()


    def clickSelectstatedropdown(self):
        sleep(2)
        self.driver.find_element_by_name("sub_message").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[1]/td[5]/select/option[2]").click()
        sleep(1)
        self.driver.find_element_by_name("sub_message").click()


    def click_state_update_unsend_messages_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.state_update_unsend_messages_btn).click()