from time import sleep
import os

class ArtivaimportClass:
    profile_href_link = "Artiva txt"
    click_select_dropdown_org = "org_id"
    click_select_dropdown_timezone = "timezone"
    click_select_dropdown_start_time = "start_time"
    click_select_dropdown_end_time = "end_time"
    artiva_submit_btn_class = "upload_artiva_txt_file_button"

    def __init__(self, driver):
        self.driver = driver

    def clickartivabtn(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.profile_href_link).click()

    def clickSelectorg(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_org).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_org).click()

    def clickSelecttimezone(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_timezone).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='timezone']/option[2]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_timezone).click()

    def clickstartdatepickertest(self):
        sleep(2)
        self.driver.find_element_by_id("starttime_input").click()
        self.driver.find_element_by_id("starttime_input").clear()
        self.driver.find_element_by_xpath("//*[@id='datepickers-container']/div[1]/nav/div[3]").click()
        self.driver.find_element_by_css_selector("#datepickers-container > div.datepicker.-bottom-left-.-from-bottom-.active > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(18)").click()

    def clickSelectstarttime(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_start_time).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='s_start_time']/option[6]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_start_time).click()


    def clickenddatepickertest(self):
        sleep(2)
        self.driver.find_element_by_id("endstime_input").click()
        self.driver.find_element_by_id("endstime_input").clear()
        self.driver.find_element_by_xpath("//*[@id='datepickers-container']/div[2]/nav/div[3]").click()
        self.driver.find_element_by_css_selector("#datepickers-container > div.datepicker.-bottom-left-.-from-bottom-.active > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(18)").click()

    def clickSelectendtime(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_end_time).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='s_end_time']/option[14]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_end_time).click()

    def clickuploadimage(self):
        sleep(2)
        self.driver.find_element_by_id("artiva_txt_file").send_keys(os.path.abspath("assets/upload_file/NBH_SSM_UF_scsiltrs_Artiva_Text_12212021.txt"))

    def clicksubmitbtn(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='upload_artiva_txt_file_button']").click()