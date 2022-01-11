Feature: I should be able to use Scenario Outlines
  Scenario Outline: I should be able to make searches using the outline
    Given The user is on the wikipedia home page
    When  The user enters "<value>" into the search bar
    When  The user clicks the search button
    Then  The user should be redirected to the "<title>" page

    Examples:
    |value|title|
    |puppy|Puppy - Wikipedia|
    |apple|Apple - Wikipedia|