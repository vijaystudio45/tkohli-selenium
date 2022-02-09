from time import sleep

class orgadminConversationhistoryClass:
    conversation_history_href_link = "Conversation History"
    click_conversation_history_filter_range_btn = "GenrateMsgHstry"
    textbox_message = "msg"

    def __init__(self, driver):
        self.driver = driver

    def clickconversationhistorybtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.conversation_history_href_link).click()

    def clickSelectdatepicker(self):
        sleep(2)
        self.driver.find_element_by_id("msgconersationrange").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[1]").click()

    def click_conversation_history_filter_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_conversation_history_filter_range_btn).click()

    def click_popup_conversation_history_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("get_conversation_msg").click()

    def setpoupuptextbox(self, response_message):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_message).clear()
        self.driver.find_element_by_name(self.textbox_message).send_keys(response_message)

    def click_popup_send_message_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("sendMsgBtn").click()

    def click_popup_close_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("close").click()

    def download_conversation_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("download_conversation_history").click()