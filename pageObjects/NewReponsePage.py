from time import sleep


class NewResponseClass:
    new_response_href_link = "New Responses"
    dropdown_organization_id = "new_organizationId"
    click_org_dropdown_btn_class = "Seach_response_organization"
    click_export_csv_btn_class = "response_export_to_csv"
    click_download_btn_class = "download_newResponse_conversation_history"
    click_update_single_response_btn_class = "change_conversation_ignore"
    active_checkbox_class_new_response = "edit_single_new_response"
    click_multiple_ignore_btn_class = "edit_multiple_new_response_btn"

    def __init__(self, driver):
        self.driver = driver

    def clicknewresponseLink(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.new_response_href_link).click()

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_id(self.dropdown_organization_id).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='new_organizationId']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_id(self.dropdown_organization_id).click()


    def click_Org_dropdown_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_org_dropdown_btn_class).click()

    def click_Export_csv_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_export_csv_btn_class).click()

    def click_download_csv_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_download_btn_class).click()

    def click_Update_single_response_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_update_single_response_btn_class).click()

    def clickActiveCheckbox(self):
        self.driver.find_element_by_class_name(self.active_checkbox_class_new_response).click()
        # self.driver.find_element_by_id(self.active_checkbox_id).Selected

    def click_Multiple_ignore_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_multiple_ignore_btn_class).click()

    def click_new_response_chat_popup_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("get_response_new_msg").click()

    def settextareaName(self, textareaName):
        sleep(1)
        self.driver.find_element_by_name("msg").clear()
        self.driver.find_element_by_name("msg").send_keys(textareaName)

    def click_new_response_chat_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("response_new_chatbtn").click()

    def click_new_response_chat_close_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("close").click()
