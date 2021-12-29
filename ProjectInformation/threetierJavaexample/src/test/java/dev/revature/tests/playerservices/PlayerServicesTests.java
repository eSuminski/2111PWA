package dev.revature.tests.playerservices;

import dev.revature.customexceptions.PlayerNotFound;
import dev.revature.daos.player.PlayerDAO;
import dev.revature.daos.player.PlayerDAOImp;
import dev.revature.entities.Player;
import dev.revature.services.PlayerServices;
import dev.revature.services.PlayerServicesImp;
import org.testng.annotations.Test;

public class PlayerServicesTests {

    static PlayerDAO playerDAO = new PlayerDAOImp();
    static PlayerServices playerServices = new PlayerServicesImp(playerDAO);

    @Test(expectedExceptions = PlayerNotFound.class, expectedExceptionsMessageRegExp = "Player not found")
    void badIdForGettingPlayer(){
        Player player = playerServices.getPlayerByIdService(10000);
    }

}
