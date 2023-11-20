*** Settings ***
Test Setup  Create User And Input New Command
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallemoi  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle123  kalle123
    Output Should Contain  Username can only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kallek  ka12
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallek  kallekalle
    Output Should Contain  Password can't contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command