from time import sleep


class ChatagentLoginClass:
    textbox_chatagent_useremail_name = "email"
    textbox_chatagent_password_name = "password"
    button_chatagent_login_xpath = "/html/body/div[1]/div/form/div[3]/input"
    link_logout_linktext = "Logout"
    toastr_login_success_class = "toast-message"

    def __init__(self, driver):
        self.driver = driver

    def setchatagentEmailName(self, email):
        self.driver.find_element_by_name(self.textbox_chatagent_useremail_name).clear()
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chatagent_useremail_name).send_keys(email)

    def setchatagentPassword(self, password):
        self.driver.find_element_by_name(self.textbox_chatagent_password_name).clear()
        sleep(1)
        self.driver.find_element_by_name(self.textbox_chatagent_password_name).send_keys(password)

    def clickchatagentPLogin(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.button_chatagent_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
