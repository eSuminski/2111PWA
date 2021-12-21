package com.rev.objects.abstract_inheritors;

import com.rev.objects.AbstractClasses;

// use the extends keyword what class's properties(variables) and behaviors(methods) will be inherited
public class Adult extends AbstractClasses {
    // the Override annotation tells your compiler this method is overriding another: it will throw exceptions
    // if it does not actually override a method

    public Adult(String abstractVariable){
        this.abstractVariable = abstractVariable;
    }

    public static void main(String[] args) {
        Adult adult = new Adult("this was provided by the abstract class");
        System.out.println(adult.abstractVariable);
        adult.printMessage();
        Adult.classMethod();
        Adult.seeAbstractNumber();
    }


    @Override
    public void speak() {
        System.out.println("I can speak coherent sentences");
    }
}
