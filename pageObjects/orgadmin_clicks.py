from time import sleep

class Orgadmin_clickClass:
    click_text = "Clicks"
    click_date_filter ="/html/body/div[2]/div[1]/ul/li[6]"
    click_filter_btn_text ="get_clicks_data"

    def __init__(self, driver):
        self.driver = driver

    def click_page_link(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.click_text).click()

    def check_filter_date(self):
        self.driver.find_element_by_id("clicksrange").click()
        self.driver.find_element_by_xpath(self.click_date_filter).click()

    def check_filter_date_btn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_filter_btn_text).click()