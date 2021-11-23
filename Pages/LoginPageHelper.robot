*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${baseURL}     https://qa-microblog.herokuapp.com/auth/login?next=%2F
${username}     id:username
${password}     id:password
${sign_in}     id:submit

*** Keywords ***
OpenTheBrowser
    Open Browser    ${baseURL}    Chrome
    maximize browser window

EnterUsername
    input text    ${username}    levis

EnterPassword
    input text    ${password}    alten1

ClickOnSubmit
    click element    ${sign_in}

VerifyPageTitle
    title should be    Home - QA_Microblog

TakeAscreenshot
    capture page screenshot    login_page_screenshot.png

CloseBrowser
    close browser

