package dev.revature.collectionoptions.sets;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SetBasics {
    public static void main(String[] args) {
        // Sets do not maintain insertion order, only allow unique elements, and are not indexable
        // because Sets and Lists both implement the Collection interface their classes share many of the same methods
        Set<String> myHashSet = new HashSet<>();
        List<String> myArrayList = new ArrayList<>();

        myArrayList.add("Eric");
        myArrayList.add("Alejandro");
        myArrayList.add("Alejandro");
        myArrayList.add("Kyla");
        // like Lists, use the add() method to add objects to the Hashset
        myHashSet.add("Ted");
        myHashSet.add("Linda");
        myHashSet.add("Rufus");
        myHashSet.add("Mary");
        myHashSet.add("Virgil");
        System.out.println(myHashSet);
        myHashSet.add("Ted");
        System.out.println(myHashSet);
        // contains() will check if the object you pass as the argument is in the Set
        System.out.println(myHashSet.contains("Linda"));
        // addAll() takes any object that implements Collection and iterates through it  and adds the values to the Set
        myHashSet.addAll(myArrayList);
        System.out.println(myHashSet);
        // remove() checks for an object and removes it
        myHashSet.remove("Eric");
        System.out.println(myHashSet);
    }
}
