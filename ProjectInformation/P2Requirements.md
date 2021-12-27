# Project 2

## Project Overview
You and your team have the freedom to decide what kind of application you wish to build for your Project 2. There are a few base requirements your project must meet:
1. Your application must be able to handle at minimum two different kinds of users (customers and clerks, employees and managers, etc.)
2. Your application must persist data using an AWS Postgres database
3. Your application must be a web service
    - it must be a RESTful web service
    - use HTML/CSS/JavaScript
4. Your application should be robust
    - logging in and out is insufficient: your users must be able to DO things with your application
5. Your backend should be programmed in Java

## User Story/Acceptance Criteria Requirements
Your project should have a minimum of 20 user stories, no user should have less than 5 user stories. Every User Story must have associated Acceptance Criteria written out for it. Both the User Stories and Acceptance Criteria should be stored together in some easy to read format (Excel file, for example) and stored in your project github repository. Also, you need to create wireframes that visually lay out the user interface and the steps the user must take to fulfill the Acceptance Criteria. This should also be stored in your project repository

## Development Requirements
You will be using Behavior Driven Development and Test Driven Development to create your application. Your back end should have a Data Access Layer, Service Layer, and API layer like your previous projects. Every applicable Data Access Layer and Service layer method should have a unit test if possible, integration test if not. Also, your Service layer should make use of Mocking and Stubbing to achieve unit testing.

Your front end should be tested by using Cucumber and Selenium to facilitate End to End testing. Every Acceptance Criteria should have an E2E test validating its completion.

Your UI should be stylized and easy to use: make use of resources like Bootstrap to provide quick styling options for your web pages if you are not comfortable doing it manually

## Team Requirements
Your team should have a daily standup each morning when possible to review your progress and assist each other with blockers. You should also use this time to review how far along with the project you are and assign work accordingly. You should create a Requirements Traceability Matrix to track feature testing progrss and to record who has worked on what feature. 

## Project Order of Operations
1. Create User Stories
    - get user stories approved
2. Create acceptance Criteria
    - get acceptance criteria approved
3. Create wireframes
4. Create your application
    - use TDD to develop the backend
    - test your front end with E2E tests
5. If you have extra time, implement stretch goals