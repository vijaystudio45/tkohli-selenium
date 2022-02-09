from time import sleep
import os

class SendingMessagesAdminClass:
    sending_messages_href_link = "Sending Messages"
    inputbox_download_amount_id = "download_amount"
    multiple_msg_send_btn_class = "multiple_message_send_btn"
    download_btn_class = "download_button"

    def __init__(self, driver):
        self.driver = driver

    def clickSendingMessages(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sending_messages_href_link).click()

    def setMessageClaim(self, amount_for_messages_you_need_to_claim):
        sleep(1)
        self.driver.find_element_by_id(self.inputbox_download_amount_id).clear()
        self.driver.find_element_by_id(self.inputbox_download_amount_id).send_keys(amount_for_messages_you_need_to_claim)

    def clickDownloadButton(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.download_btn_class).click()

    def clickSendMessageButton(self):
        sleep(1)
        self.driver.find_element_by_class_name(self.multiple_msg_send_btn_class).click()




