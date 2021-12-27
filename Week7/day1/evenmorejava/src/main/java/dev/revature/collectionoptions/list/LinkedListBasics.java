package dev.revature.collectionoptions.list;

import java.util.LinkedList;
import java.util.List;

public class LinkedListBasics {
    public static void main(String[] args) {
        // ArrayLists preserve the order of entry, they are indexable, and they allow duplicates
        List<Integer> myLinkedList = new LinkedList<>();
        myLinkedList.add(1);
        myLinkedList.add(2);
        myLinkedList.add(3);
        myLinkedList.add(4);
        System.out.println(myLinkedList);
    }
}
