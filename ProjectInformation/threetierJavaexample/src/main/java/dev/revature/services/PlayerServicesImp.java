package dev.revature.services;

import dev.revature.customexceptions.PlayerNotFound;
import dev.revature.daos.player.PlayerDAO;
import dev.revature.entities.Player;

import java.util.List;

public class PlayerServicesImp implements PlayerServices{

    PlayerDAO playerDAO;

    public PlayerServicesImp (PlayerDAO playerDAO){
        this.playerDAO = playerDAO;
    }

    @Override
    public Player getPlayerByIdService(int id) {
        try{
            Player player = this.playerDAO.getPlayerById(id);
            return player;
        } catch (PlayerNotFound e){
            throw new PlayerNotFound("Player not found");
        }
    }

    @Override
    public List<Player> getAllPlayersService() {
        return this.playerDAO.getAllPlayers();
    }

    @Override
    public Player createPlayer(Player player) {
        return this.playerDAO.createPlayer(player);
    }
}
