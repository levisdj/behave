from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class HomePage:
    home_href_link = "Home"
    explore_href_link = "Explore"
    profile_href_link = "Profile"
    logout_href_link = "Logout"
    textbox_post_id = "post"
    btn_submit_post_id = "submit"

    def __init__(self, driver):
        self.driver = driver


