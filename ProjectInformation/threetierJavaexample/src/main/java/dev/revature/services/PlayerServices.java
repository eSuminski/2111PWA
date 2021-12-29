package dev.revature.services;

import dev.revature.entities.Player;

import java.util.List;

public interface PlayerServices {

    Player getPlayerByIdService(int id);

    List<Player> getAllPlayersService();

    Player createPlayer(Player player);
}
