from time import sleep

class SignupClass:
    textbox_signup_first_name = "f_name"
    textbox_signup_last_name = "l_name"
    textbox_signup_email = "email"
    textbox_signup_password = "password"
    textbox_signup_confirm_password = "c_password"
    create_signup_class = "registerWebsiteUserBtn"

    def __init__(self, driver):
        self.driver = driver

    def setSignupFirstName(self, Signup_first_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_signup_first_name).clear()
        self.driver.find_element_by_name(self.textbox_signup_first_name).send_keys(Signup_first_name)

    def setSignupLastName(self, Signup_last_name):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_signup_last_name).clear()
        self.driver.find_element_by_name(self.textbox_signup_last_name).send_keys(Signup_last_name)

    def setSignupemail(self, Signup_email):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_signup_email).clear()
        self.driver.find_element_by_name(self.textbox_signup_email).send_keys(Signup_email)

    def setSignuppassword(self, Signup_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_signup_password).clear()
        self.driver.find_element_by_name(self.textbox_signup_password).send_keys(Signup_password)

    def setSignupconfirmpassword(self, Signup_confirm_password):
        sleep(1)
        self.driver.find_element_by_name(self.textbox_signup_confirm_password).clear()
        self.driver.find_element_by_name(self.textbox_signup_confirm_password).send_keys(Signup_confirm_password)

    def clickCreateSignupBtn(self):
        sleep(2)
        self.driver.find_element_by_class_name(self.create_signup_class).click()