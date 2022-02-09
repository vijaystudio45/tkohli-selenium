from time import sleep
import os

class MessageSendersClass:
    message_senders_href_link = "Message Senders"
    textbox_messsage_senders_class = "message_input"
    message_senders_radio_btn_id = "check_all"
    send_message_btn_class = "send_messages"

    def __init__(self, driver):
        self.driver = driver

    def clickMessageSenders(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.message_senders_href_link).click()

    def setMessageSendersMessage(self, message):
        sleep(1)
        self.driver.find_element_by_class_name(self.textbox_messsage_senders_class).clear()
        self.driver.find_element_by_class_name(self.textbox_messsage_senders_class).send_keys(message)

    def clickuploadimage(self):
        sleep(2)
        self.driver.find_element_by_class_name("media_url_input").send_keys(os.path.abspath("assets/upload_file/Bannerv2.png"))

    def clickRadioButton(self):
        sleep(2)
        self.driver.find_element_by_id(self.message_senders_radio_btn_id).click()

    def clickSendMessageButton(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.send_message_btn_class).click()




