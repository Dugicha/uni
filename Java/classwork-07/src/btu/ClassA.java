package btu;

import java.util.Scanner;

public class ClassA implements IMyInterface {
    final int M_SIZE = 15;
    int[] m = new int[M_SIZE];

    @Override
    public void meth1() {
        Scanner s = new Scanner(System.in);
        System.out.print("a: ");
        int a = s.nextInt();
        System.out.print("b: ");
        int b = s.nextInt();
        int min = Math.min(a, b);
        int max = Math.max(a, b);

        for (int i = 0; i < M_SIZE; i++) {
            m[i] = (int) Math.floor(min + (max - min + 1) * Math.random());
        }
    }

    public int meth2() {
        int sum = 0;
        for (int i = 0; i < M_SIZE; i++) {
            if (m[i] < i)
                sum += m[i];
        }
        return sum;
    }

    public int meth3() {
        int sum = 0;
        for (int i = 0; i < M_SIZE; i++) {
            if (m[i] > i)
                sum *= m[i];
        }
        return sum;
    }

    public void meth4() {
        for (int i = 0; i < M_SIZE; i++) {
            if (m[i] % 2 == 0)
                System.out.println(m[i]);
        }
    }
}
