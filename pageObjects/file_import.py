from time import sleep

class FileimportClass:
    file_import_href_link = "File Import"
    file_import_btn = "import_file_button"
    click_select_table = "table_select"
    save_file_import_btn = "save_file_data_btn"
    skip_file_import_btn = "skip_file_button"

    def __init__(self, driver):
        self.driver = driver

    def clickfileimportbtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.file_import_href_link).click()

    def click_file_import_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.file_import_btn).click()


    def fileimportdropdowntable(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_table).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='table_select']/option[text()='messages']").click()
        self.driver.find_element_by_id(self.click_select_table).click()


    def click_save_file_import_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.save_file_import_btn).click()

    def click_skip_file_import_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.skip_file_import_btn).click()

    def clickmultipleignoreCheckbox(self):
        self.driver.find_element_by_id("ignore_check_all").click()

    def click_multiple_ignore_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name("ignore_multiple_files_button").click()