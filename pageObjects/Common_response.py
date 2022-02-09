from time import sleep
import os

class CommonResponseClass:
    commonresponse_href_link = "Common Responses"
    create_common_response_href_link = "Create Common Response"
    textbox_synonyms = "synonyms"
    textbox_response = "response"
    textbox_response_message = "message"
    dropdown_organization_name = "org_id"
    create_common_response_class = "create_common_response_btn"
    edit_common_response_class = "action_btns"
    update_common_response_class = "update_response_btn"
    remove_common_response_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickCommonResponse(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.commonresponse_href_link).click()

    def clickCreateCommonResponse(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_common_response_href_link).click()

    def setResponse(self, Response):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_response).clear()
        self.driver.find_element_by_name(self.textbox_response).send_keys(Response)

    def setCommonResponsesynonyms(self, synonyms):
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_common_response_form']/div[1]/input").clear()
        self.driver.find_element_by_xpath("//*[@id='add_common_response_form']/div[1]/input").send_keys(synonyms)
        self.driver.find_element_by_xpath("//*[@id='add_common_response_form']/div[1]/input").click()

    def setResponseMessage(self, Response_message):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_response_message).clear()
        self.driver.find_element_by_name(self.textbox_response_message).send_keys(Response_message)


    def clickuploadimage(self):
        sleep(2)
        upload_file = self.driver.find_element_by_css_selector('.dz-hidden-input')
        upload_file.send_keys(os.path.abspath("assets/upload_file/Bannerv2.png"))
        self. driver.find_element_by_css_selector('.dz-image').is_displayed()


    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()

    def clickSelectbusinessunit(self):
        sleep(2)
        self.driver.find_element_by_name("business_unit_id").click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='business_unit_id']/option[text()='Automation-Business-unit-update']").click()
        sleep(1)
        self.driver.find_element_by_name("business_unit_id").click()


    def clickCreatecommonResponseBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.create_common_response_class).click()

    def clickEditcommonResponseBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_common_response_class).click()

    def clickUpdatecommonResponseBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.update_common_response_class).click()

    def clickRemoveCommonResponse(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_common_response_link).click()


    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()