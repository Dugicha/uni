package btu;

import java.util.ArrayList;
import java.util.Random;

public class Main {

    public static void main(String[] args) {
        final int NUM_COUNT = 12;
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        ArrayList<Integer> extraNumbers = new ArrayList<Integer>();
        Random r = new Random();
        for (int i = 0; i < NUM_COUNT; i++) {
            int n = 5 + r.nextInt(6);
            numbers.add(n);
            extraNumbers.add(n);
            if (i > 0 && i % 3 == 0) {
                extraNumbers.add(20 + r.nextInt(6));
            }
        }

        System.out.println("თავდაპირველი:");
        System.out.println(numbers);
        System.out.println("მიღებული:");
        System.out.println(extraNumbers);
    }
}
