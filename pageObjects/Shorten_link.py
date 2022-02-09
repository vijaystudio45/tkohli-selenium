from time import sleep

class Shorten_link_Class:
    shorten_href_link = "Shorten Link"
    dropdown_org_name = "org_id"
    textbox_url_name = "url"
    textbox_shorten_expire_name = "shorten_expire"
    textbox_shorten_expire_id = "shorten_date"
    shorten_link_create_btn_class = "shorten_url_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickCreateShortenUrl(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.shorten_href_link).click()

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_org_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_org_name).click()

    def setShortenurlName(self, shortenUrl):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_url_name).clear()
        self.driver.find_element_by_name(self.textbox_url_name).send_keys(shortenUrl)


    def setExpireTime(self, shortenUrl_Time):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_shorten_expire_name).clear()
        self.driver.find_element_by_name(self.textbox_shorten_expire_name).send_keys(shortenUrl_Time)

    def clicksetExpireTime(self):
        sleep(2)
        self.driver.find_element_by_id("shorten_date").click()
        self.driver.find_element_by_id("shorten_date").clear()
        self.driver.find_element_by_xpath("//*[@id='datepickers-container']/div/nav/div[3]").click()
        self.driver.find_element_by_css_selector("#datepickers-container > div > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(29)").click()

    def clickShortenUrl(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.shorten_link_create_btn_class).click()