Feature: Wikipedia should support searching for individual articles

  Scenario Outline: As a user I want to search the wikipedia website so that I can read about a specific subject I am interested in
    Given the user is on the homepage
    When the user inputs <value> into the search bar
    When the user clicks the search button
    Then the user should be redirected to a webpage with the title <title>

    Examples:
      | value  | title               |
      | apple  | Apple - Wikipedia   |
      | puppy  | Puppy - Wikipedia   |
      | pacman | Pac-Man - Wikipedia |