from time import sleep

class ZipwhipSendingDemoClass:
    zipwhip_sending_demo_href_link = "Zipwhip Sending Demo"
    zipwhip_sending_demo_phone_number_id = "phoneNumber"
    zipwhip_sending_demo_message_id = "body"
    zipwhip_sending_demo_btn_class = "btn-primary"

    def __init__(self, driver):
        self.driver = driver

    def clickZipwhipSendingDemo(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.zipwhip_sending_demo_href_link).click()

    def setZipwhipSendPhoneNumberId(self, zipwhipsendingPhoneNumber):
        sleep(1)
        self.driver.find_element_by_id(self.zipwhip_sending_demo_phone_number_id).clear()
        self.driver.find_element_by_id(self.zipwhip_sending_demo_phone_number_id).send_keys(zipwhipsendingPhoneNumber)

    def setZipwhipSendPhoneMessageId(self, zipwhipsendingMessage):
            sleep(1)
            self.driver.find_element_by_id(self.zipwhip_sending_demo_message_id).clear()
            self.driver.find_element_by_id(self.zipwhip_sending_demo_message_id).send_keys(zipwhipsendingMessage)

    def clickZipwhipSendingDemobtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.zipwhip_sending_demo_btn_class).click()

