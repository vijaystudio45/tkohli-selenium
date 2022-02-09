from time import sleep

class SendingMessagesClass:
    sending_message_href_link = "Sending Messages"
    enter_amount_name = "download_amount"
    download_btn_class = "download_button"

    def __init__(self, driver):
        self.driver = driver

    def clickSendingMessage(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sending_message_href_link).click()

    def setEnterAmountName(self, enterAmount):
        sleep(1)
        self.driver.find_element_by_name(self.enter_amount_name).clear()
        self.driver.find_element_by_name(self.enter_amount_name).send_keys(enterAmount)

    def downloadBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.download_btn_class).click()