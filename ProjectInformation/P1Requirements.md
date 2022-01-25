# Project 1

## Expense Reimbursement System
You are tasked with creating an expense reimbursement system for a small company/group. This program will allow employees to create reimbursement requests, and all Managers can view these requests and approve or deny them. When they approve/deny they can optionally leave a message for the employee.

### key features
- Employee
    - An employee can login to see their own reimbursements, past and pending
    - An employee can submit a reimbursement with an amount and a reason
- Manager
    - A Manager can view all reimbursements past and pending
    - A Manager can appove or deny any reimbursement

### Key Notes
- you do NOT have to allow for the creation of employees or managers.
    - You can have these already in the database.
- You do NOT need to implement security for your application. You can assume that a later security team is responsible for making the applicaiton secure.
    - API routes do not need to be protected
    - Passwords do not have to be encrpted
- Web page templates are allowed

### Technical and testing requirements
- TDD practices should be followed
- Backend should be developed in Flask
- Backend should be a RESTful web service
    - You may have to a make a non-REST compliant endpoint for login. This is normal.
- AWS postgres RDS should be used to persist information
- All DAO methods should have at least three tests verifying they work
- All Service methods with logic should have at least three tests verifying they work
- There should be logging in the application
- There should be at minimum a login page, employee homepage, and manager homepage
    - all web pages should have styling applied to them
- All user stories and acceptance criteria must be written out
- Must have E2E tests using gherkin and selenium for all user stories.
    - make sure to include business logic validation in your E2E tests

### User Stories
- Employees
    - as an employee, I should be able to login so I can manage my reimbursements
    - as an employee, I should be able to submit new reimbursement requests so I can get money back from the company
    - as an employee, I should be able to review my reimbursement requests so I can know if they are approved or denied
    - as an employee, I should be able to logout so my information does not remain available on my computer
- Managers
    - as a manager, I should be able to login so I can approve or deny reimbursements
    - as a manager, I should be able to approve reimbursement requests because they are legitamate
    - as a manager, I should be able to deny reimbursement requests because they are illegitamate
    - as a manager, I should be able to leave a comment about my decisions regarding reimbursement requests so employees better understand my decisions
    - as a manager, I should be able to view pending reimbursement requests so I can make decisions about them
    - as a manager, I should be able to view past reimbursement requests so I can check previous decisions
    - as a manager, I should be able to log out so my information does not remain available on my computer
- System
    - as the system, I should reject failed login attempts
    - as the system, I should reject negative values for reimbursement requests
    - as the system, I should reject non-numeric values for reimbursement requests

### Stretch Goals
These are extra features you can add if you complete all the base requirements
- add more tests/make your application more robust
    - add mocking and stubbing to your application (MagicMock)
- Enhance the styling of your web pages
- Add security features to your application
- Add the ability to create and remove employees
- Add the ability to submit receipts alongside reimbursements