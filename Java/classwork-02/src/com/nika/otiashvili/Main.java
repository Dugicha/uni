package com.nika.otiashvili;

// Classwork 02
// ნიკოლოზ ოთიაშვილი

import java.util.Random;
import java.util.Scanner;

public class Main {

    // სავარჯიშო 1
    static void ex1() {
        System.out.print("C++\nC#\nJava\nPascal\nphp\nJavaScript\nActionScript");
    }

    // სავარჯიშო 2
    static void ex2() {
        Scanner scanner = new Scanner(System.in);
        int firstInt = scanner.nextInt();
        int secondInt = scanner.nextInt();
        System.out.println(firstInt + "/" + secondInt + " = " + firstInt / secondInt);
        System.out.println(secondInt + "/" + firstInt + " = " + secondInt / firstInt);
    }

    // სავარჯიშო 3
    static void ex3() {
        Scanner scanner = new Scanner(System.in);
        int firstInt = scanner.nextInt();
        int secondInt = scanner.nextInt();
        int thirdInt = scanner.nextInt();
        System.out.println(firstInt + " + " + secondInt + " + " + thirdInt + " = " + (firstInt + secondInt + thirdInt));
        System.out.println(firstInt + " * " + secondInt + " * " + thirdInt + " = " + (firstInt * secondInt * thirdInt));
    }

    // სავარჯიშო 4
    static void ex4() {
        Scanner scanner = new Scanner(System.in);
        int threeDigitInt = Math.abs(scanner.nextInt());
        int third = threeDigitInt % 10;
        int second = (threeDigitInt % 100) / 10;
        int first = threeDigitInt / 100;
        System.out.println(first);
        System.out.println(second);
        System.out.println(third);
    }

    // სავარჯიშო 5
    static void ex5() {
        Scanner scanner = new Scanner(System.in);
        int fourDigitInt = Math.abs(scanner.nextInt());
        int fourth = fourDigitInt % 10;
        int third = (fourDigitInt % 100) / 10;
        int second = (fourDigitInt % 1000) / 100;
        int first = fourDigitInt / 1000;
        System.out.println(first);
        System.out.println(second);
        System.out.println(third);
        System.out.println(fourth);
    }

    // სავარჯიშო 6
    static void ex6() {
        Scanner scanner = new Scanner(System.in);
        int num = Math.abs(scanner.nextInt());
        int last = num % 10;

        // ვადგენთ ციფრების რაოდენობას
        int digits = 1;
        while (Math.pow(10, digits) < num) {
            digits += 1;
        }

        // ვბეჭდავთ სათითაოდ
        for (int i = digits; i > 0; i--) {
            System.out.println((int) (num % Math.pow(10, i)) / (int) Math.pow(10, i - 1));
        }
    }

    // სავარჯიშო 7
    static void ex7() {
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();

        // 0-ის ქეისები აქვე მოვაგვაროთ
        if (num1 == 0 && num2 == 0) {
            System.out.println("უმცირესი საერთო ჯერადია 0");
            System.out.println("უდიდესი საერთო გამყოფი არ არსებობს");
            return;
        }

        if (num1 == 0) {
            System.out.println("უმცირესი საერთო ჯერადი (0-ის გარდა) არ არსებობს");
            System.out.println("უდიდესი საერთო გამყოფია " + num2);
            return;
        }

        if (num2 == 0) {
            System.out.println("უმცირესი საერთო ჯერადი (0-ის გარდა) არ არსებობს");
            System.out.println("უდიდესი საერთო გამყოფია " + num1);
            return;
        }

        int min = Math.min(num1, num2);
        int max = Math.max(num1, num2);

        // უმცირესი საერთო ჯერადი
        int absMax = Math.max(Math.abs(num1), Math.abs(num2));
        // ზედა ხაზზე ვიღებთ მოდულებს, რადგან როცა ერთ-ერთი რიცხვი უარყოფითია, უფრო მეტჯერ შესრულდება ციკლი.
        // მაგალითად: -6 და 2. 2 მეტი გამოდის (მოდულების გარეშე მაქსიმუმის აღებით), ამიტომ
        // მოგვიწევს შევამოწმოთ 2, 4 და 6. თუ მოდულების მაქსიმუმს ავიღებთ, გვიწევს მხოლოდ 6 შევამოწმოთ, რაც 3-ჯერ
        // ნაკლები ოპერაციაა ამ შემთხვევაში
        for (int i = absMax; i < Math.abs(absMax * min); i += absMax) {
            if (i % min == 0 && i % max == 0) {
                // თუ i > 0 შეგვიძლია მისი უარყოფითი ავიღოთ და _ტექნიკურად_ ეგ იქნება უმცირესი,
                // მაგრამ პროგრამირების დავალებაა და არა ლინგვისტიკის, ამიტომ დავტოვოთ ასე
                System.out.println("უმცირესი საერთო ჯერადია " + i);
                break;
            }
        }

        // უდიდესი საერთო გამყოფი, ევკლიდეს სტილში
        int a = min;
        int b = max;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        System.out.println("უდიდესი საერთო გამყოფია " + a);
    }

