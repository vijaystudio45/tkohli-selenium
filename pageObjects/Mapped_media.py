from time import sleep
class MappedmediaClass:
    mapped_media_href_link = "Mapped Media"
    create_mapped_media_href_link = "Create Mapped Media"
    dropdown_organization_name = "org_id"
    textbox_file_name = "file_name"
    textbox_mapped_location = "mapped_location"
    create_mapped_media_btn = "create_mapped_media_btn"
    edit_mapped_media_btn = "action_btns"
    update_mapped_media_btn = "update_mapped_media_btn"
    remove_mapped_media_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickmappedmedia(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.mapped_media_href_link).click()

    def clickcreatemappedmedia(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_mapped_media_href_link).click()

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()


    def setfilename(self, file_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_file_name).clear()
        self.driver.find_element_by_name(self.textbox_file_name).send_keys(file_name)

    def setmappedlocation(self, mapped_location):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_mapped_location).clear()
        self.driver.find_element_by_name(self.textbox_mapped_location).send_keys(mapped_location)

    def click_create_mapped_media_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.create_mapped_media_btn).click()

    def click_edit_mapped_media_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_mapped_media_btn).click()

    def click_update_mapped_media_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.update_mapped_media_btn).click()

    def clickRemoveMappedMediaLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_mapped_media_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[9]/div/div[3]/div[2]/button").click()