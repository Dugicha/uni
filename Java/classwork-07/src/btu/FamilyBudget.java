package btu;

import java.io.FileWriter;
import java.io.IOException;

public class FamilyBudget {
    // When money > max(limits, i), we classify as limit[i]
    private final int RICH_LIMIT = 40000;
    private final int MID_LIMIT = 10000;
    private final int POOR_LIMIT = 0;

    final String LOG_FILE_NAME = "budget.txt";

    private int money;

    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
        try {
            logFamilyStatus();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String determineFamilyStatus() {
        if (money > RICH_LIMIT) {
            return "Rich";
        } else if (money > MID_LIMIT) {
            return "Middle";
        } else {
            return "Poor";
        }
    }

    public void logFamilyStatus() throws IOException {
        FileWriter fw = new FileWriter(LOG_FILE_NAME, true);
        fw.write(String.valueOf(getMoney()));
        fw.write('\n');
        fw.close();
    }
}
