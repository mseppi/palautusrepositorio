*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallemoi
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Register Should Fail With message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kallel
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Credentials
    Register Should Fail With message  Passwords do not match

Login after succesfull registration
    Set Username  kallesss
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kallesss
    Set Password  kalle123
    Submit Credentials Login
    Main Page Should Be Open

Login after failed registration
    Set Username  kalleright
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kallewrong
    Set Password  kalle123
    Submit Credentials Login
    Login Page Should Be Open

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Register Should Fail With message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}



