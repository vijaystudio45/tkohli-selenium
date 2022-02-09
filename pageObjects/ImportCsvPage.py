from time import sleep
import os
class ImportCsvClass:
    import_csv_href_link = "Import CSV"
    upload_file_csv_name = "csv_file"
    import_csv_btn_class = "btn-danger"
    dropdown_import_csv_id = "select_tables"
    select_import_csv_btn_class = "import_csv_file_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickImportCsv(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.import_csv_href_link).click()

    def setUploadCsvFile(self, uploadCsvFile):
        sleep(1)
        self.driver.find_element_by_name(self.upload_file_csv_name).clear()
        self.driver.find_element_by_name(self.upload_file_csv_name).send_keys(uploadCsvFile)

    def clickuploadfile(self):
        sleep(2)
        self.driver.find_element_by_id("csv_file").send_keys(os.path.abspath("assets/upload_file/campaign-csv-endtime.csv"))

    def importCsvBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.import_csv_btn_class).click()

    def clickImportCsvSelect(self):
        sleep(2)
        self.driver.find_element_by_id(self.dropdown_import_csv_id).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='select_tables']/option[text()='messages']").click()
        self.driver.find_element_by_id(self.dropdown_import_csv_id).click()

    def importCsvSelectBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.select_import_csv_btn_class).click()




