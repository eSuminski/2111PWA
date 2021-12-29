package dev.revature.app;

import dev.revature.controllers.PlayerConroller;
import dev.revature.daos.player.PlayerDAO;
import dev.revature.daos.player.PlayerDAOImp;
import dev.revature.services.PlayerServices;
import dev.revature.services.PlayerServicesImp;
import io.javalin.Javalin;

public class App {
    public static void main(String[] args) {
        Javalin app = Javalin.create(config -> {
            config.enableDevLogging();
            config.enableCorsForAllOrigins();
        });

        PlayerDAO playerDAO = new PlayerDAOImp();
        PlayerServices playerServices = new PlayerServicesImp(playerDAO);
        PlayerConroller playerController = new PlayerConroller(playerServices);


        app.post("/player", playerController.createPlayer);

        app.get("/player/{id}", playerController.getPlayer);

        app.get("/player", playerController.getAllPlayers);

        app.start();
    }
}
