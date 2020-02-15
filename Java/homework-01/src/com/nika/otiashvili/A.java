package com.nika.otiashvili;

import java.util.Scanner;

public class A {
    public int x;

    // კონსტრუქტორი
    public A() {
        System.out.println("Hello");
    }

    // მეთოდი 1
    public void setX() {
        Scanner s = new Scanner(System.in);
        System.out.print("x: ");
        x = s.nextInt();
    }

    // მეთოდი 2
    public void printXPlus12() {
        System.out.println(x + 12);
    }

    // მეთოდი 3
    public void xEvenOrOdd() {
        if (x % 2 == 0)
            System.out.println("X ლუწია");
        else
            System.out.println("X კენტია");
    }
}
