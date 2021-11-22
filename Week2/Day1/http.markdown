# HTTP
Hyper Text Transfer Protocol (HTTP) is the most common way of sending information accross the web. HTTP is a request/response format that guarantees the requester a response.

## Request Anatomoy
1. HTTP version: the version of http the request is using
2. URL: the route
3. Body: the content of the request
4. Verb: indicates what kind of request is being made
5. Header: contains meta information

## Response Anatomy
1. HTTP version: the version of http the request is using
2. Header: contains meta information
3. Response Body: content of the response
4. Status Code: indicates how the request was handled

## HTTP Status Codes
- 100 level
    - simply means continue
- 200 level
    - success level
    - 201 is the creation success code
    - 204 is the success but nothing to return code
- 300 level
    - transfer level/ reroute level
- 400 level
    - user/client errors
    - 401 unauthorized
    - 403 forbidden 
    - 404 not found 
    - 422 unprocessable
- 500 level
    - server error
    - these are bad
    - you don't want 500 status code

## HTTP Verbs
There are a few common verbs you should be familiar with
- GET
    - Use gets when you are retrieving information
    - can not have a request body
- PUT
    - Use when you are replacing an object or some data
- PATCH
    - Use when you are updating an object or some data 
- POST
    - Use when you are adding or creating an object or some data
- DELETE
    - Use when you delete an object or some data