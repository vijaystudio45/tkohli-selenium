class ClickClass:
    click_get_record_class = "get_clicks_data"
    click_href_link = "Clicks"

    def __init__(self, driver):
        self.driver = driver

    def clickShowRecordsByDate(self):
        self.driver.find_element_by_class_name(self.click_get_record_class).click()

    def clickpagebtn(self):
        self.driver.find_element_by_link_text(self.click_href_link).click()