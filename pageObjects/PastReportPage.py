from time import sleep

class PastReportClass:
    view_past_report_href_link_button = "Past Reports"
    download_past_report_Class = "download-file-past-report-from-bucket"
    remove_past_report_class = "action_btns"
    confirm_delete_report_xpath = "/html/body/div[10]/div/div[3]/div[2]/button"
    click_select_dropdown_org = "add_pastorg_id"
    org_filter_btn_class = "get_organization"
    date_range_filter_btn_class = "get_reportpaste_data"

    def __init__(self, driver):
        self.driver = driver



    def clickviewpastreport(self):
        self.driver.find_element_by_link_text(self.view_past_report_href_link_button).click()
    def ckeckDownloadPastReportDisplay(self):
        sleep(1)
        # check_download_display = self.driver.find_element_by_class_name(self.download_past_report_Class)
        self.driver.find_element_by_class_name(self.download_past_report_Class).is_displayed()
        # check_download_display.is_displayed()

    def clickDownloadPastReport(self):
        sleep(1)
        self.driver.find_element_by_class_name(self.download_past_report_Class).click()

    def clickRemovePastContract(self):
        sleep(3)
        self.driver.find_element_by_class_name(self.remove_past_report_class).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath(self.confirm_delete_report_xpath).click()


    def clickSelectorg1(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_org).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_pastorg_id']/option[32]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_select_dropdown_org).click()

    def clickSelectorg2(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_org).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_pastorg_id']/option[3]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_select_dropdown_org).click()


    def clickOrgfilterbtn(self):
        sleep(3)
        self.driver.find_element_by_class_name(self.org_filter_btn_class).click()
