from time import sleep

class orgadminTodayCampaignsClass:
    today_campaigns_href_link = "Todays Campaigns"

    def __init__(self, driver):
        self.driver = driver

    def clickTodayCampaigns(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.today_campaigns_href_link).click()