from time import sleep

class MessagemergeparserClass:
    message_merges_parser_href_link = "Message Merge Parser"
    dropdown_message_merge_parser_name = "admin_parser_org_id"
    message_merge_parser_string_name = "string"
    message_merge_parser_create_btn_class = "btn-danger"

    def __init__(self, driver):
        self.driver = driver

    def clickMessageMergeParser(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.message_merges_parser_href_link).click()

    def clickSelectMessageMergeParser(self):

            sleep(2)
            self.driver.find_element_by_name(self.dropdown_message_merge_parser_name).click()
            sleep(1)
            self.driver.find_element_by_name(self.dropdown_message_merge_parser_name).click()
            self.driver.find_element_by_xpath("//select[@name='admin_parser_org_id']/option[text()='Automation-organization-updated']").click()
            sleep(1)

    def setMessageMergeParserName(self, mergeparserKey):
        sleep(1)
        self.driver.find_element_by_name(self.message_merge_parser_string_name).clear()
        self.driver.find_element_by_name(self.message_merge_parser_string_name).send_keys(mergeparserKey)

    def clickMessagemergesparserbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.message_merge_parser_create_btn_class).click()