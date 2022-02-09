from time import sleep

class orgadminMessagemergeparserClass:
    message_merges_parser_href_link = "Message Merge Parser"
    message_merge_parser_string_name = "string"
    message_merge_parser_create_btn_class = "message_merge_user"
    click_select_dropdown_business_unit = "business_unit_id"

    def __init__(self, driver):
        self.driver = driver

    def clickMessageMergeParser(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.message_merges_parser_href_link).click()


    def setMessageMergeParserName(self, mergeparserKey):
        sleep(1)
        self.driver.find_element_by_name(self.message_merge_parser_string_name).clear()
        self.driver.find_element_by_name(self.message_merge_parser_string_name).send_keys(mergeparserKey)


    def clickMessagemergesparserbtn(self):
        sleep(2)
        self.driver.find_element_by_id(self.message_merge_parser_create_btn_class).click()


    def clickSelectbusinessunit(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_business_unit).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='business_unit_id']/option[2]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_business_unit).click()