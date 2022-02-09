class ReportorgadminSchedulerHistoryClass:

    report_href_link = "Reports Scheduler History"
    click_download_report = "download-reportfile-from-bucket"

    def __init__(self, driver):
        self.driver = driver

    def clickreportbtn(self):
        self.driver.find_element_by_link_text(self.report_href_link).click()


    def clickDownloadReport(self):
        self.driver.find_element_by_class_name(self.click_download_report).click()