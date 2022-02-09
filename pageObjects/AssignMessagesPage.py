from time import sleep


class AssignMessageClass:
    assign_message_href_link = "Assign Messages"
    dropdown_assign_msg_sender_name = "sender"
    dropdown_assign_msg_type_name = "type"
    assign_amount_name = "assign_amount"
    checkbox_assign_message_name = "claim_messages"
    submit_btn_class = "submit_am_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickAssignMessage(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.assign_message_href_link).click()

    def clickAssignMsgSender(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_assign_msg_sender_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='sender']/option[text()='Vijay Kumar']").click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_assign_msg_sender_name).click()
        sleep(1)

    def clickAssignMsgType(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_assign_msg_type_name).click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_assign_msg_type_name).click()
        self.driver.find_element_by_xpath("//select[@name='type']/option[text()='Any']").click()
        sleep(1)

    def setAssignAmountName(self, assignAmount):
        sleep(1)
        self.driver.find_element_by_name(self.assign_amount_name).clear()
        self.driver.find_element_by_name(self.assign_amount_name).send_keys(assignAmount)

    def clickAssignMessageCheckbox(self):
        sleep(1)
        self.driver.find_element_by_name(self.checkbox_assign_message_name).click()

    def submitdBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.submit_btn_class).click()

