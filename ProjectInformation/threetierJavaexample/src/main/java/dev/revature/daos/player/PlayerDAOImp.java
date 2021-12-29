package dev.revature.daos.player;

import dev.revature.customexceptions.PlayerNotFound;
import dev.revature.entities.Player;
import dev.revature.utility.ConnectionBasics;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class PlayerDAOImp implements PlayerDAO{
    @Override
    public Player getPlayerById(int id) {
        try (Connection connection = ConnectionBasics.createConnection()){
            // use ? to indicate you will be entering a value into your sql statement
            String sql = "select * from player where player_id = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            // indexing for preparedStatements starts at 1
            // would be setString for strings, setFloat for floats, etc.
            preparedStatement.setInt(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            // this checks if there is actually a row of data for us to draw from: true is returned if there is
            // and false is returned if there is not
            if(resultSet.next()) {
                Player player = new Player(
                        resultSet.getString("first_name"),
                        resultSet.getString("last_name"),
                        resultSet.getInt("jersey_number"),
                        resultSet.getInt("player_id"),
                        resultSet.getInt("team_id")
                );
                // this is also an acceptable way of creating your entity: using your setter methods
//            Player player2 = new Player();
//            player2.setPlayerId(resultSet.getInt("player_id"));
//            player2.setFirstName(resultSet.getString("first_name"));
//            player2.setTeamId(resultSet.getInt("team_id"));
//            player2.setJerseyNumber(resultSet.getInt("jersey_number"));
//            player2.setLastName(resultSet.getString("last_name"));
                return player;
            } else {
                // we throw a custom exception if the hasNext() method returns false
                throw new PlayerNotFound ("Player not found");
            }
        } catch (SQLException e){
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public List<Player> getAllPlayers() {
        try (Connection connection = ConnectionBasics.createConnection()){
            // because I am not manipulating the query any further I can use a statement instead of preparedStatement
            String sql = "select * from player";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(sql);
            List<Player> players = new ArrayList<>();
            // each iteration of this while loop tries to move the cursor to the next row of data
            // when there are no more rows of data the method returns false and we leave the loop
            while(resultSet.next()){
                Player player= new Player(
                        resultSet.getString("first_name"),
                        resultSet.getString("last_name"),
                        resultSet.getInt("jersey_number"),
                        resultSet.getInt("player_id"),
                        resultSet.getInt("team_id")
                );
                // make sure to add your players to a list
                players.add(player);
            }

            return players;

        } catch (SQLException e){
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public Player createPlayer(Player player) {
        try (Connection connection = ConnectionBasics.createConnection()){
           String sql = "insert into player values(?, ?, ?, default, ?)";
           PreparedStatement preparedStatement = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
           preparedStatement.setString(1, player.getFirstName());
           preparedStatement.setString(2, player.getLastName());
           preparedStatement.setInt(3, player.getJerseyNumber());
           preparedStatement.setInt(4, player.getTeamId());
           preparedStatement.execute();
           ResultSet resultSet = preparedStatement.getGeneratedKeys();
           resultSet.next();
           player.setPlayerId(resultSet.getInt("player_id"));
           return player;

        } catch (SQLException e){
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public Player updatePlayer(Player player) {
        return null;
    }

    @Override
    public boolean deletePlayer(int id) {
        return false;
    }
}
