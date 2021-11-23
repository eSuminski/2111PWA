# REST

## Webservice
At its core, a webservice is a way of facilitating the transfer of information accross the web. There are many ways of handling this, we will be looking at one way: RESTful web services

## REST
Representational State Transfer (REST) web services are a type of web service that transfers a representation of the data you are working with instead of the actual data itself. This kind of web service is not directly used by humans. The format of information transfered in a RESTful web service is transfered in a computer friendly format (think JSON). There 6 constraints a RESTful web service needs to follow in order to be considered a true RESTful web service.
1. Uniform Interface
    - URLs are the standard way of interacting over the web
    - URI to identify the resource, and use the HTTP verb to identify what you are trying to do with the resource
    - example: GET/customer/1
        - the intent of the route should be obvious based upon the wording and the verb associated with the request
2. Client - Server architecture
    - A RESTful web service is not a complete application
        - all it should do is handle the transfer of information
3. Stateless
    - RESTful web services do not keep track of users
4. Cacheable
    - RESTful web services can cache information client side
5. Layered System
    - RESTful web services should be able to call other services
6. Code on Demand (optional)
    - RESTful web services should be able to send back executable code (Think Javascript)
        - this is not a common practice