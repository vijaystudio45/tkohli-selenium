from time import sleep


class ReportSchedulerClass:
    report_scheduler_href_link = "Reports Scheduler"
    create_report_scheduler_href_link = "Create Report Scheduler"
    click_select_org_name = "org_id"
    click_frequency_dropdown_id = "Frequency"
    click_report_type_dropdown_id = "report_type"
    textbox_report_title_name = "report_title"
    textarea_report_sql_query_name = "sql_query"
    report_scheduler_create_btn_class = "create_report_scheduler_btn"
    edit_report_scheduler_class = "action_btns"
    edit_dropdown_org_name = "org_id"
    click_update_btn_class = "update_reportScheduler_btn"
    remove_report_scheduler_href_link = "Remove"
    confirm_delete_report_scheduler_class = "swal-button"
    textbox_sftp_host = "ftp_host"
    textbox_sftp_username = "ftp_username"
    textbox_sftp_password = "ftp_password"
    textbox_sftp_location = "ftp_location"
    report_history_href_link = "Reports Scheduler History"
    report_history_error_href_link = "Report Error Items"


    def __init__(self, driver):
        self.driver = driver

    def clickReportScheduler(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.report_scheduler_href_link).click()

    def clickCreateReportScheduler(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_report_scheduler_href_link).click()

    def clickSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_org_name).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='org_id']/option[text()='Automation-organization-updated']").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_org_name).click()

    def setFrequencyFromDropdown(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_frequency_dropdown_id).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='Frequency']/option[3]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_frequency_dropdown_id).click()

    def setReportTypeFromDropdown(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_report_type_dropdown_id).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='report_type']/option[3]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_report_type_dropdown_id).click()

    def setReportTitle(self, reportTitle):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_report_title_name).clear()
        self.driver.find_element_by_name(self.textbox_report_title_name).send_keys(reportTitle)

    def setReportSchedulerSQLQuery(self, sqlQuery):
        sleep(1)
        self.driver.find_element_by_name(self.textarea_report_sql_query_name).clear()
        sleep(1)
        self.driver.find_element_by_name(self.textarea_report_sql_query_name).send_keys(sqlQuery)

    def clickCreatebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.report_scheduler_create_btn_class).click()

    def clickEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_report_scheduler_class).click()

    def editDropdownOrg(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_org_name).click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_org_name).click()
        self.driver.find_element_by_xpath("//*[@id='add_report_schedule_form']/div[1]/select[1]/option[7]").click()

    def clickUpdateBtn(self):
        sleep(3)
        self.driver.find_element_by_class_name(self.click_update_btn_class).click()

    def clickRemoveReportScheduler(self):
        sleep(3)
        # self.driver.find_element_by_class_name(self.remove_report_scheduler_class).click()
        self.driver.find_element_by_link_text(self.remove_report_scheduler_href_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath("//button[normalize-space()='Yes, delete it!']").click()


    def clickdropdownSelectOrg(self):
        sleep(2)
        self.driver.find_element_by_id("add_report_org_id").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_report_org_id']/option[19]").click()
        sleep(1)
        self.driver.find_element_by_id("add_report_org_id").click()

    def clickorgdropdownBtn(self):
        sleep(3)
        self.driver.find_element_by_class_name("get_scheduler_By_organization").click()


    def setemail(self, email):
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_report_schedule_form']/div[1]/div/span").clear()
        self.driver.find_element_by_xpath("//*[@id='add_report_schedule_form']/div[1]/div/span").send_keys(email)
        self.driver.find_element_by_xpath("//*[@id='add_report_schedule_form']/div[1]/div/span").click()


    def setReport_sftp_host(self, sftp_host):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sftp_host).clear()
        self.driver.find_element_by_name(self.textbox_sftp_host).send_keys(sftp_host)

    def setReport_sftp_username(self, sftp_username):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sftp_username).clear()
        self.driver.find_element_by_name(self.textbox_sftp_username).send_keys(sftp_username)

    def setReport_sftp_password(self, sftp_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sftp_password).clear()
        self.driver.find_element_by_name(self.textbox_sftp_password).send_keys(sftp_password)

    def setReport_sftp_file_location(self, sftp_location):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sftp_location).clear()
        self.driver.find_element_by_name(self.textbox_sftp_location).send_keys(sftp_location)


    def clickexcicuteBtn(self):
        sleep(3)
        self.driver.find_element_by_class_name("executeReportSchedulerBtn").click()


    def clickreporthistorybtn(self):
        self.driver.find_element_by_link_text(self.report_history_href_link).click()


    def clickreporthistoryerrorbtn(self):
        self.driver.find_element_by_link_text(self.report_history_error_href_link).click()

