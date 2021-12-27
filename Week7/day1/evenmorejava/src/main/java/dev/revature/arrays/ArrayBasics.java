package dev.revature.arrays;

public class ArrayBasics {
    public static int[] myFirstArray = new int[]{1,2,3,4};

    public static void main(String[] args) {
        // if you want to initialize the starting values when you create your array, use this method
        int[] myFirstArray = new int[]{1,2,3,4};
        for (int x: myFirstArray){
            System.out.println(x);
        }

        // if you want to create an array but not place elements inside it just yet, use this method
        int[] mySecondArray = new int[4];
        // use [] and the index position to place elements inside that index position
        mySecondArray[0] = 1;
        mySecondArray[1] = 2;
        mySecondArray[2] = 3;
        mySecondArray[3] = 4;
        for (int x : mySecondArray){
            System.out.println(x);
        }
        System.out.println(myFirstArray.length);
        // clone creates a copy of your array and returns the clone
        int[] myThirdArray = myFirstArray.clone();
        for (int x: myThirdArray){
            System.out.println(x);
        }
    }
}
