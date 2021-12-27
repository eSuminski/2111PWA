package dev.revature.maps;

import java.util.HashMap;
import java.util.Map;

public class MapBasics {
    public static String myString;
    public static void main(String[] args) {
        System.out.println(myString);
        Map<Integer, String> myMap = new HashMap<>();
        myMap.put(1,"this is my first value");
        myMap.put(2,"this is my second value");
        myMap.put(3,"this is my third value");
        myMap.put(4,null);
        System.out.println(myMap);
        System.out.println(myMap.get(1));
        // getOrDefault will either return the value of the given key, or return a default value you provide
        System.out.println(myMap.getOrDefault(4, "key 4 does not exist"));
        System.out.println(myMap);
        // keySet returns a set containing the keys
        System.out.println(myMap.keySet());
        // returns a Collection of the values
        System.out.println(myMap.values());
        System.out.println(myMap.containsKey(4));
        System.out.println(myMap.containsValue("this is my second value"));
        // replace will replace the existing value of a key if the key exists
        myMap.replace(4,"this is the fourth value");
        System.out.println(myMap);
    }
}
