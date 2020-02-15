package com.nika.otiashvili;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        // 1
        float START = 1.0f, END = 2.0f;
        float y = 0;
        try {
            FileWriter fw = new FileWriter("function.txt");
            for (float x = START; x <= END; x += 0.01f) {
                y = (float) Math.pow(x, 2.0) + 2.0f * x + 3;
                fw.write(String.valueOf(y) + "\n");
            }
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 2
        float min = 0, max = 0;
        try {
            FileReader fr = new FileReader("function.txt");
            char[] buf = new char[100];
            // p - ახლანდელი რიცხვის ინდექსი
            int p = 0, code;
            char c;
            // წავიკითხოთ პირველი ხაზი რომ min-სა და max-ს მივანიჭოთ
            while ((code = fr.read()) != -1 && (c = (char) code) != '\n') {
                buf[p++] = c;
            }
            min = Float.parseFloat(String.valueOf(buf, 0, p));
            max = min;
            // წავიკითხოთ ყველა სხვა ხაზი
            p = 0;
            while ((code = fr.read()) != -1) {
                c = (char) code;
                buf[p++] = c;
                if (c == '\n') {
                    float num = Float.parseFloat(String.valueOf(buf, 0, p));
                    if (num > max)
                        max = num;
                    else if (num < min)
                        min = num;
                    p = 0;
                }
            }

            System.out.println("max: " + max);
            System.out.println("min: " + min);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 3
        ThirdProblem tp = new ThirdProblem(4700, 4998);
        tp.printFactorsA();
        tp.printPrimeFactorsB();
        tp.printWholeNumsAB();
        System.out.println(tp.getMostCommonCharB());
    }
}
