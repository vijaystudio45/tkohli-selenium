from time import sleep

class TelnyxApiDemoClass:
    telnyx_api_demo_href_link = "Telnyx API Demo"
    telnyx_api_demo_phone_number_name = "phone_number"
    telnyx_api_demo_message_name = "message"
    telnyx_api_demo_btn_class = "btn-primary"

    def __init__(self, driver):
        self.driver = driver

    def clickTelnyxApiDemo(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.telnyx_api_demo_href_link).click()

    def setTelnyxApiPhoneNumberName(self, telnyxApiPhoneNumber):
        sleep(1)
        self.driver.find_element_by_name(self.telnyx_api_demo_phone_number_name).clear()
        self.driver.find_element_by_name(self.telnyx_api_demo_phone_number_name).send_keys(telnyxApiPhoneNumber)

    def setTelnyxApiMessageName(self, telnyxApiMessage):
            sleep(1)
            self.driver.find_element_by_name(self.telnyx_api_demo_message_name).clear()
            self.driver.find_element_by_name(self.telnyx_api_demo_message_name).send_keys(telnyxApiMessage)

    def clickTelnyxApiDemobtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.telnyx_api_demo_btn_class).click()