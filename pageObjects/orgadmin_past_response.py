from time import sleep

class orgadminpastresponseClass:
    response_href_link = "Past Responses"
    textbox_message = "msg"

    def __init__(self, driver):
        self.driver = driver

    def clickpastresponse(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.response_href_link).click()

    def clickSelectdatepicker(self):
        sleep(2)
        self.driver.find_element_by_id("msgnewresponserange").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[3]").click()

    def click_select_range_date_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("GenrateMsgresponse").click()

    def click_popup_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("get_response_past_msg").click()

    def setpoupuptextbox(self, response_message):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_message).clear()
        self.driver.find_element_by_name(self.textbox_message).send_keys(response_message)

    def click_popup_send_message_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("save_response_past_chatbtn").click()

    def click_popup_close_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("close").click()

    def download_response_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("download_past_Response_conversation_history").click()

    def update_response_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("change_past_ignore").click()