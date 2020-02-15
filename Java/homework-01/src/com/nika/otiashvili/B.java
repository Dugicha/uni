package com.nika.otiashvili;

import java.util.Scanner;

public class B extends A {
    public int y;

    // მეთოდი 1
    public void setY() {
        Scanner s = new Scanner(System.in);
        System.out.print("y: ");
        y = s.nextInt();
    }

    // მეთოდი 2
    public int getXYSum() {
        return x + y;
    }
}
