from time import sleep

class SendingDemoClass:
    sending_demo_href_link = "Sending Demo"
    sending_demo_phone_number_name = "demo_phone_number"
    sending_demo_btn_class = "demo_send_msg_btn"
    sending_demo_create_btn = "sending_msg_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickSendingDemo(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sending_demo_href_link).click()

    def setSendPhoneNumberName(self, sendingPhoneNumber):
        sleep(1)
        self.driver.find_element_by_name(self.sending_demo_phone_number_name).clear()
        self.driver.find_element_by_name(self.sending_demo_phone_number_name).send_keys(sendingPhoneNumber)

    def clickSendingDemobtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.sending_demo_btn_class).click()

    def clickDemoSendingCreateBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.sending_demo_create_btn).click()