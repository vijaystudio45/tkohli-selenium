from time import sleep

class ProcessedFilesClass:
    processed_files_href_link = "Processed Files"

    def __init__(self, driver):
        self.driver = driver

    def clickProcessedFile(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.processed_files_href_link).click()

