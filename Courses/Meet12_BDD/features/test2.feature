Feature: Multiple user can login
  as a user
  I want to login on Netflix
  so that I can watch my favourite movie

  @smoke
  Scenario: check login for multiple users
    Given User Popescu is valid
    When  He is entering the password Abcd1234
    Then He is logged into the Netflix account

  Scenario Outline: check login with more inputs
    Given User "<user_name>" is valid
    When He is entering the password "<password_name>"
    Then He is logged into the Netflix account
    Examples:
      | user_name        | password_name |
      | popescu@ion.ro   | strongpass    |
      | george@russel.uk | f14th         |
      | george@russel.uk | f14th         |
      | george@russel.uk | f14th         |
      | george@russel.uk | f14th         |
      | george@russel.uk | f14th         |
      | george@russel.uk | f14th         |
      | george@russel.uk | f14th         |
      | george@russel.uk | f14th         |
      | george@russel.uk | f14th         |