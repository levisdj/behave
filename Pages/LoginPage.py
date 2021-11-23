

class LoginPage:
    input_text_username_id = "username"
    input_text_password_id = "password"
    sign_in_btn_id = "submit"
    click_to_register_href_link = "Click to Register!"
    checkbox_remember_me_xpath = "/html/body/div/div/div/form/div[3]/label"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.input_text_username_id).send_keys(username)

    def setupassword(self, password):
        self.driver.find_element_by_id(self.input_text_password_id).send_keys(password)

    def clickOnSignIn(self):
        self.driver.find_element_by_id(self.sign_in_btn_id).click()
