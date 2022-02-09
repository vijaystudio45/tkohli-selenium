from time import sleep

class SendingClass:
    sending_href_link = "Start Sending"
    sending_view_btn_class = "right_send_btn"
    textbox_DownloadMessageAmmount_name = "download_amount"
    claimed_message_btn_class ="download_button"
    sending_message_btn_class = "multiple_message_send_btn"

    def __init__(self, driver):
        self.driver = driver


    def clicksenderbtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sending_href_link).click()

    def Sending_Process_view_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.sending_view_btn_class).click()

    def setEnterDownloadMessageAmmount(self, DownloadMessageAmmount):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_DownloadMessageAmmount_name).clear()
        self.driver.find_element_by_name(self.textbox_DownloadMessageAmmount_name).send_keys(DownloadMessageAmmount)

    def download_claimed_message_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.claimed_message_btn_class).click()

    def Sending_message_btn_class(self):
        sleep(2)
        for i in range(1, 11):
            self.driver.find_element_by_class_name(self.sending_message_btn_class).click()