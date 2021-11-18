from flask import Flask, request, jsonify

"""
to create a flask object you create a variable that holds its information. For a basic Flask object
you only need to pass in the argument __name__. This tells the object to look in the module it was
created in to find all the code it needs to work
"""
app: Flask = Flask(__name__)
count = 0
info = [0]


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def convert_to_dictionary(self):
        return {
            "name": self.name,
            "age": self.age
        }

person = Person("Timmy", 2837829324)


@app.get("/")
def landing_page():
    return "This is the landing page"


@app.get("/count")
def check_application_visits():
    global count
    count += 1
    return "This page has been visited {} times".format(count)


@app.get("/info/<index_position>")
def get_information_from_list(index_position: int):
    global info
    return_value = info[int(index_position)]
    return str(return_value)


@app.get("/info")
def get_all_information():
    global info
    # we are eventually going to convert this dictionary into a json to return to the requester
    return_value = {}
    # we need a unique key to identify each item inside our info list
    key = 0
    for data in info:
        return_value.setdefault(key, data)
        key += 1
    return jsonify(return_value)




"""
JSON (Javascript Object Notation) is the most common data format for sending information accross the internet. It is
basically a formatted string: this is because just about every programming language has a way of working with strings
so it makes sense to use them to transfer information. JSONs can store strings, numbers, and booleans. JSONS make an
excellent vehicle for not only sending information to your application but also for sending information back to the user.
The jsonify method can handle this for you: it takes a dictionary and converts it into a json before sending it back to
the requester. This can be extremely useful when trying to send objects back to the requester.
"""


@app.post("/info")
def add_data_to_info_list():
    # the get_json method converts a json into a python dictionary
    data = request.get_json()
    global info
    info.append(data["data"])
    return "data was added successfully"

"""
We have already used post to indicate that it is a route that is expecting to add something into our application.
So, if we want to update instead of adding, we should use a new verb. In this case we will use PATCH
"""

@app.patch("/info/<index_position>")
# we are annotating the index position as a string because that is how it will be received from the request
def update_info_list(index_position: str):
    global info
    body = request.get_json()
    info[int(index_position)] = body["data"]
    return "Info list was updated"

"""
the DELETE verb has an obvious usage: it means our route is intended to remove some information from our application
"""

@app.delete("/info/<index_position>")
def delete_info_from_info_list(index_position: str):
    global info
    deleted_value = info.pop(int(index_position))
    return f"{deleted_value} was removed from the info list"


"""
if we wanted to, we could combine the post and get info routes into one function that can handle them both. if we
do this, we instead will use the @app.route instead of get or post. Inside the @app.route we would add a second
argument called method, in which we declare the kinds of requests the function will handle
"""

# commenting this out so it does not potentially conflict with our earlier code
# @app.route("/info", methods=["GET", "POST"])
# def info_function_for_get_and_post_requests():
#     if request.method == "GET":
#         global info
#         # we are eventually going to convert this dictionary into a json to return to the requester
#         return_value = {}
#         # we need a unique key to identify each item inside our info list
#         key = 0
#         for data in info:
#             return_value.setdefault(key, data)
#             key += 1
#         return jsonify(return_value)
#     elif request.method == "POST":
#         # the get_json method converts a json into a python dictionary
#         data = request.get_json()
#         info
#         info.append(data["data"])
#         return "data was added successfully"

# let's get Timmy, the ancient of days, information
@app.get("/timmy")
def get_timmy():
    global person
    person_as_dictionary = person.convert_to_dictionary()
    person_as_json = jsonify(person_as_dictionary)
    return person_as_json
    # this line of code below does the same thing
    #return jsonify(person.convert_to_dictionary())


app.run()
"""
with the functions above you are actually defining routes that potentially anyone on the web can use to access
your web application. All urls have a basic structure to them:

http(s):// this is the first part of the url: it specifies you are making a Hyper Text Transfer Protocal request. 
http(s) requests are a request/response system that guarantee the requester a response, even if that response is to
only say that everything has gone wrong.

127.0.0.1 this is the domain name. When you get something like 127.0.0.1 you know you are working on a local host.
However, this does not have to be the case: you could use a unique domain name, like google.com, amazon.com, 
netflix.com, etc.

5000 this is the web port we are using

/count this is the path to the file. This will determine where in the web application we are using our request will
be sent to, and therfor, what kind of response we are going to get

parameters are next, they help determine what specific information you need from your web application

query parameters are next, they help filter information you receive from your request

anchors are also part of http(s) requests, but we will not be using them

example url using http:
http://www.exampleDomainName.com:port#/path/to/file/and/params/?queryParams=value#anchor
"""

"""
in postman you can determine the VERB that your route is using: this is actually part of your http request, like the url
above. A VERB is mostly an indicator of what the request wants to achieve, and they should be mostly obvious. Apart
from indicating what you are trying to do with your route, and in the case of a GET request indicating the request
has no body, these verbs don't really do anything else for you.
"""
