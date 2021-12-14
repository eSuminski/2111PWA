Feature: Wikipedia should support multiple languages

  Scenario: as an English speaker I want to view the english page so I can educate myself on a subject that interests me in my own language
    Given The English user is on the wikipedia home page
    When The English user clicks on the english link
    Then The English user should be redirected to the english home page

  Scenario: as an Spanish speaker I want to view the english page so I can educate myself on a subject that interests me in my own language
    Given The Spanish user is on the wikipedia home page
    When The Spanish user clicks on the spanish link
    Then The Spanish user should be redirected to the spanish home page

  Scenario: as an Italian speaker I want to view the english page so I can educate myself on a subject that interests me in my own language
    Given The Italian user is on the wikipedia home page
    When The Italian user clicks on the italian link
    Then The Italian user should be redirected to the italian home page
