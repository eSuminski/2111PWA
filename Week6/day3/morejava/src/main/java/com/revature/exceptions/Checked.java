package com.revature.exceptions;

import java.io.FileWriter;
import java.io.IOException;

public class Checked {
    public static void main(String[] args) {
        String filePath = "src/main/resources/newFile.txt";
        String text = "Hello World!";
        // the IOException is a checked exception: if we do not have this code that might throw an IOException
        // inside of a try catch block then our application will not build: we are REQUIRED to catch it
        // and handle it so our code can actually be built and our application run
        try{
            createFile(filePath, text);
        } catch (IOException e){
            System.out.println("Error creating your file");
        }

    }


    // you can use the "throws" keyword at the end of a method to "duck" a checked exception. What this means
    // is that you are telling your code you know there is a checked exception in the method but you will
    // handle catching it somewhere else in your code. In this case, we are catching it in the main method
    public static void createFile(String path, String text) throws IOException{
        FileWriter writer = new FileWriter(path, true);
        writer.write(text);
        writer.close();
    }
}

