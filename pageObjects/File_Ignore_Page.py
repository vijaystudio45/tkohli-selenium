from time import sleep

class FileIgnoreClass:
    file_ignore_href_link = "File Ignore"
    delete_file_ignore_btn_class = "delete_file"


    def __init__(self, driver):
        self.driver = driver

    def clickfileignorebtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.file_ignore_href_link).click()

    def click_delete_file_ignore_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.delete_file_ignore_btn_class).click()

    def click_delete_file_ignore_confirm_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name('swal-button--confirm').click()

    def click_file_ignore_process_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name('process_file').click()




