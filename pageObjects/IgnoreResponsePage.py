from time import sleep


class IgnoreResponseClass:
    ignore_response_href_link = "Ignored Responses"
    dropdown_ignore_response_organization_id = "new_organizationId"
    click_org_dropdown_btn_class = "Seach_ignore_response_organization"
    click_export_csv_btn_class = "responseExport_to_csv"
    click_download_btn_class = "download_ignoreResponse_conversation_history"
    click_update_single_response_btn_class = "change_ignore_status"
    active_checkbox_class_past_response = "edit_single_new_response"
    click_multiple_ignore_btn_class = "edit_multiple_ignore_response_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickignoreresponseLink(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.ignore_response_href_link).click()

    def clickIgnoreReponseSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_id(self.dropdown_ignore_response_organization_id).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='new_organizationId']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_id(self.dropdown_ignore_response_organization_id).click()


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
        self.driver.find_element_by_class_name(self.active_checkbox_class_past_response).click()

    def click_Multiple_ignore_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_multiple_ignore_btn_class).click()

    def click_ignore_response_chat_popup_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("get_response_ignore_msg").click()

    def settextareaName(self, textareaName):
        sleep(1)
        self.driver.find_element_by_name("msg").clear()
        self.driver.find_element_by_name("msg").send_keys(textareaName)

    def click_ignore_response_chat_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("response_ignore_chatbtn").click()

    def click_ignore_response_chat_close_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name("close").click()


