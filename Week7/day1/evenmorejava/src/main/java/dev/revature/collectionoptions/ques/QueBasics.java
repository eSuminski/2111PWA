package dev.revature.collectionoptions.ques;

import java.util.ArrayDeque;
import java.util.Deque;

public class QueBasics {
    public static void main(String[] args) {
        // Ques are a good choice when you want to follow a "first in, first out" principle

        Deque<String> myDeque = new ArrayDeque<>();
        // if there is no room for some reason, add will throw an exception if it can't add the element
        myDeque.add("Billy");
        myDeque.add("Sally");
        myDeque.add("Timmy");
        // offer, on the other hand, will just return false if it can't add the value
        myDeque.offer("Vlad");
        System.out.println(myDeque);
        myDeque.addFirst("Sid");
        System.out.println(myDeque);
        myDeque.addLast("Woody");
        System.out.println(myDeque);
        // you can get the first OR last element of a deque
        System.out.println(myDeque.getFirst());
        System.out.println(myDeque.getLast());
        // to return AND remove an element, use pop
        System.out.println(myDeque.pop());
        System.out.println(myDeque);
        // to just look use the peek method, if there are no elements will return null
        System.out.println(myDeque.peek());
        // use element() if you want an exception to be thrown if there is nothing in the deque
        System.out.println(myDeque.element());


    }
}
