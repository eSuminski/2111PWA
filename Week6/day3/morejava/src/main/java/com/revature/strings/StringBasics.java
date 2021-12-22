package com.revature.strings;

public class StringBasics {

    public static void main(String[] args) {
        // despite declaring three String objects here, because of the String pool, all of these refereences
        // are to the same string literal object, which is "this is the simplest way of making a string"
        String stringOne = "this is the simplest way of making a string";
        String stringTwo = "this is the simplest way of making a string";
        String stringThree = stringTwo;
        System.out.println(stringThree.equals(stringOne)); // this will return true
        System.out.println(stringTwo.equals(stringOne));// this will also return true

        System.out.println(stringOne + " I am concatonating this onto stringOne!");
        System.out.println(stringOne);

        String stringFour = new String("this is the simplest way of making a string");

        // the equals() for strings compares the string literals, but the == checks memory position
        System.out.println(stringOne.equals(stringFour));
        System.out.println(stringOne == stringFour);
        // rule of thumb: equals() checks content, == checks memory location for objects
        // you can actually override the equals() in objects to give them custom ways of being compared

        System.out.println(stringFour.toUpperCase());
        System.out.println(stringFour);

        // there are many different methods you can call on a string: just remember that none of them are actually
        // changing the value of the string literal that resides within the string pool

    }

}
