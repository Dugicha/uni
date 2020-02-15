package btu;

import java.io.FileWriter;
import java.io.IOException;

public class FamilyMember {
    private final String LOG_FILE_NAME = "family.txt";

    String name, lastName, status;
    int age, money = 0;

    public FamilyMember(String name, String lastName, int age, String status) {
        this.name = name;
        this.lastName = lastName;
        this.age = age;
        this.status = status;
    }

    void logFields() throws IOException {
        FileWriter fw = new FileWriter(LOG_FILE_NAME, true);
        fw.write(name);
        fw.write(", ");
        fw.write(lastName);
        fw.write(", ");
        fw.write(status);
        fw.write(", ");
        fw.write(String.valueOf(age));
        fw.write('\n');
        fw.close();
    }

    void borrowMoney(FamilyBudget budget, int amount) {
        int m = budget.getMoney();
        if (amount > m) {
            return;
        }
        this.money += amount;
        budget.setMoney(m - amount);
    }
}
