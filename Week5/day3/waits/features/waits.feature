Feature: how to use implicit wait
  Scenario: I need to use implicit wait to access the button
    Given I am on the webpage with the hidden button
    When I click the button that says click me
    Then I should see an alert that says good job