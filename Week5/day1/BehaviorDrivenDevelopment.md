# Behavior Driven Development
Behavior Driven Development (BDD) is development from the user's perspective
    - unlike TDD, BDD focuses on what the user is doing
    - BDD takes into account the user experience, expectations, interactions, etc.
    - BDD take into account ALL of your application, not just one or two parts of it
        - User experience
            - what do they see
            - what do they do
            - what are they expecting
            - etc.
        - API
        - Database
        - Buisness Logic
    - Tests for Behavior Driven Development are called End to End (E2E) tests
        - these tests simulate what a user would/could do with your front end
            - you can test logging in
            - you can test filling our forms and submitting information
            - you can test running snippets of code on your website

### End to End Testing
1. User Stories 
    - a good user story will provide three key pieces of information:
        - who is doing the action? 
            - (As a...)
        - what is the action? 
            - (I want...)
        - why are they taking the action? 
            - (So that...)
    - User stories are beneficial for multiple reasons:
        - User stories help you outline your application
        - User stories also provide guardrails for your application
            - does a feature not fit any user stories? Then it is not needed and you don't need to spend time on it
            - this is particularly helpful for avoiding feature creep
2. Write out Acceptance Criteria
    - Acceptance Criteria is written using Gherkin syntax
    - Gherkin is the syntax that is used for creating Acceptance Criteria in End to End tests, so we will also use it here so that we are getting a head-start on our code
    - There are some key words to know:
        - Feature: a high level description of a User story or a group of user stories
        - Scenario: explicit or direct description of a user story
        - Given: This explains where the user is starting the process of fulfilling the user story
        - When: This explains the steps the user takes to complete the user story
        - Then: this explains where the user should end the user story