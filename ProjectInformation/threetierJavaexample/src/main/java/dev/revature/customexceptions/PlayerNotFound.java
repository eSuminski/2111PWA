package dev.revature.customexceptions;

public class PlayerNotFound extends RuntimeException{
    public PlayerNotFound(String message){
        super(message);
    }
}