    // სავარჯიშო 8
    static void ex8() {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();

        // იმ შემთხვევისთვისაც მუშაობს, როცა m > n
        int min = Math.min(m,n);
        int max = Math.max(m, n);

        // max-მდე (და არა მისი ჩათვლით)
        for (int i = min; i < max; i++) {
            System.out.println(i);
        }
    }

    // სავარჯიშო 9
    static void ex9() {
        double[] numbers = {12, 8, -1.4, 99, 69, 69.69, -420, 0};
        // მინიმალურისა და მაქსიმალურის ინდექსები
        int min = 0;
        int max = 0;
        System.out.print("მასივის ელემენტებია: " + numbers[0]);
        // 1-დან ვიწყებთ, რადგან მენულე უკვე დამახსოვრებული გვაქვს
        for (int i = 1; i < numbers.length; i++) {
            System.out.print(", " + numbers[i]);
            if (numbers[i] < numbers[min]) {
                min = i;
            } else if (numbers[i] > numbers[max]) {
                max = i;
            }
        }
        System.out.print("\nუდიდესი ელემენტია " + numbers[max]);
        System.out.println("\nუმცირესი ელემენტია " + numbers[min]);
    }

    // სავარჯიშო 10, 11 და 12-ისთვის საჭირო სორტირების ფუნქცია
    static void quickSort(double arr[], int left, int right) {
        if (left >= right) {
            return;
        }

        int pivot = left;
        for (int i = pivot + 1; i <= right; i++) {
            if (arr[i] < arr[pivot]) {
                // გავცვალოთ arr[i] და arr[pivot]
                double temp = arr[i];
                arr[i] = arr[pivot];
                arr[pivot] = temp;

                // გადავანაცვლოთ პივოტი თავის ახალ ადგილას (ბოლო უმცირესის მარჯვნივ)
                if (pivot + 1 != i) {
                    temp = arr[i];
                    arr[i] = arr[pivot + 1];
                    arr[pivot + 1] = temp;
                }
                pivot += 1;
            }
        }
        quickSort(arr, left, pivot);
        quickSort(arr, pivot + 1, right);
    }

    // სავარჯიშო 10
    static void ex10() {
        double[] numbers = {12, 8, -1.4, 99, 69, 69.69, -420, 0};
        quickSort(numbers, 0, numbers.length - 1);
        for (double d : numbers) {
            System.out.println(d);
        }
    }

    // სავარჯიშო 11
    static void ex11() {
        double[] numbers = new double[8];
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = Math.random();
        }

        for (double d : numbers) {
            System.out.println(d);
        }
    }

    // სავარჯიშო 12
    static void ex12() {
        int[] numbers = new int[8];
        Random r = new Random();
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = r.nextInt();
        }

        // კონვერტაცია ნამდვილ რიცხვებამდე (quickSort-ისთვის)
        double[] dNumbers = new double[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            dNumbers[i] = numbers[i];
        }

        // დავალაგოთ ზრდადობით
        quickSort(dNumbers, 0, numbers.length - 1);

        // შევატრიალოთ
        for (int i = 0; i < dNumbers.length / 2; i++) {
            double temp = dNumbers[i];
            dNumbers[i] = dNumbers[dNumbers.length - 1 - i];
            dNumbers[dNumbers.length - 1 - i] = temp;
        }

        // დავბეჭდოთ მთელ რიცხვებად
        for (double d : dNumbers){
            System.out.println((int) d);
        }
    }

    public static void main(String[] args) {
        ex1();
        ex2();
        ex3();
        ex4();
        ex5();
        ex6();
        ex7();
        ex8();
        ex9();
        ex10();
        ex11();
        ex12();
    }
}
