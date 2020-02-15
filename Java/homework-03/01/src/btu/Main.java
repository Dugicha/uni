package btu;

import java.util.ArrayList;
import java.util.Random;

public class Main {
    // სორტირების ფუნქცია
    static void quickSort(ArrayList<Integer> arr, int left, int right) {
        if (left >= right) {
            return;
        }

        int pivot = left;
        for (int i = pivot + 1; i <= right; i++) {
            if (arr.get(i) < arr.get(pivot)) {
                // გავცვალოთ arr[i] და arr[pivot]
                int temp = arr.get(i);
                arr.set(i, arr.get(pivot));
                arr.set(pivot, temp);

                // გადავანაცვლოთ პივოტი თავის ახალ ადგილას (ბოლო უმცირესის მარჯვნივ)
                if (pivot + 1 != i) {
                    temp = arr.get(i);
                    arr.set(i, arr.get(pivot + 1));
                    arr.set(pivot + 1, temp);
                }
                pivot += 1;
            }
        }
        quickSort(arr, left, pivot);
        quickSort(arr, pivot + 1, right);
    }

    public static void main(String[] args) {
        final int NUM_COUNT = 12;
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        Random r = new Random();
        for (int i = 0; i < NUM_COUNT; i++) {
            numbers.add(r.nextInt());
        }

        // მხოლოდ კენტ ინდექსიანები გადავაკოპიროთ
        ArrayList<Integer> oddIndexNumbers = new ArrayList<Integer>();
        for (int i = 0; i < NUM_COUNT; i += 2) {
            oddIndexNumbers.add(numbers.get(i));
        }

        quickSort(numbers, 0, numbers.size() - 1);
        quickSort(oddIndexNumbers, 0, oddIndexNumbers.size() - 1);

        System.out.println("თავდაპირველი:");
        System.out.println(numbers);
        System.out.println("მიღებული:");
        System.out.println(oddIndexNumbers);
    }
}
