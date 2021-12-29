package dev.revature.controllers;


import com.google.gson.Gson;
import dev.revature.entities.ShowingOffGson;
import io.javalin.http.Handler;

import java.util.ArrayList;
import java.util.List;

public class AppController {

    // I'm using this list to simulate a database
    List<ShowingOffGson> list = new ArrayList<>();

    // this just returns Hello there! when someone goes to the base page
    // Javalin provides a contex object for your Handler lambda, gives you access to the result and status methods
    public Handler hello = ctx ->{
        // result is what you are returning in the HTTP response
        ctx.result("Hello there!");
        // status lets you set a custom status
        ctx.status(200);
    };

    public Handler addObject = ctx ->{
        // Gson objects can access the body of a request for you
        Gson gson = new Gson();
        // to create an object from the request body, use the fromJson method
        // first argument is the ctx.body, second argument is the class you are creating an object of
        ShowingOffGson object = gson.fromJson(ctx.body(), ShowingOffGson.class);
        // once you have created your object you can do what you need with it in your code
        list.add(object);
        // use the result and status methods to craft your http response
        ctx.result("You have added your object to the list");
        ctx.status(201);
    };

    public Handler getObject = ctx -> {
        // path parameters start as strings, so if you need a non-string object you need to parse it from the string
        // pathParam is the method to acquire a value from the url
        int index = Integer.parseInt(ctx.pathParam("index"));
        ShowingOffGson object = list.get(index);
        Gson gson = new Gson();
        // use the toJson method to convert an object to a JSON(it is technically a string, JSONs are basically formatted strings)
        // the gson object makes use of your getter and setter methods to create jsons, so you want to use the JavaBean design pattern for your classes
        String objectJSON = gson.toJson(object);
        // you can use the result method to return the json you created in the response body
        ctx.result(objectJSON);
        ctx.status(200);
    };

}
