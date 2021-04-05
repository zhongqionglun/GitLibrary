*** Settings ***
Documentation     Suite description
Library           Selenium2Library

*** Test Cases ***
Test_Case01
    [Tags]    DEBUG
    Open Browser    https://baidu.com    chrome
    Input Text    id=kw    pycharm
    Click Button    id=su
    Sleep    5
    Close Browser

*** Keywords ***
Provided precondition
    Setup system under test
