# Banking Application

## Description

   The Bank app is a RESTful application that simulates banking operations. A customer can create an account, view their account balances, and make withdrawals and deposits. An employee can add new customers to the system and view account balances for customers.
	
## Purpose

   We want to see that you can meet deadlines and that you can code. You are expected to complete the following requirements and give a 5 minute presentation of your project to our QC team.

## Requirements
1. Functionality should reflect the provided user stories.
2. Customer and Bank Account information should be stored in a database.
	- validation is not required in this project, so don't create Employee data
3. A custom stored procedure in the database should be utilized to perform some portion of the application's functionality.
4. Data Access should be performed through the use of Psycopg3 in a data layer consisting of Data Access Objects.
5. All requests to the application should be facilitated through Postman and handled by Flask.
6. All requests to the application and their results should be logged in a central file.
7. Every DAO and Service layer function should have a test validating its functionality 

## User Stories

* As a customer, I can create a new bank account with a starting balance. (create_account)
* As a customer, I can view the balance of a specific account. (get_account_by_id)
* As a customer, I can make a withdrawal or deposit to a specific account. (deposit_into_account_by_id, withdraw_from_account_by_id)
* As a customer, I can transfer money between accounts (transfer_money_between_accounts_by_their_ids)
* As a customer, I can update my personal information (update_customer_by_id)
* As a customer, I can view my personal information (get_customer_by_id)
* As a customer, I can close any of my bank accounts (delete_account_by_id)
* As a customer, I can end my buisness relationship with the bank (delete_customer_by_id)
* As the system, I reject invalid transactions.
	* Ex:
		* A withdrawal that would result in a negative balance.
		* A deposit or withdrawal of negative money.
* As an employee, I can create new customers and add them to the system (create_new_customer)
* As an employee, I can get a list of all the bank's customers (get_all_customers)
* As an employee, I can get a list of all the bank accounts we manage (get_all_accounts)
* As an employee, I can get a list of all of a client's accounts (get_all_customer_accounts_by_id)
