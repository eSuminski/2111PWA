package dev.revature.interactwithdatabase;

import dev.revature.connectingtodatabase.ConnectionBasics;
import dev.revature.entities.Player;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class PlayerDAOImp implements PlayerDAO{
    @Override
    public Player getPlayerById(int id) {
        try (Connection connection = ConnectionBasics.createConnection()){
            String sql = "select * from player where player_id = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            resultSet.next();
            Player player= new Player(
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
            while(resultSet.next()){
                Player player= new Player(
                        resultSet.getString("first_name"),
                        resultSet.getString("last_name"),
                        resultSet.getInt("jersey_number"),
                        resultSet.getInt("player_id"),
                        resultSet.getInt("team_id")
                );

                players.add(player);
            }

            return players;

        } catch (SQLException e){
            e.printStackTrace();
            return null;
        }
    }
}
