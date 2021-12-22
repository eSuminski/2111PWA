package com.revature.object_class;

public class ObjectClassBasics {
    String classString;
    // The Object class is the root class of all others in Java, directly or indirectly. Any class that does not
    // explicitly inherit from another class will implicitly inherit from the Object class. If a class explicitly
    // inherits from another class, it will still benefit from the fact that its parent class, or whatever parent class
    // is at the top of the inheritance chain, is implicitly inheriting from the Object class.

    // The toString() method is implicitly called when you print an object. It is commonly overwritten by developers
    // when they create custom classes.
    @Override
    public String toString() {
        return "ObjectClassBasics{" +
                "classString='" + classString + '\'' +
                '}';
    }

    // another common method from the Object class to overwrite is the equals() method
    // By default, the method uses the == to compare the memory addresses of the two objects (the one calling the
    // method and the object being passed in as the argument). However, sometimes it can be beneficial to use a
    // different criteria instead.

    // hashCode() is a commonly overwritten method, but we will not have much use for it in this course. This method
    // returns a hash code, which is a number that categorizes an instance of a class (the object). Used for hashing
    // the object, which is something that happens in some of the Java Collections data structures.
}
