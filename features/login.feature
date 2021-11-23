Feature: Test the QA microblog using Behave functionalities
  Scenario: Verify Home Page
    Given Launch the browser
    Then Verify the page title
    And Close the browser

  Scenario: Verify the login functionality
    Given Launch the browser
    When Enter login credentials
    Then Click submit
    Then Verify the page title and screenshot
    And Close the browser