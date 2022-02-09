from time import sleep

class ConversationhistoryClass:
    conversation_history_href_link = "Conversation History"
    dropdown_organization_name = "organizationId"
    click_conversation_history_filter_range_btn = "GenrateMsgHstry"
    click_conversation_history_download_btn = "download_conversation_history"

    def __init__(self, driver):
        self.driver = driver

    def clickconversationhistorybtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.conversation_history_href_link).click()

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_id(self.dropdown_organization_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='organizationId']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_id(self.dropdown_organization_name).click()

    def click_conversation_history_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_conversation_history_filter_range_btn).click()

    def click_download_conversation_history_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_conversation_history_download_btn).click()

    def click_conversation_history_chat_popup_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("get_conversation_msg1").click()

    def settextareaName(self, textareaName):
        sleep(1)
        self.driver.find_element_by_name("msg").clear()
        self.driver.find_element_by_name("msg").send_keys(textareaName)

    def click_conversation_history_chat_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("sendMsgBtn").click()

    def click_conversation_history_chat_close_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("close").click()