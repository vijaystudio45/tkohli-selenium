from time import sleep
import os
class delimitedimportClass:
    delimited_href_link = "Delimited Import"

    def __init__(self, driver):
        self.driver = driver

    def clickdelimitedbtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.delimited_href_link).click()

    def clickuploadfile(self):
        sleep(2)
        self.driver.find_element_by_id("txt_file").send_keys(os.path.abspath("assets/upload_file/delimited.txt"))

    def clicksubmitbtn(self):
        sleep(2)
        self.driver.find_element_by_id("upload_delimited_file_button").click()

