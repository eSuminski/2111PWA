package com.rev.objects.abstract_inheritors;

import com.rev.objects.AbstractClasses;

// see Adult class for extends and Override explanation
public class Baby extends AbstractClasses {

    public Baby(String abstractVariable){
        this.abstractVariable = abstractVariable;
    }

    public static void main(String[] args) {
        Baby baby = new Baby("this baby object also has access to the abstractVariable");
        System.out.println(baby.abstractVariable);
        baby.printMessage();
        Baby.classMethod();
        Baby.seeAbstractNumber();
    }

    @Override
    public void speak() {
        // if you check the Adult implementation of this function you will see it is different:
        // this is the power of polymorphism
        System.out.println("gogogaga");
    }
}
