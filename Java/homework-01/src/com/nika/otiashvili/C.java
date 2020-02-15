package com.nika.otiashvili;

import java.util.Scanner;

public class C {
    int a, b, c;

    // მეთოდი 1
    public void setInts() {
        Scanner s = new Scanner(System.in);
        System.out.print("a: ");
        a = s.nextInt();
        System.out.print("b: ");
        b = s.nextInt();
        System.out.print("c: ");
        c = s.nextInt();
    }

    // მეთოდი 2
    public int getLastDigitA() {
        return a % 10;
    }

    // მეთოდი 3
    public int getFirstDigitB() {
        int digits = 1;
        while (Math.pow(10, digits) < b)
            digits += 1;
        return (int) (b / Math.pow(10, digits - 1));
    }

    // მეთოდი 4
    public int getDigitSumC() {
        int sum = c % 10;
        int digits = 1;
        while (Math.pow(10, digits) < c) {
            digits += 1;
            sum += (c % Math.pow(10, digits)) / Math.pow(10, digits - 1);
        }
        return (int) sum;
    }

    // მეთოდი 5
    public int getMethod2And3Product() {
        return getLastDigitA() * getFirstDigitB();
    }

    // მეთოდი 6
    public int getMethod3And5Sum() {
        return getFirstDigitB() + getMethod2And3Product();
    }
}
