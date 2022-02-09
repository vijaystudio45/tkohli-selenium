from time import sleep

class SenderClaimsClass:
    sender_claims_href_link = "Sender Claims"
    sender_claims_btn_class = "slow_sender_release_btn"

    def __init__(self, driver):
        self.driver = driver

    def clickSenderClaims(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sender_claims_href_link).click()

    def clickSenderClaimsbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.sender_claims_btn_class).click()

    def clickupdateSenderClaimsbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name("release_claims_btn").click()