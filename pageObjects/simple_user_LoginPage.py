from time import sleep


class SimpleuserLoginClass:
    textbox_simple_useremail_name = "email"
    textbox_simple_user_password_name = "password"
    button_simple_user_login_xpath = "/html/body/div[1]/div/form/div[3]/input"
    link_simple_user_logout_linktext = "Logout"
    toastr_login_success_class = "toast-message"

    def __init__(self, driver):
        self.driver = driver

    def setsimpleuserEmailName(self, email):
        self.driver.find_element_by_name(self.textbox_simple_useremail_name).clear()
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_useremail_name).send_keys(email)

    def setsimpleuserPassword(self, password):
        self.driver.find_element_by_name(self.textbox_simple_user_password_name).clear()
        sleep(1)
        self.driver.find_element_by_name(self.textbox_simple_user_password_name).send_keys(password)

    def clicksimpleuserLogin(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.button_simple_user_login_xpath).click()

    def clicksimpleuserLogout(self):
        self.driver.find_element_by_link_text(self.link_simple_user_logout_linktext).click()
