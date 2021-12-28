package dev.revature.playertests;

import dev.revature.entities.Player;
import dev.revature.interactwithdatabase.PlayerDAO;
import dev.revature.interactwithdatabase.PlayerDAOImp;
import org.postgresql.util.PSQLException;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.sql.SQLException;
import java.util.List;

public class PlayerDAOTests {

    PlayerDAO playerDAO = new PlayerDAOImp();

    @Test
    void selectPlayerById(){
        Player player =playerDAO.getPlayerById(1);
        System.out.println(player);
        Assert.assertEquals(player.getPlayerId(), 1);
    }

    @Test
    void getAllPlayers(){
        List<Player> players = playerDAO.getAllPlayers();
        for (Player p : players){
            System.out.println(p);
        }
        Assert.assertTrue(players.size() >= 3);
    }

}
