from time import sleep

class chatagentignoreresponseClass:
    chatagent_href_link = "Ignored Responses"
    textbox_chatagent_message = "msg"

    def __init__(self, driver):
        self.driver = driver

    def clickchatagentignoreresponse(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.chatagent_href_link).click()

    def clickSelectdatepicker(self):
        sleep(2)
        self.driver.find_element_by_id("msgnewresponserange").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[6]").click()

    def click_select_range_date_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("GenrateMsgresponse").click()

    def click_popup_chat_agent_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("get_response_ignore_msg").click()

    def setchatagentpoupuptextbox(self, ignore_response_message):
        sleep(2)
        self.driver.find_element_by_name(self.textbox_chatagent_message).clear()
        self.driver.find_element_by_name(self.textbox_chatagent_message).send_keys(ignore_response_message)

    def click_popup_chat_agent_send_message_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("response_ignore_chatbtn").click()

    def click_popup_close_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("close").click()

    def download_ignoreresponse_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("download_ignore_Response_conversation_history").click()

    def update_ignoreresponse_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("change_ignore_status").click()