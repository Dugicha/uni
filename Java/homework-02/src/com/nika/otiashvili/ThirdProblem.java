package com.nika.otiashvili;

public class ThirdProblem implements IThirdProblem {
    int a, b;

    ThirdProblem(int a, int b) {
        this.a = a;
        this.b = b;
    }

    @Override
    public void printWholeNumsAB() {
        int min = Math.min(a, b);
        int max = Math.max(a, b);
        for (int i = min; i < max; i++)
            System.out.println(i);
    }

    @Override
    public void printFactorsA() {
        for (int i = 1; i < a; i++) {
            if (a % i == 0) {
                System.out.println(i);
            }
        }
    }

    @Override
    public void printPrimeFactorsB() {
        for (int i = 1; i < a; i++) {
            if (a % i == 0) {
                boolean isPrime = true;
                for (int j = 2; j < i; j++) {
                    if (i % j == 0) {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime)
                    System.out.println(i);
            }
        }
    }

    @Override
    public int getMostCommonCharB() {
        char[] s = String.valueOf(b).toCharArray();
        int[] counts = new int[10];
        for (int i = 0; i < s.length - 1; i++) {
            counts[s[i] - '0']++;
        }
        int maxindex = 0;
        for (int i = 1; i < counts.length; i++) {
            if (counts[i] > counts[maxindex])
                maxindex = i;
        }
        return maxindex;
    }
}
