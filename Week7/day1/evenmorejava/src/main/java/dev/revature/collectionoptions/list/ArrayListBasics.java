package dev.revature.collectionoptions.list;

import java.util.ArrayList;
import java.util.List;

public class ArrayListBasics {
    public static void main(String[] args) {
        // ArrayLists preserve the order of entry, they are indexable, and they allow duplicates
        List<Integer> myArrayList = new ArrayList<>();
        List<Integer> newArrayList= new ArrayList<>();
        // use the add() method to add elements to your ArrayList
        newArrayList.add(1);
        newArrayList.add(2);
        newArrayList.add(3);
        myArrayList.add(1);
        myArrayList.add(2);
        myArrayList.add(3);
        myArrayList.add(4);
        System.out.println(myArrayList);
        // use the get() method and index position to retrieve an element
        System.out.println(myArrayList.get(2));
        myArrayList.add(5);
        // use the set() method, along with an index position and a value, to replace the element
        // at the indicated index position with the new value
        myArrayList.set(0,0);
        myArrayList.set(1,1);
        myArrayList.set(2,2);
        System.out.println(myArrayList);
        // the size() method returns the size of the ArrayList
        System.out.println(myArrayList.size());
        // indexOf() and a given index position returns the stored value, -1 if the value is not in the ArrayList
        System.out.println(myArrayList.indexOf(6));
        // clear() removes all elements from the ArrayList
        myArrayList.clear();
        System.out.println(myArrayList);
        // addAll() adds all the elements from an object that implements the Collection interface
        myArrayList.addAll(newArrayList);
//        for (int x : newArrayList){
//            myArrayList.add(x);
//        }
        System.out.println(myArrayList);
        // remove() removes an element at the given index position, or it looks for the element you provide
        myArrayList.remove(1);
        System.out.println(myArrayList);
        List<String> showingRemove = new ArrayList<>();
        showingRemove.add("Ben");
        showingRemove.add("Kyle");
        showingRemove.add("Billy");
        // this method looks for the string "Billy" and removes it
        showingRemove.remove("Billy");
        System.out.println(showingRemove);
        // method will return false if the element can not be removed (like because it does not exist)
        System.out.println(showingRemove.remove("Billy"));

        // can hold your custom classes
        List<ArrayListBasics> holdsArrayListBasicObjects = new ArrayList<>();
    }
}
