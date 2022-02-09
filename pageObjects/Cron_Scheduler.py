from time import sleep

class CronSchedulerClass:
    cronscheduler_href_link = "Cron Scheduler"
    create_cronscheduler_href_link = "Create Cron Scheduler"
    textbox_cron_name = "cron_name"
    textbox_cron_link_name = "cron_link"
    click_select_dropdown_cron_run = "cron_run"
    textbox_cron_time = "cron_time"
    active_checkbox_name = "active_cron_Link"
    cron_scheduler_create_btn_class = "create_cron_scheduler_btn"
    edit_cron_scheduler_class ="action_btns"
    cron_scheduler_update_btn_class ="update_cron_scheduler_btn"
    remove_cronscheduler_link ="Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickCronScheduler(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.cronscheduler_href_link).click()

    def clickCronSchedulerCreate(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_cronscheduler_href_link).click()

    def setCronName(self, cron_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_cron_name).clear()
        self.driver.find_element_by_name(self.textbox_cron_name).send_keys(cron_name)

    def setCronLink(self, cron_link):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_cron_link_name).clear()
        self.driver.find_element_by_name(self.textbox_cron_link_name).send_keys(cron_link)

    def clickSelectCronRun(self):
        sleep(2)
        self.driver.find_element_by_name(self.click_select_dropdown_cron_run).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='cron_run']/option[2]").click()
        sleep(1)
        self.driver.find_element_by_name(self.click_select_dropdown_cron_run).click()

    def setCronTime(self, cron_time):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_cron_time).clear()
        self.driver.find_element_by_name(self.textbox_cron_time).send_keys(cron_time)

    def clickActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_checkbox_name).click()

    def clickcreatecronschedulerbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.cron_scheduler_create_btn_class).click()


    def clickEditcronschedulerbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_cron_scheduler_class).click()

    def clickupdatecronschedulerbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.cron_scheduler_update_btn_class).click()

    def clickRemovecronschedulerLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_cronscheduler_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[2]/button').click()