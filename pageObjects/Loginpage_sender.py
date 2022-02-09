from time import sleep


class LoginsenderClass:
    textbox_sender_useremail_name = "email"
    textbox_sender_password_name = "password"
    button_sender_login_xpath = "/html/body/div[1]/div/form/div[3]/input"
    sender_link_logout_linktext = "log_out_btn"
    toastr_login_success_class = "toast-message"
    sender_home_href_link = "Home"


    def __init__(self, driver):
        self.driver = driver

    def setsenderEmailName(self, email):
        self.driver.find_element_by_name(self.textbox_sender_useremail_name).clear()
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_useremail_name).send_keys(email)


    def setsenderPasswordName(self, password):
        self.driver.find_element_by_name(self.textbox_sender_password_name).clear()
        sleep(1)
        self.driver.find_element_by_name(self.textbox_sender_password_name).send_keys(password)

    def clicksenderLogin(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.button_sender_login_xpath).click()

    def clicksenderLogout(self):
        self.driver.find_element_by_class_name(self.sender_link_logout_linktext).click()

    def clicksenderDashboard(self):
        sleep(2)
        self.driver.find_element_by_link_text(self.sender_home_href_link).click()