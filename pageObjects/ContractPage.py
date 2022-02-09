from time import sleep
from selenium.common.exceptions import NoSuchElementException

class ContractClass:
    view_contract_href_link_button = "Contract"
    textbox_contract_id = "version_tag"
    create_contract_href_link_button = "Create Contract"
    textbox_payrate_id = "pay_rate"
    textarea_contract_tag_name = "iframe"
    active_checkbox_name = "check"
    active_checkbox_id = "active_ind"
    button_save_contract_class = "button-blue"
    button_update_contract_class = "updateContractBtn"
    button_edit_contract_class = "action_btns"

    def __init__(self, driver):
        self.driver = driver

    def clickviewContract(self):
        self.driver.find_element_by_link_text(self.view_contract_href_link_button).click()

    def clickCreateContract(self):
        self.driver.find_element_by_link_text(self.create_contract_href_link_button).click()

    def setContractName(self, contact):
        sleep(1)
        self.driver.find_element_by_id(self.textbox_contract_id).clear()
        self.driver.find_element_by_id(self.textbox_contract_id).send_keys(contact)

    def setPayRate(self, payRate):
        sleep(1)
        self.driver.find_element_by_id(self.textbox_payrate_id).clear()
        self.driver.find_element_by_id(self.textbox_payrate_id).send_keys(payRate)

    def setContractTextArea(self, textArea):
        sleep(1)
        iframe = self.driver.find_element_by_tag_name(self.textarea_contract_tag_name)
        self.driver.switch_to.frame(iframe)
        tinymce = self.driver.find_element_by_tag_name("body")
        tinymce.clear()
        tinymce.send_keys(textArea)
        self.driver.switch_to.default_content()

    def clickActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_checkbox_name).click()
        # self.driver.find_element_by_id(self.active_checkbox_id).Selected

    def clickSaveContract(self):
        sleep(1)
        self.driver.find_element_by_class_name(self.button_save_contract_class).click()
        # self.driver.clickActiveCheckbox(self.button_save_contract_xpath).click()

    def clickeditContract(self):
        sleep(1)
        self.driver.find_element_by_class_name(self.button_edit_contract_class).click()
        # self.driver.clickActiveCheckbox(self.button_save_contract_xpath).click()

    def clickUpdateContract(self):
        sleep(1)
        # self.driver.find_element_by_xpath(self.button_update_contract_xpath).click()
        self.driver.find_element_by_class_name(self.button_update_contract_class).click()
