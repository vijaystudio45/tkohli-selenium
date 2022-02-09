from time import sleep

class Orgadmin_PastReportClass:
    past_report_text = "Past Reports"
    past_report_date_filter = "/html/body/div[2]/div[1]/ul/li[3]"
    past_report_date_filter_btn = "get_reportpaste_data"
    past_report_download_btn = "download-file-past-report-from-user-bucket"
    remove_past_report_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def click_past_report(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.past_report_text).click()

    def check_filter_date(self):
        self.driver.find_element_by_id("reportpasterange").click()
        self.driver.find_element_by_xpath(self.past_report_date_filter).click()

    def check_filter_date_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.past_report_date_filter_btn).click()

    def check_download_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.past_report_download_btn).click()

    def clickRemovepastreportLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_past_report_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[2]/button').click()