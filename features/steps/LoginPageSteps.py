
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig
from behave import given, when, then


baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()


@given(u'Launch the browser')
def step_impl(context):
    driver = webdriver.Chrome()
    mylogger.info("**** Driver Initialized correctly ****")
    driver.get(baseURL)
    context.driver = driver
    mylogger.info("**** Browser launched ****")


@when(u'Enter login credentials')
def step_impl(context):
    mylogger.info("**** Providing User Credentials ****")
    global hpage
    global lpage
    # hpage = HomePage(context.driver)
    lpage = LoginPage(context.driver)
    usr = ReadConfig.getUserName()
    pwd = ReadConfig.getPassword()
    lpage.setusername(usr)
    lpage.setupassword(pwd)
    mylogger.info("**** Credentials provided ****")


@then(u'Click submit')
def step_impl(context):
    lpage.clickOnSignIn()
    mylogger.info("**** Sign_in Button clicked ****")


@then(u'Verify the page title and screenshot')
def step_impl(context):
    actual_title = context.driver.title

    # print("page title 1 ======", context.driver.title)
    # actual_title = "true"
    expected_title = "Home - QA_Microblog"
    if actual_title.strip() == expected_title:
        assert True
        context.driver.save_screenshot(".\\ScreenShots\\" + "LoginPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="qa_microblog login test", attachment_type=AttachmentType.PNG)
        mylogger.info("page title 1 ======>>", context.driver.title)
        mylogger.info("**** Title matched ****")
    else:
        mylogger.info("**** Title NOT matched ****")
        context.driver.save_screenshot(".\\ScreenShots\\" + "LoginPage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="qa_microblog login test",
                      attachment_type=AttachmentType.PNG)
        assert False


@then(u'Close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info("**** Browser closed ****")
