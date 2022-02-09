from time import sleep

class SignalWireDemoClass:
    signal_wire_href_link = "Signalwire Demo"
    textbox_mobileNumber_name = "to"
    textbox_msg_name = "body"
    signalwire_submit_btn_id = "submit"


    def __init__(self, driver):
        self.driver = driver

    def clickSignalWire(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.signal_wire_href_link).click()

    def setSignalWireMobileNumber(self, signalMobileNumber):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_mobileNumber_name).clear()
        self.driver.find_element_by_name(self.textbox_mobileNumber_name).send_keys(signalMobileNumber)

    def setSignalWireMessage(self, signalMessage):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_msg_name).clear()
        self.driver.find_element_by_name(self.textbox_msg_name).send_keys(signalMessage)

    def clickSignalWireSubmitebtn(self):
        sleep(2)
        self.driver.find_element_by_id(self.signalwire_submit_btn_id).click()

    def setlongcodeFromDropdown(self):
        sleep(2)
        self.driver.find_element_by_name("longcode").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='abacus']/div[3]/select/option[2]").click()
        sleep(1)
        self.driver.find_element_by_name("longcode").click()

    