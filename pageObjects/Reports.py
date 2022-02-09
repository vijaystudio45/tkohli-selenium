from time import sleep

class ReportsClass:
    reports_href_link = "Reports"
    view_report_campaign_css_selector = "#campaign_result_table > tbody > tr > td:nth-child(1) > a"
    view_report_campaign_export_csv_btn_class = "export_to_csv_report"
    view_report_unsigned_campaign_export_csv_btn_class = "export_to_csv_unsignedreport"

    def __init__(self, driver):
        self.driver = driver

    def clickReportbtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.reports_href_link).click()


    def clickvewReportcampaignbtn(self):
        sleep(2)
        self.driver.find_element_by_css_selector(self.view_report_campaign_css_selector).click()


    def clickvewReportcampaignexportcsvbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.view_report_campaign_export_csv_btn_class).click()


    def clickvewReportunsignedcampaignbtn(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='unsignedcampaign_result_table']/tbody/tr/td[1]/a").click()


    def clickvewReportunsignedcampaignexportcsvbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.view_report_unsigned_campaign_export_csv_btn_class).click()