## Webservice
Webservices are simply applications that allow for the transfering of information through the internet. Typically this is done by transfering the data via machine-friendly formatted data (python object is transfered as a JSON to a Java app accross the internet). There are many different architectural styles for creating Webservices, but we will focus on creating RESTful web services.
## REST
A Representational State Transfer (REST) service is a type of web service that is not directly used by humans. Instead, its inputs and outputs are in machine friendly format (think JSON, XML, etc) and this data is worked with instead of the Python/Java/Whatever data the human using the REST service is working with (the Python object, Java object, etc.). What this means is that a RESTful webservice does not send the actual object the user is working with: it sends a representation of the object accross the web. 
## REST Constraints
there are 6 constraints a RESTful web service must follow to be considered a true REST webservice
1. Client - Server architecture
    - RESTful web services are not complete applications: they do not handle any client logic.
    - with this architecture, feasibly any client-side tech could interact with your server: the data being sent to the client does not HAVE to be specific to any one particular software
2. Stateless
    - RESTful webservices do not keep track of the client: this is handled clientside
3. Cacheable
    - can cache information from the server clientside for optimization
4. Uniform Interface
    - This is a standard web service convention
        - resrouces handeled by a RESTful web service should be identifiable by a Uniform Resource Identifier (URI). For instance, if you are dealing with customers, their identifier in the path should be "customer"
        - you then use specific verbs with your URIs to determine what will actually happen
            - GET/customer/1 should get the information for customer 1
            - the meaning of the URI should be clear even without a description
        - Hypermedia as the Engine of Application State (HATEOAS) should also be followed
            - basically, instead of sending constant http requests to the server to navigate, clients should be able to use links (think hyperlinks) to navigate
5. Layered System
    - RESTful web services should be able to call other services
    - this is not something the client needs to be aware of
6. (optional) Code on Demand
    - RESTful web services can return executable code (like Javascript) that the client web browser can execute
    - this is not a normal practice, and therefor it is optional

## HTTP
Hyper Text Transfer Protocol (HTTP) is the most common means of communication accross the web. It is a request/response based system that guarantees the requester a response.
### HTTP Request Anatomy:
- HTTP Version
- URL
    - where the request is going
- Verb
    - What type of request is being made
- Headers
    - meta infomation about the request
- Body
    - Any data you are sending with the request
### HTTP Response Anatomy:
- HTTP Version
- Headers
- Body
- Status code (How it was processed)
    - 100
        - informational
    - 200
        - success
    - 300
        - redirect
    - 400
        - requester error
    - 500
        - server error (very bad)

### HTTP Status codes in-depth:
- 100
    - Continue status code (it means everything is fine and the HTTP request should continue)
- 200
    - The general success code
    - 201 is for successfully creating an object/resource
    - 204 is success but there is no information to return to the requester
- 300
    - redirect
        - not common in RESTful services
- 400
    - Client error (data was entered incorrectly, login failed, tried to divide by zero, etc)
    - 401 unauthorized
    - 403 forbidden
    - 404 not found
    - 405 method not permitted for this endpoint
    - 422 Unprocessable
- 500
    - Server error
    - the server is unable to handle the request because something is either not working properly or has not yet been implemented. These are developer mistakes, not client mistakes
    - You really do not want 500 errors
### HTTP Verbs in-depth
- GET
    - Used to retrive infromation
    - GET requests do not have a body
- PUT
    - Use PUT when you are replacing an object or some sort of data
- POST
    - Use POST when creating an object or some kind of data
- DELETE
    - Use DELETE when removing data
- PATCH
    - Use PATCH when you are updating or editing an object or data
## JSON
JavaScript Object Notation (JSON) is one of the most common ways of sending information accross the web. JSONs are basically formatted strings: every programming language has a way of using strings, so it makes sense to use them for sending information accross the web. There are a few rules to follow when using JSONs:
- JSONs should follow JavaScript naming conventions
    - camelCase
- JSONs support three data types
    - string
    - number
    - boolean
        - you can pass this data in a list as well
- JSONs are key:value pair groupings
    - "key1":"string value"
    - "key2": 1
    - "key3": true
- example JSON:
```JSON
{
    "name":"Ted",
    "profession":"Football Coach",
    "yearsExperience":0,
    "overHisHead":true
}
```