*** Settings ***
Library           Selenium2Library
Library           ../send-sms.py
Library           ../../Android/third.py

*** Test Cases ***
test-ride
    Selenium2Library.Open Browser    192.168.3.5    ie
    Input Text    id=loginname    admin
    input text    id=loginpass    admin
    Click Button    id=login_button
    sleep    10
    Selenium2Library.Close Browser

DWG-Test01-SIPP-callDWG
    [Tags]    skip
    Ssh Exec Command    sipp/sipp -i 192.168.3.3 -p 5060 -sf /root/sipp/uac.xml -inf /root/sipp/call.csv 192.168.3.5:5060 \ -t -u -m 1
    turnonscreen
    Waite Accept Call
    sleep    30
    Turnoffscreen
