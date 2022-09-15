Feature: Heroku form_authentication tests

  Background:
    Given home_page: I am on the https://the-internet.herokuapp.com/ page

    Scenario: The form_authentication with the correct username and password
      When home_page: I click on the Form Authentication link
      When login_page: I fill tomsmith in the username field
      When login_page: I fill SuperSecretPassword! in the password field
      When login_page: I click on the Login button
      When secure_page: I see the login succes message
      When secure_page: I click on the Logout button
      Then secure_page: I verify that I am on the login_page