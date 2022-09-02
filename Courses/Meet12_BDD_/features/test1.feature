Feature: Intro to BDD
  as a user
  I want to learn BDD
  so that I can get a better job

  Background: Stable Internet Connection
    Given I have a Digi coonection

  @smoke
  Scenario: test BDD works in Python
    Given I have Behave installed
    When I type Behave on Console
    Then My first test should fail

  @valid
  Scenario: testing valid login
    Given I have a valid username and password
    When I login to website herokup
    Then I am able to connect my account
  @valid
  Scenario: combining more steps
    Given I have Behave installed
    And I have a valid username and password
    When I login to website herokup
    Then My first test should fail