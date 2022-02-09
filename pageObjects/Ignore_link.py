from time import sleep


class IgnoreLinkClass:
    ignore_href_link = "Manage Ignore link"
    create_Ignore_href_link = "Create Ignore Link"
    textbox_ignore_domain_id = "domain_input"
    dropdown_organization_name = "org_id"
    active_checkbox_name = "active_status_Link"
    ignore_active_checkbox_name = "active_global_ignore"
    ignore_create_btn_class = "create_ignore_links_btn"
    edit_Ignore_link_class = "action_btns"
    Ignore_link_update_btn_class = "update_ignore_links_btn"
    remove_Ignore_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickIgnoreLink(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.ignore_href_link).click()

    def clickCreateIgnoreLink(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_Ignore_href_link).click()

    def setDomainName(self, DomainName):
        sleep(1)
        self.driver.find_element_by_id(self.textbox_ignore_domain_id).clear()
        self.driver.find_element_by_id(self.textbox_ignore_domain_id).send_keys(DomainName)

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()

    def clickActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_checkbox_name).click()
        # self.driver.find_element_by_id(self.active_checkbox_id).Selected

    def IgnoreclickActiveCheckbox(self):
        self.driver.find_element_by_name(self.ignore_active_checkbox_name).click()

    def clickIgnorebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.ignore_create_btn_class).click()

    def clickIgnorelinkEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_Ignore_link_class).click()

    def click_update_Ignore_link_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.Ignore_link_update_btn_class).click()

    def clickRemoveIgnoreLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_Ignore_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()
