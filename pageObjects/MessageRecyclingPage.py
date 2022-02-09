from time import sleep


class MessageRecyclingClass:
    message_recycling_href_link = "Message Recycling"
    # action_btns_text = 'Recycle'
    action_btn_class = 'recycle_btn'

    def __init__(self, driver):
        self.driver = driver

    def clickMessageRecycling(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.message_recycling_href_link).click()

    def clickRecycleBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.action_btn_class).click()



