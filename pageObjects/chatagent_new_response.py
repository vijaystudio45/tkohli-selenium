from time import sleep

class chatagentnewresponseClass:
    chatagent_href_link = "New Responses"
    textbox_chatagent_message = "msg"

    def __init__(self, driver):
        self.driver = driver

    def clickchatagentnewresponse(self):
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
        self.driver.find_element_by_class_name("get_response_new_msg").click()

    def setchatagentpoupuptextbox(self, new_response_message):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chatagent_message).clear()
        self.driver.find_element_by_name(self.textbox_chatagent_message).send_keys(new_response_message)

    def click_popup_chat_agent_send_message_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("save_response_new_chatbtn").click()

    def click_popup_close_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("close").click()

    def download_newresponse_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("download_new_Response_conversation_history").click()

    def update_newresponse_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("change_conversation_ignore").click()