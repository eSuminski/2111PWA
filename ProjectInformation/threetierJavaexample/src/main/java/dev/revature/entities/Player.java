package dev.revature.entities;

import java.util.Objects;

// we will be using the JavaBean design patter for this entity
// to be a true JavaBean class:
// private properties accessed via public getter and setter methods
// no args constructor and a constructor that sets all the properties
// override the toString, equals, and hashCode methods
public class Player {

    // all properties will be set to private in order to protect them from uninteded use
    // we will be making use of getter and setter methods to access these properties
    private String firstName;
    private String lastName;
    private int jerseyNumber;
    private int playerId;
    private int teamId;

    // JavaBeans make use of a no args constructor and a constructor that sets all the properties
    public Player(){}

    public Player(String firstName, String lastName, int jerseyNumber, int playerId, int teamId) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.jerseyNumber = jerseyNumber;
        this.playerId = playerId;
        this.teamId = teamId;
    }

    // JavaBeans override the default toString method, along with the equals and hashCode methods
    @Override
    public String toString() {
        return "Player{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", jerseyNumber=" + jerseyNumber +
                ", playerId=" + playerId +
                ", teamId=" + teamId +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Player player = (Player) o;
        return jerseyNumber == player.jerseyNumber && playerId == player.playerId && teamId == player.teamId && Objects.equals(firstName, player.firstName) && Objects.equals(lastName, player.lastName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(firstName, lastName, jerseyNumber, playerId, teamId);
    }

    // lastly, generate getter and setter methods so we can access the properties of this class

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getJerseyNumber() {
        return jerseyNumber;
    }

    public void setJerseyNumber(int jerseyNumber) {
        this.jerseyNumber = jerseyNumber;
    }

    public int getPlayerId() {
        return playerId;
    }

    public void setPlayerId(int playerId) {
        this.playerId = playerId;
    }

    public int getTeamId() {
        return teamId;
    }

    public void setTeamId(int teamId) {
        this.teamId = teamId;
    }
}
