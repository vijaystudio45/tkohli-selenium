from time import sleep

class PermissionClass:
    click_edit_permission_class = "glyphiconedit"
    click_permission_href_link = "Permission"
    click_onboarding_dropdown_id = "onboarding"
    click_org_dropdown_id = "org_id"
    click_user_role_id = "user_role"
    click_active_chk_id = "Showactiveuser"
    click_update_btn_class = "edit-user-permission"

    click_change_password_class = "change_password"
    textbox_new_password_id = "new_pass"
    textbox_conf_password_id = "confirm_pass"
    click_update_pass_btn_class = "change-user-password"
    click_select_dropdown_org = "add_org_id"
    click_select_dropdown_roles = "add_user_role"
    permission_href_link = "Permission"

    def __init__(self, driver):
        self.driver = driver

    def clickpermisionbtn(self):
        self.driver.find_element_by_link_text(self.permission_href_link).click()

    def clickEditPermission(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_edit_permission_class).click()

    def clickfilterorgbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name("Select_organization").click()

    def clickSelectorg1(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_org).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_org_id']/option[6]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_select_dropdown_org).click()


    def clickSelectorg2(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_org).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_org_id']/option[18]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_select_dropdown_org).click()

    def clickfilterrolebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name("Select_Role").click()

    def clickSelectrole(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_roles).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='add_user_role']/option[3]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_select_dropdown_roles).click()

    def clickOnboarding(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_onboarding_dropdown_id).click()
        sleep(1)
        self.driver.find_element_by_id(self.click_onboarding_dropdown_id).click()
        self.driver.find_element_by_xpath("//select[@name='onboarding']/option[text()='Onboarding']").click()

    def clickselectOrg_permission(self):
        sleep(2)
        self.driver.find_element_by_id('org_id').click()
        sleep(1)
        # self.driver.find_element_by_xpath("//select[@name='Organization']/option[text()='Message Org']").click()
        self.driver.find_element_by_xpath("//select[@id='org_id']/option[text()='Automation-organization-updated']").click()
        self.driver.find_element_by_id("org_id").click()

    def clickRole(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_user_role_id).click()
        sleep(1)
        self.driver.find_element_by_id(self.click_user_role_id).click()
        # self.driver.find_element_by_xpath("//select[@name='user_role']/option[text()='Org Admin']").click()
        self.driver.find_element_by_xpath("//*[@id='user_role']/option[2]").click()

    def clickActiveChk(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_active_chk_id).click()

    def clickUpdateBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_update_btn_class).click()

    def clickChangePassBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_change_password_class).click()

    def setNewPassword(self, newPassword):
        sleep(1)
        self.driver.find_element_by_id(self.textbox_new_password_id).clear()
        self.driver.find_element_by_id(self.textbox_new_password_id).send_keys(newPassword)

    def setConfPassword(self, confPassword):
        sleep(1)
        self.driver.find_element_by_id(self.textbox_conf_password_id).clear()
        self.driver.find_element_by_id(self.textbox_conf_password_id).send_keys(confPassword)

    def clickUpdatePassBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_update_pass_btn_class).click()

