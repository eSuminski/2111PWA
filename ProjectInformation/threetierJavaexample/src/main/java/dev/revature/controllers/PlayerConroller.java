package dev.revature.controllers;

import com.google.gson.Gson;
import dev.revature.customexceptions.PlayerNotFound;
import dev.revature.entities.Player;
import dev.revature.services.PlayerServices;
import io.javalin.http.Handler;

import java.util.ArrayList;
import java.util.List;

public class PlayerConroller {
    PlayerServices playerServices;

    public PlayerConroller(PlayerServices playerServices){
        this.playerServices = playerServices;
    }

    public Handler createPlayer = ctx ->{
        Gson gson = new Gson();
        Player newPlayer = gson.fromJson(ctx.body(), Player.class);
        Player createdPlayer = this.playerServices.createPlayer(newPlayer);
        String createdPlayerJson = gson.toJson(createdPlayer);
        ctx.result(createdPlayerJson);
        ctx.status(201);
    };

    public Handler getPlayer = ctx -> {
        int id = Integer.parseInt(ctx.pathParam("id"));
        try{
            Player player = this.playerServices.getPlayerByIdService(id);
            Gson gson = new Gson();
            String playerJson = gson.toJson(player);
            ctx.result(playerJson);
            ctx.status(200);
        } catch (PlayerNotFound e){
            ctx.result(e.getMessage());
            ctx.status(404);
        }
    };

    public Handler getAllPlayers = ctx -> {
        List<Player> players = this.playerServices.getAllPlayersService();
        Gson gson = new Gson();
        String playersJSONs = gson.toJson(players);
        ctx.result(playersJSONs);
        ctx.status(200);
    };
}
