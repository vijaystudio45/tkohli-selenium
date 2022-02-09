from time import sleep

class ApiKeyClass:
    Organizations_href_link = "Manage Organizations"
    org_apikey_btn_text = "Automation-organization-updated"
    create_api_key_href_link = "Create Api Key"
    textbox_api_keys = "api_key"
    active_checkbox_name = "active_status_api"
    api_key_create_btn_class = "create_apikey_btn"
    api_key_edit_btn_class = "action_btns"
    api_key_update_btn_class = "update_apikey_btn"
    remove_api_key_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickorgbtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.Organizations_href_link).click()

    def clickorgapibtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.org_apikey_btn_text).click()

    def clickcreateapikeybtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_api_key_href_link).click()

    def setapikey(self, api_keys):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_api_keys).clear()
        self.driver.find_element_by_name(self.textbox_api_keys).send_keys(api_keys)

    def clickdatepickertest(self):
        sleep(2)
        self.driver.find_element_by_id("start_date").click()
        self.driver.find_element_by_id("start_date").clear()
        self.driver.find_element_by_xpath("//*[@id='datepickers-container']/div/nav/div[3]").click()
        self.driver.find_element_by_css_selector("#datepickers-container > div > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(25)").click()


    def clickActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_checkbox_name).click()

    def clickapikeycreatebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.api_key_create_btn_class).click()


    def clickapikeyeditbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.api_key_edit_btn_class).click()

    def clickapikeyupdatebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.api_key_update_btn_class).click()

    def clickRemoveApikeyLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_api_key_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div[3]/div[2]/button').click()
