package dev.revature.tests.playerdaos;

import dev.revature.customexceptions.PlayerNotFound;
import dev.revature.daos.player.PlayerDAO;
import dev.revature.daos.player.PlayerDAOImp;
import dev.revature.entities.Player;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.List;

public class PlayerDAOTests {

    PlayerDAO playerDAO = new PlayerDAOImp();

    @Test
    void selectPlayerById(){
        Player player =playerDAO.getPlayerById(1);
        System.out.println(player);
        Assert.assertEquals(player.getPlayerId(), 1);
    }

    // we can test for exceptions like this
    @Test(expectedExceptions = PlayerNotFound.class, expectedExceptionsMessageRegExp = "Player not found")
    void selectPlayerByIdFail(){
        Player player = playerDAO.getPlayerById(1111111);
    }

    @Test
    void getAllPlayers(){
        List<Player> players = playerDAO.getAllPlayers();
        for (Player p : players){
            System.out.println(p);
        }
        Assert.assertTrue(players.size() >= 3);
    }

    @Test
    void createPlayer(){
        Player newPlayer = new Player("first", "last", 33, 0, 1);
        Player returnedPlayer = playerDAO.createPlayer(newPlayer);
        Assert.assertTrue(returnedPlayer.getPlayerId() != 0);
    }

    @Test
    void updatePlayer(){
        Assert.fail();
    }

    @Test
    void deletePlayer(){
        Assert.fail();
    }

}
