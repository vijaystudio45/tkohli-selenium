from time import sleep

class OrganizationsClass:
    organizations_href_link = "Manage Organizations"
    create_organization_href_link = "Create Organization"
    textbox_organization_name = "org_name"
    textbox_organization_website = "org_website"
    textbox_phone_number = "org_phone_number"
    textbox_first_name = "org_f_name"
    textbox_last_name = "org_l_name"
    textbox_org_email = "org_email"
    textbox_org_contact_phone_number = "org_contact_phone_number"
    textbox_org_response_service_email = "response_service_email"
    organization_dropdown_type_dropdown_id = "timezone"
    click_qc_btn_link = "add_representative_new_div"
    textbox_org_qc_phone_no = "phone_number[1]"
    textbox_sftp_location_host = "sftp_location"
    textbox_sftp_username = "sftp_username"
    org_sftp_password = "sftp_password"
    org_sftp_File_Location = "file_location"
    org_import_root_public = "import_root_public"
    org_import_root_private = "import_root_private"
    message_webhook_url = "message_webhook"
    message_webhook_key = "message_webhook_key"
    response_webhook_url = "response_webhook"
    response_webhook_key = "response_webhook_key"
    click_webhook_url = "click_webhook"
    click_webhook_key = "click_webhook_key"
    org_telnyx_key = "telnyx_api_key"
    active_checkbox_name = "active_org"
    qc_checkbox_name = "active_qc_required"
    org_create_btn_class = "create_org_btn"
    edit_org_link_class = "action_btns"
    org_update_btn_class = "update_org_btn"
    remove_org_link = "Remove"

    def __init__(self, driver):
        self.driver = driver

    def clickOrganizations(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.organizations_href_link).click()

    def clickCreateOrganizations(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.create_organization_href_link).click()

    def setorganizationName(self, org_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_organization_name).clear()
        self.driver.find_element_by_name(self.textbox_organization_name).send_keys(org_name)

    def setorganizationWebsite(self, org_website):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_organization_website).clear()
        self.driver.find_element_by_name(self.textbox_organization_website).send_keys(org_website)

    def setorganizationPhonenumber(self, org_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_phone_number).send_keys(org_phone_number)

    def setorganizationFirstName(self, org_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_first_name).clear()
        self.driver.find_element_by_name(self.textbox_first_name).send_keys(org_first_name)

    def setorganizationLastName(self, org_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_last_name).clear()
        self.driver.find_element_by_name(self.textbox_last_name).send_keys(org_first_name)

    def setorganizationEmail(self, org_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_org_email).clear()
        self.driver.find_element_by_name(self.textbox_org_email).send_keys(org_email)

    def setorganizationContactPhoneNo(self, org_contact_phone_no):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_org_contact_phone_number).clear()
        self.driver.find_element_by_name(self.textbox_org_contact_phone_number).send_keys(org_contact_phone_no)

    def setorganizationResponseServiceEmail(self, org_service_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_org_response_service_email).clear()
        self.driver.find_element_by_name(self.textbox_org_response_service_email).send_keys(org_service_email)

    def setFrom_Organization_timezone_Dropdown(self):
        sleep(2)
        self.driver.find_element_by_id(self.organization_dropdown_type_dropdown_id).click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@name='default_timezone']/option[text()='MST']").click()
        sleep(1)
        self.driver.find_element_by_id(self.organization_dropdown_type_dropdown_id).click()

    def click_qc_btn_class(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.click_qc_btn_link).click()

    def setorganizationqc_Phoneno(self, org_qc_phoneno):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_org_qc_phone_no).clear()
        self.driver.find_element_by_name(self.textbox_org_qc_phone_no).send_keys(org_qc_phoneno)

    def setorganization_sftp_host(self, org_sftp_host):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sftp_location_host).clear()
        self.driver.find_element_by_name(self.textbox_sftp_location_host).send_keys(org_sftp_host)

    def setorganization_sftp_username(self, org_sftp_username):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sftp_username).clear()
        self.driver.find_element_by_name(self.textbox_sftp_username).send_keys(org_sftp_username)

    def setorganization_sftp_Password(self, org_sftp_password):
        sleep(1)
        self.driver.find_element_by_name(self.org_sftp_password).clear()
        self.driver.find_element_by_name(self.org_sftp_password).send_keys(org_sftp_password)

    def setorganization_sftp_FileLocation(self, org_sftp_File_Location):
        sleep(1)
        self.driver.find_element_by_name(self.org_sftp_File_Location).clear()
        self.driver.find_element_by_name(self.org_sftp_File_Location).send_keys(org_sftp_File_Location)

    def setorganization_import_root_public(self, import_root_public):
        sleep(1)
        self.driver.find_element_by_name(self.org_import_root_public).clear()
        self.driver.find_element_by_name(self.org_import_root_public).send_keys(import_root_public)

    def setorganization_import_root_private(self, import_root_private):
        sleep(1)
        self.driver.find_element_by_name(self.org_import_root_private).clear()
        self.driver.find_element_by_name(self.org_import_root_private).send_keys(import_root_private)

    def setorganization_message_webhook_url(self, message_webhook_url):
        sleep(1)
        self.driver.find_element_by_name(self.message_webhook_url).clear()
        self.driver.find_element_by_name(self.message_webhook_url).send_keys(message_webhook_url)

    def setorganization_message_webhook_key(self, message_webhook_key):
        sleep(1)
        self.driver.find_element_by_name(self.message_webhook_key).clear()
        self.driver.find_element_by_name(self.message_webhook_key).send_keys(message_webhook_key)

    def setorganization_response_webhook_url(self, response_webhook_url):
        sleep(1)
        self.driver.find_element_by_name(self.response_webhook_url).clear()
        self.driver.find_element_by_name(self.response_webhook_url).send_keys(response_webhook_url)

    def setorganization_response_webhook_key(self, response_webhook_key):
        sleep(1)
        self.driver.find_element_by_name(self.response_webhook_key).clear()
        self.driver.find_element_by_name(self.response_webhook_key).send_keys(response_webhook_key)

    def setorganization_click_webhook_Url(self, click_webhook_url):
        sleep(1)
        self.driver.find_element_by_name(self.click_webhook_url).clear()
        self.driver.find_element_by_name(self.click_webhook_url).send_keys(click_webhook_url)

    def setorganization_click_webhook_key(self, click_webhook_key):
        sleep(1)
        self.driver.find_element_by_name(self.click_webhook_key).clear()
        self.driver.find_element_by_name(self.click_webhook_key).send_keys(click_webhook_key)

    def setorganization_telnyx_key(self, org_telnyx_key):
        sleep(1)
        self.driver.find_element_by_name(self.org_telnyx_key).clear()
        self.driver.find_element_by_name(self.org_telnyx_key).send_keys(org_telnyx_key)

    def clickActiveCheckbox(self):
        self.driver.find_element_by_name(self.active_checkbox_name).click()

    def clickQCCheckbox(self):
        self.driver.find_element_by_name(self.qc_checkbox_name).click()

    def clickcreateorgbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.org_create_btn_class).click()

    def clickOrgEditBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.edit_org_link_class).click()

    def clickUpdateorgbtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.org_update_btn_class).click()

    def clickRemoveOrgLink(self):
        sleep(3)
        self.driver.find_element_by_link_text(self.remove_org_link).click()

    def clickConfirmDelete(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div[3]/div[2]/button').click()