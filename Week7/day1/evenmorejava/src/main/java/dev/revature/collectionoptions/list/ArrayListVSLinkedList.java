package dev.revature.collectionoptions.list;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class ArrayListVSLinkedList {
    public static void main(String[] args) {
        // you can swap between arrayList and linkedList to see how they differ
        // searching is easier in ArrayLists, adding elements is easier in LinkedLists
        List<Object> arrayList = new ArrayList<>();
        List<Object> linkedList = new LinkedList<>();

        long start = System.nanoTime();
        for(int i =0; i<100_000; i++){
            linkedList.add(new Object()); // adding 100,000 objects to the END of the list
        }
        long end = System.nanoTime();
        System.out.println("Time to add 100,000 objects to the end " + (end-start)/1000000000.0);

        start = System.nanoTime();
        for(int i =0; i<100_000; i++){
            linkedList.get(50_000); // get object at middle of list
        }
        end = System.nanoTime();
        System.out.println("Time to get object 50_000 in the middle of the list " + (end-start)/1000000000.0);

        start = System.nanoTime();
        for(int i =0; i<100_000; i++){
            linkedList.add(0, new Object()); // add to the begining of the list 100_000 times
        }
        end = System.nanoTime();
        System.out.println("Time to add object 100_000 to the beginning of the list " + (end-start)/1000000000.0);

    }
}
