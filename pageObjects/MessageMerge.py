from time import sleep

class MessagemergeClass:
    message_merges_href_link = "Message Merges"
    create_message_merges_href_link = "Create Message Merge"
    merge_key_name = 'title'
    short_description_name = "description"
    full_description_name = "full_description"
    dropdown_message_merge_name = "org_id"
    checkbox_message_merge_name = "active_global_ignore"
    message_merge_create_btn_class = "create_message_merge_btn"
    edit_message_merge_class = "action_btns"
    message_merge_update_btn_class = "update_messagemerge_btn"
    #remove_campaign_link = "Remove"
    remove_msg_merge_btn_class = "delete_message_merge_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickMessageMerge(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.message_merges_href_link).click()

    def clickCreateMessageMerge(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_message_merges_href_link).click()

    def setMessageMergeKey(self, mergeKey):
        sleep(1)
        self.driver.find_element_by_name(self.merge_key_name).clear()
        self.driver.find_element_by_name(self.merge_key_name).send_keys(mergeKey)

    def setMessageShortDes(self, messageShortDes):
        sleep(1)
        self.driver.find_element_by_name(self.short_description_name).clear()
        self.driver.find_element_by_name(self.short_description_name).send_keys(messageShortDes)

    def setMessageFulltDes(self, messageFulltDes):
        sleep(1)
        self.driver.find_element_by_name(self.full_description_name).clear()
        self.driver.find_element_by_name(self.full_description_name).send_keys(messageFulltDes)

    def clickSelectMessageOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_message_merge_name).click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_message_merge_name).click()
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)


    def clickMessageMergeCheckbox(self):
        sleep(1)
        self.driver.find_element_by_name(self.checkbox_message_merge_name).click()

    def clickMessagemergesbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.message_merge_create_btn_class).click()

    def clickMessageMergeEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_message_merge_class).click()

    def click_msg_merge_update_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.message_merge_update_btn_class).click()

    def clickRemoveMessageMerge(self):
        sleep(3)
        self.driver.find_element_by_class_name(self.remove_msg_merge_btn_class).click()


    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()
