package dev.revature.interactwithdatabase;

import dev.revature.entities.Player;

import java.util.List;

public interface PlayerDAO {
    Player getPlayerById(int id);

    // I am returning an interface (not really, will return an actual class) because this gives me flexibility in my
    // implementation of the method
    List<Player> getAllPlayers();
}
