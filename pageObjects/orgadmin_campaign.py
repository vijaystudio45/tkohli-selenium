from time import sleep
import os
class CampaignorgadminClass:
    campaigns_href_link = "Manage Campaigns"
    create_campaigns_href_link = "Create Campaigns"
    textbox_campaign_id = "campaign_name"
    continue_campaigns_id = "f_frm_continue"
    textbox_message_name = "message"
    campaigns_create_btn_class = "add_campiagn_btn"
    edit_campaign_class = "action_btns"
    campaigns_update_btn_class = "update_campaigns_btn"
    remove_campaign_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickCampaigns(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.campaigns_href_link).click()

    def clickCreateCampaigns(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_campaigns_href_link).click()

    def setCampaignName(self, campaignName):
        sleep(1)
        self.driver.find_element_by_id(self.textbox_campaign_id).clear()
        self.driver.find_element_by_id(self.textbox_campaign_id).send_keys(campaignName)

    def clickcampaigncsv(self):
        sleep(2)
        upload_file = self.driver.find_element_by_css_selector('.dz-hidden-input')
        upload_file.send_keys(os.path.abspath("assets/upload_file/campaignTemplateCSV.csv"))
        self.driver.find_element_by_css_selector('.dz-image').is_displayed()

    def clickstartdate(self):
        sleep(2)
        self.driver.find_element_by_id("s_start_date").click()
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/a[2]").click()
        self.driver.find_element_by_css_selector("#ui-datepicker-div > table > tbody > tr:nth-child(3) > td:nth-child(5) > a").click()

    def click_Selectstart_time(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='add_campaigns_form']/div[1]/div[3]/div/div[2]/div[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_campaigns_form']/div[1]/div[3]/div/div[2]/div[1]/ul/li[11]").click()


    def clickenddate(self):
        sleep(2)
        self.driver.find_element_by_id("s_end_date").click()
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/a[2]").click()
        self.driver.find_element_by_css_selector("#ui-datepicker-div > table > tbody > tr:nth-child(4) > td:nth-child(6) > a").click()


    def click_Select_end_time(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='add_campaigns_form']/div[1]/div[3]/div/div[5]/div[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_campaigns_form']/div[1]/div[3]/div/div[5]/div[1]/ul/li[24]").click()

    def clickCampaignContinue(self):
        sleep(2)
        self.driver.find_element_by_id(self.continue_campaigns_id).click()

    def setCampaignMessage(self, campaignMessage):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_message_name).clear()
        self.driver.find_element_by_name(self.textbox_message_name).send_keys(campaignMessage)

    def click_Select_business_unit(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='add_campaigns_form']/div[2]/div[3]/div/div").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_campaigns_form']/div[2]/div[3]/div/div/ul/li[2]").click()

    def clickCampaignsbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.campaigns_create_btn_class).click()

    def clickCampaignEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_campaign_class).click()

    def click_campaigns_update_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.campaigns_update_btn_class).click()


    def click_edit_Selectstart_time(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='update_campaigns_form']/div[1]/div[3]/div/div[2]/div").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='update_campaigns_form']/div[1]/div[3]/div/div[2]/div/ul/li[2]").click()


    def click_edit_Select_end_time(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='update_campaigns_form']/div[1]/div[3]/div/div[5]/div").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='update_campaigns_form']/div[1]/div[3]/div/div[5]/div/ul/li[18]").click()



    def clickRemoveCampaign(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_campaign_link).click()


    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/button").click()


