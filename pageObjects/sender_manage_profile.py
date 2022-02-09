from time import sleep
import os
class SenderProfileClass:
    sender_profile_href_link = "Manage Profile"
    textbox_sender_Profile_first_name = "f_name"
    textbox_sender_Profile_last_name = "l_name"
    sender_Profile_phone_number = "phone_number"
    click_select_dropdown_sender_profile_state = "state_code"
    textbox_sender_Profile_Address_Line1 = "address_line_1"
    textbox_sender_Profile_Address_Line2 = "address_line_2"
    textbox_sender_Profile_city = "city"
    textbox_sender_Profile_zipcode = "zip"
    textbox_sender_Profile_security_number = "social"
    textbox_sender_Profile_paypal_Email = "paypal_email"
    textbox_sender_current_password = "current_password"
    textbox_sender_new_password = "new_pass"
    textbox_sender_confirm_password = "confirm_pass"
    sender_active_checkbox_name = "check"
    update_sender_profile_btn_class = "updateUserProfileBtn"

    def __init__(self, driver):
        self.driver = driver

    def clicksenderProfile(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sender_profile_href_link).click()

    def setsenderProfileFirstName(self, sender_Profile_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_Profile_first_name).clear()
        self.driver.find_element_by_name(self.textbox_sender_Profile_first_name).send_keys(sender_Profile_first_name)

    def setsenderProfileLastName(self, sender_Profile_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_Profile_last_name).clear()
        self.driver.find_element_by_name(self.textbox_sender_Profile_last_name).send_keys(sender_Profile_last_name)

    def setsenderProfilePhoneNumber(self, sender_Profile_phone_number):
        sleep(1)
        self.driver.find_element_by_name(self.sender_Profile_phone_number).clear()
        self.driver.find_element_by_name(self.sender_Profile_phone_number).send_keys(sender_Profile_phone_number)

    def clicksenderprofiledate(self):
        sleep(2)
        self.driver.find_element_by_id("date_content").clear()
        self.driver.find_element_by_id("date_content").clear()
        self.driver.find_element_by_css_selector("#datepickers-container > div > div > div > div.datepicker--cells.datepicker--cells-days > div:nth-child(8)").click()

    def clickSelectsenderProfileState(self):
        sleep(2)
        self.driver.find_element_by_id(self.click_select_dropdown_sender_profile_state).click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id='state_code']/option[5]").click()
        sleep(1)
        self.driver.find_element_by_id(self.click_select_dropdown_sender_profile_state).click()


    def setsenderProfileAddressLine1(self, sender_Profile_Address_Line1):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_Profile_Address_Line1).clear()
        self.driver.find_element_by_name(self.textbox_sender_Profile_Address_Line1).send_keys(sender_Profile_Address_Line1)


    def setsenderProfileAddressLine2(self, sender_Profile_Address_Line2):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_Profile_Address_Line2).clear()
        self.driver.find_element_by_name(self.textbox_sender_Profile_Address_Line2).send_keys(sender_Profile_Address_Line2)

    def setsenderProfilecity(self, sender_Profile_city):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_Profile_city).clear()
        self.driver.find_element_by_name(self.textbox_sender_Profile_city).send_keys(sender_Profile_city)

    def setsenderProfilezipcode(self, sender_Profile_zipcode):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_Profile_zipcode).clear()
        self.driver.find_element_by_name(self.textbox_sender_Profile_zipcode).send_keys(sender_Profile_zipcode)

    def setsenderProfilesecurityNumber(self, sender_Profile_security_number):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_Profile_security_number).clear()
        self.driver.find_element_by_name(self.textbox_sender_Profile_security_number).send_keys(sender_Profile_security_number)

    def setsenderProfile_paypal_Email(self, sender_Profile_paypal_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_Profile_paypal_Email).clear()
        self.driver.find_element_by_name(self.textbox_sender_Profile_paypal_Email).send_keys(sender_Profile_paypal_email)


    def clicksenderuploadimage(self):
        sleep(2)
        self.driver.find_element_by_name("photo_url").send_keys(os.path.abspath("assets/upload_file/Bannerv2.png"))

    def setsenderProfilecurrentPassword(self, sender_Profile_current_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_current_password).clear()
        self.driver.find_element_by_name(self.textbox_sender_current_password).send_keys(sender_Profile_current_password)

    def setsenderProfilenewPassword(self, sender_Profile_new_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_new_password).clear()
        self.driver.find_element_by_name(self.textbox_sender_new_password).send_keys(sender_Profile_new_password)


    def setsenderProfileconfirmPassword(self, sender_Profile_confirm_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_confirm_password).clear()
        self.driver.find_element_by_name(self.textbox_sender_confirm_password).send_keys(sender_Profile_confirm_password)

    def clicksenderActiveCheckbox(self):
        self.driver.find_element_by_name(self.sender_active_checkbox_name).click()

    def clickupdate_sender_profilebtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.update_sender_profile_btn_class).click()
