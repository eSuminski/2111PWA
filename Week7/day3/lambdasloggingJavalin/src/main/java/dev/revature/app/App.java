package dev.revature.app;

import dev.revature.controllers.AppController;
import io.javalin.Javalin;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class App {
    static Logger logger = LoggerFactory.getLogger(App.class);
    /*
    logging levels (most to least inclusive):
    all = logs everything
    debug = fine-grain information
    info = general information about your application
    warn = use when something might break
    error = use when something goes wrong, but the app can still run
    fatal = a REAL bad error, most likely will crash your application
    off = no logging
     */

    public static void main(String[] args) {

        // to manually log use your logger and the method associated with the level you want to log to
        logger.info("creating Javalin object");
        // notice I am using a lambda in my create method to configure my Javalin object
        Javalin app = Javalin.create(config ->{
            // this helps you avoid CORS errors
            config.enableCorsForAllOrigins();
            // this provides detailed logging of your HTTP requests and responses
            config.enableDevLogging();
        });
        logger.info("Javalin object created");

        // this controller handles the requests and responses: our Javalin object handles obtaining the request and sending the response
        AppController appController = new AppController();

        // app.verb("url/{pathparam}, controllerObject.methodReference);
        app.get("/",appController.hello);

        app.get("object/{index}", appController.getObject);

        app.post("/object", appController.addObject);


        logger.info("Starting Javalin app");
        // make sure to actually start your server
        app.start();
    }
}
