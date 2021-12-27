package dev.revature.wrapperclasses;

public class Wrappers {
    public static void main(String[] args) {
        basicFunction(5);
        // we are passing in a primitive in as the argument, despite an Integer object being expected
        // Java will use autoboxing under the hood to convert the primitive into an object
        usingIntegerClass(5);
    }
    public static void basicFunction(int num){
        System.out.println("you entered the number " + num);
    }

    // Wrapper classes are the object versions of primitives. There are some Java methods that require the use of
    // objects for them to function, but you will be passing primitives in as the arguments. To allow
    // these functions to work, Java will either "box" or "unbox" your primitive value.

    // boxing = converting a primitive value into its object form
    // unboxing = converting an object into its primitive value
    // the process of boxing and unboxing is called "autoboxing"
    public static void usingIntegerClass(Integer num){
        System.out.println("you entered the number " + num);
    }
}
