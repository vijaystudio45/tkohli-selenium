from time import sleep

class LogFileClass:
    log_file_href_link = "Log File"

    def __init__(self, driver):
        self.driver = driver

    def clickLogFile(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.log_file_href_link).click()

    def clickdownloadLogFile(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData12']/tbody/tr/td[3]/a").click()

    def clickRemove_logfile_Linkbtn(self):
        sleep(3)
        self.driver.find_element_by_link_text("Remove").click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()
