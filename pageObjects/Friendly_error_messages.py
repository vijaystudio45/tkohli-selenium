from time import sleep

class FriendlyerrorClass:
    friendly_error_messages_href_link = "Friendly Message"
    friendly_error_create_messages_href_link = "Create Friendly Message"
    textbox_error_id = "error_id"
    textbox_friendly_title = "friendly_title"
    textbox_friendly_description = "description"
    textbox_friendly_provider = "provider"
    create_friendly_messages_btn = "create_Friendly_Error_btn"
    edit_friendly_messages_btn = "action_btns"
    update_friendly_messages_btn = "update_Friendly_Error_btn"
    remove_friendly_message_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickfriendlymessagebtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.friendly_error_messages_href_link).click()

    def clickcreatefriendlymessagebtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.friendly_error_create_messages_href_link).click()

    def seterrorid(self, error_id):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_error_id).clear()
        self.driver.find_element_by_name(self.textbox_error_id).send_keys(error_id)

    def seterrorfriendlytitle(self, friendly_title):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_friendly_title).clear()
        self.driver.find_element_by_name(self.textbox_friendly_title).send_keys(friendly_title)


    def seterrorfriendlydescription(self, friendly_description):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_friendly_description).clear()
        self.driver.find_element_by_name(self.textbox_friendly_description).send_keys(friendly_description)


    def seterrorfriendlyprovider(self, friendly_provider):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_friendly_provider).clear()
        self.driver.find_element_by_name(self.textbox_friendly_provider).send_keys(friendly_provider)

    def click_create_friendly_messages_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.create_friendly_messages_btn).click()



    def click_edit_friendly_messages_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_friendly_messages_btn).click()

    def click_update_friendly_messages_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.update_friendly_messages_btn).click()


    def clickRemovefriendlymessageLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_friendly_message_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()