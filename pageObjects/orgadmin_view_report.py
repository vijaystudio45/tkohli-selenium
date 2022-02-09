from time import sleep

class Reports_orgadmin_Class:

    reports_href_link = "Reports"
    view_report_campaign_css_selector = "#campaign_result_table > tbody > tr:nth-child(1) > td:nth-child(1) > p > a"
    view_report_unsigned_campaign ="//*[@id='unsigned_campaign_data_table']/tbody/tr/td[1]/a"
    view_report_response_btn ="//*[@id='response_result_table']/tbody/tr[1]/td[1]/a"

    def __init__(self, driver):
        self.driver = driver

    def clickReportbtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.reports_href_link).click()

    def clickvewReportcampaignbtn(self):
        sleep(2)
        self.driver.find_element_by_css_selector(self.view_report_campaign_css_selector).click()

    def clickvewReportunsignedcampaignbtn(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.view_report_unsigned_campaign).click()

    def clickvewReportresponsebtn(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.view_report_response_btn).click()