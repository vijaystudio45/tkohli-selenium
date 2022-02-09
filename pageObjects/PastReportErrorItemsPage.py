from time import sleep


class PastReportErrorItemsClass:
    view_past_report_href_link_button = "Past Reports Error Items"
    click_past_report_errpr_item_xpath = "/html/body/div[7]/div[2]/div[2]/table/tbody/tr[1]/td[5]/a"
    click_update_btn_class = "button-blue"

    def clickviewpastreporterroritems(self):
        self.driver.find_element_by_link_text(self.view_past_report_href_link_button).click()

    def __init__(self, driver):
        self.driver = driver

    def clickEditPastReportErrorItems(self):
        sleep(3)
        self.driver.find_element_by_xpath(self.click_past_report_errpr_item_xpath).click()

    def clickUpdateButton(self):
        sleep(3)
        self.driver.find_element_by_class_name(self.click_update_btn_class).click()
