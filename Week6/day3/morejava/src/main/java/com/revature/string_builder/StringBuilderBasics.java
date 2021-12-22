package com.revature.string_builder;

import com.sun.org.apache.xpath.internal.operations.String;

public class StringBuilderBasics {
    // if strings in java are immutable and clunky to work with, StringBuilder objects are the oppsoite
    // when you know you are going to need to make lots of changes to a string, use a StringBuilder

    public static void main(String[] args) {
        // StringBuilder objects do not store themselves in the Stringpool: they act like normal objects
        // creating two StringBuilder objects and giving them the same value will make two objects in the heap
        // that have the same value.
        StringBuilder stringBuilder = new StringBuilder("This is my StringBuilder!");
        StringBuilder stringBuilder1 = new StringBuilder("This is my StringBuilder!");
        System.out.println(stringBuilder);
        // Unlike a string, when we call this method on the StringBuilder object it makes the change permanent
        stringBuilder.reverse();
        // this will show a string of text that has been reversed
        System.out.println(stringBuilder);
        stringBuilder.reverse();
        // appending this string to the end of the Stringbuilder also makes the change permanent
        stringBuilder.append(" I am adding this to the stringbuilder!");
        System.out.println(stringBuilder);

        // general rule: use a string when possible, use a StringBuilder when you know you will make lots of
        // changes to the text before doing something with it (like passing it into a method or returning it from
        // a method

        // There is another class that is a part of the String API: StringBuffer. It is a thread-safe string, but we
        // will not be using it
    }
}
