from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()
CAMPAIGN_ORG_NAME = os.getenv('CAMPAIGN_ORG_NAME')
class CampaignClass:
    campaigns_href_link = "Manage Campaigns"
    create_campaigns_href_link = "Create Campaign"
    continue_campaigns_id = 'f_frm_continue'
    textbox_campaign_id = "campaign_name"
    textbox_start_date_name = "start_date"
    textbox_start_time_name = "start_time"
    textbox_end_date_name = "end_date"
    textbox_end_time_name = "end_time"
    textbox_timezone_name = "timezone"
    textbox_message_name = "message"
    dropdown_organization_name = "org_id"
    dropdown_business_unit_name = "business_unit_id"
    campaigns_create_btn_class = "add_campiagn_btn"
    campaigns_update_btn_class = "update_campaigns_btn"
    edit_campaign_class = "action_btns"
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

    def clickstartdate(self):
        sleep(2)
        self.driver.find_element_by_id("s_start_date").click()
        self.driver.find_element_by_xpath("//*[@id='datepickers-container']/div[1]/nav/div[3]").click()
        self.driver.find_element_by_css_selector("#datepickers-container > div.datepicker.-bottom-left-.-from-bottom-.active > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(13)").click()

    def click_Selectstart_time(self):
        sleep(2)
        self.driver.find_element_by_name("start_time").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='s_start_time']/option[8]").click()
        sleep(1)
        self.driver.find_element_by_name("start_time").click()

    def clickenddate(self):
        sleep(2)
        self.driver.find_element_by_id("s_end_date").click()
        self.driver.find_element_by_xpath("//*[@id='datepickers-container']/div[2]/nav/div[3]").click()
        self.driver.find_element_by_css_selector("#datepickers-container > div.datepicker.-bottom-left-.-from-bottom-.active > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(27)").click()

    def click_Select_end_time(self):
        sleep(2)
        self.driver.find_element_by_name("end_time").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='s_end_time']/option[15]").click()
        sleep(1)
        self.driver.find_element_by_name("end_time").click()


    def clickCampaignContinue(self):
        sleep(2)
        self.driver.find_element_by_id(self.continue_campaigns_id).click()


    def setCampaignMessage(self, campaignMessage):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_message_name).clear()
        self.driver.find_element_by_name(self.textbox_message_name).send_keys(campaignMessage)

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='" + CAMPAIGN_ORG_NAME + "']").click()
        sleep(1)
        self.driver.find_element_by_name(self.dropdown_organization_name).click()


    def clickSelectbusinessunit(self):
        sleep(2)
        self.driver.find_element_by_name("business_unit_id").click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='business_unit_id']/option[text()='Automation-Business-unit-update']").click()
        sleep(1)
        self.driver.find_element_by_name("business_unit_id").click()


    def clickCampaignsbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.campaigns_create_btn_class).click()

    def clickCampaignEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_campaign_class).click()

    def click_campaigns_update_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.campaigns_update_btn_class).click()

    def clickRemoveCampaign(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_campaign_link).click()


    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[9]/div/div[3]/div[2]/button").click()

    def clickcampaigncsv(self):
        sleep(2)
        upload_file = self.driver.find_element_by_css_selector('.dz-hidden-input')
        upload_file.send_keys(os.path.abspath("assets/upload_file/campaignTemplateCSV.csv"))
        self.driver.find_element_by_css_selector('.dz-image').is_displayed()


