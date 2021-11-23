*** Settings ***
Library     SeleniumLibrary
Documentation  Feature: Test the QA microblog using Behave functionalities
Resource  ../../Pages/LoginPageHelper.robot

*** Variables ***


*** Test Cases ***
Scenario: Verify Home Page
  [Tags]  Smoke
  Given Launch the browser
  Then Verify the page title
#  And Close the browser

Scenario: Verify the login functionality
  [Tags]  Smoke
  Given Launch the browser
  When Enter login credentials
  Then Click submit
  Then Verify the page title and screenshot
#  And Close the browser


#TC1
#    Launch the browser
#    Enter login credentials
#    Click submit
#    Verify the page title and screenshot

*** Keywords ***
Launch the browser
    LoginPageHelper.OpenTheBrowser

Enter login credentials
    LoginPageHelper.EnterUsername
    LoginPageHelper.EnterPassword

Click submit
    LoginPageHelper.ClickOnSubmit

Verify the page title
    LoginPageHelper.VerifyPageTitle

Verify the page title and screenshot
    LoginPageHelper.VerifyPageTitle
    LoginPageHelper.TakeAscreenshot

Close the browser
    LoginPageHelper.CloseBrowser
