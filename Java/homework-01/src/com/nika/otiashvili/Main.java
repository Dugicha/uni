package com.nika.otiashvili;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
       // 1.1
       C cObj = new C();
       cObj.setInts();
       System.out.println(cObj.getLastDigitA());
       System.out.println(cObj.getFirstDigitB());
       System.out.println(cObj.getDigitSumC());
       System.out.println(cObj.getMethod2And3Product());
       System.out.println(cObj.getMethod3And5Sum());

       // 1.2
       A aObj = new A();
       aObj.setX();
       aObj.printXPlus12();
       aObj.xEvenOrOdd();
       B bObj = new B();
       bObj.setX();
       bObj.setY();
       System.out.println(bObj.getXYSum());

        // 1.3
        int a, b;
        Scanner s = new Scanner(System.in);
        System.out.print("a: ");
        a = s.nextInt();
        System.out.print("b: ");
        b = s.nextInt();

        // გავუცვალოთ ადგილი თუ მეტია
        if (a > b) {
            int temp = b;
            b = a;
            a = temp;
        }

        int numCount = 40, evenCount = 0 , oddCount = 0, evenSum = 0, oddSum = 0, numCountBetweenSums = 5;
        int[] randomNumbers = new int[numCount];
        System.out.println(numCount + " რიცხვი [" + a + "; " + b + "] ინტერვალში:");
        for (int i = 0; i < numCount; i++) {
            int newNum = a + (int) (Math.random() * (b - a));
            randomNumbers[i] = newNum;
            System.out.print(newNum + " ");

            if (newNum % 2 == 0) {
                evenCount += 1;
                evenSum += newNum;
            } else {
                oddCount += 1;
                oddSum += newNum;
            }
        }

        System.out.println("\nმათ შორის არის " + evenCount + " ლუწი და " + oddCount + " კენტი");
        System.out.println("ამ ლუწი რიცხვების ჯამი არის " + evenSum + ", ხოლო კენტების არის " + oddSum);

        // დავადგინოთ evenSum-სა და oddSum-ს შორის დიდი და პატარა
        int large, small;
        if (evenSum > oddSum) {
            large = evenSum;
            small = oddSum;
        } else {
            large = oddSum;
            small = evenSum;
        }

        System.out.println(numCountBetweenSums + " შემთხვევითი რიცხვი [" + small + "; " + large + "] ინტერვალში:");
        for (int i = 0; i < numCountBetweenSums; i++) {
            int newNum = small + (int) (Math.random() * (large - small));
            System.out.print(newNum + " ");
        }
    }
}
