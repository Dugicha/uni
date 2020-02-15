package btu;

import java.io.IOException;

public class Main {

    public static void main(String[] args) {
/*
        ClassA a = new ClassA();
        a.meth1();
        System.out.println(a.meth2());
        System.out.println(a.meth3());
        a.meth4();
*/

        FamilyBudget fb = new FamilyBudget();
        fb.setMoney(50);
        fb.setMoney(5000000);
        fb.setMoney(12000);

        FamilyMember fm = new FamilyMember("a", "b", 34, "idk");
        try {
            fm.logFields();
        } catch (IOException e) {
            e.printStackTrace();
        }
        fm.borrowMoney(fb, 13000);
        fm.borrowMoney(fb, 11000);
    }
}
