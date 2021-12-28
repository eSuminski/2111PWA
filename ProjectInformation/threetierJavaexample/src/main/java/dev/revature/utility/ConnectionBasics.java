package dev.revature.utility;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectionBasics {

    public static Connection createConnection(){

        try {
            String dbURL = String.format(
                    "jdbc:postgresql://%s:%s/%s?user=%s&password=%s",
                    System.getenv("HOST"),
                    System.getenv("PORT"),
                    System.getenv("DB"),
                    System.getenv("USER"),
                    System.getenv("PASSWORD")
            );
            Connection connection = DriverManager.getConnection(dbURL);
            return connection;
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
            return null;
        }
    }
    public static void main(String[] args) {
        System.out.println(createConnection());
    }

}
