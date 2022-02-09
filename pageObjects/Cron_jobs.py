from time import sleep

class CronJobsClass:
    cron_href_link = "Cron"

    def __init__(self, driver):
        self.driver = driver

    def clickCronjobs(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.cron_href_link).click()

    def clickCronjobs_Longcodes(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[1]/td[3]/a").click()

    def clickCronjobs_unclaimmed_message_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[2]/td[3]/a").click()

    def clickCronjobs_message_merge_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[3]/td[3]/a").click()

    def clickCronjobs_campaign_report_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[4]/td[3]/a").click()

    def clickCronjobs_count_update_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[5]/td[3]/a").click()

    def clickCronjobs_Reports_Scheduler_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[6]/td[3]/a").click()

    def clickCronjobs_Sender_Aggregates_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[7]/td[3]/a").click()

    def clickCronjobs_Reports_Schedule_Message_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[8]/td[3]/a").click()

    def clickCronjobs_Reports_Schedule_response_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[9]/td[3]/a").click()

    def clickCronjobs_Get_Response_Service_Email_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[10]/td[3]/a").click()

    def clickCronjobs_Get_Message_Archive_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[11]/td[3]/a").click()

    def clickCronjobs_Twilio_API_Poll_Cron_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[12]/td[3]/a").click()

    def clickCronjobs_Twilio_Bulk_Export_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[13]/td[3]/a").click()

    def clickCronjobs_Campaign_Complete_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[14]/td[3]/a").click()

    def clickCronjobs_Bulk_Export_Review_Responses_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[15]/td[3]/a").click()

    def clickCronjobs_Bulk_Export_Review_Messages_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[16]/td[3]/a").click()

    def clickCronjobs_Carrier_Lookup_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[17]/td[3]/a").click()

    def clickCronjobs_tcpa_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[18]/td[3]/a").click()

    def clickCronjobs_Multiple_Cron_Data_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[19]/td[3]/a").click()

    def clickCronjobs_Insert_Redis_Data_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[20]/td[3]/a").click()

    def clickCronjobs_Update_messages_to_Redis_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[21]/td[3]/a").click()

    def clickCronjobs_Update_Messages_and_callback_Status(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[22]/td[3]/a").click()

    def clickCronjobs_Remove_Expired_Messages_from_Redis(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[23]/td[3]/a").click()

    def clickCronjobs_Fix_Missing_Success_Columns_cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[24]/td[3]/a").click()

    def clickCronjobs_Receiving_Cron(self):
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='tableData_message']/tbody/tr[25]/td[3]/a").click()