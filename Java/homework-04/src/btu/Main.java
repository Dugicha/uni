package btu;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String locale;
        int minWordLength, maxWordLength;
        int minWordCount, maxWordCount;
        int sentenceCount;

        // Read locale
        System.out.print("Language(en/ka/ru): ");
        locale = s.nextLine();

        // Read params
        System.out.print("Parameters: ");
        String params;
        params = s.nextLine();

        // Determine ascii limits based on locale
        char lowerMinAscii, lowerMaxAscii, upperMinAscii, upperMaxAscii;
        switch (locale) {
            case "ka":
                lowerMinAscii = 'ა';
                lowerMaxAscii = 'ჰ';
                upperMinAscii = 'ა';
                upperMaxAscii = 'ჰ';
                break;
            case "ru":
                lowerMinAscii = 'а';
                lowerMaxAscii = 'я';
                upperMinAscii = 'А';
                upperMaxAscii = 'Я';
                break;
            default:
                lowerMinAscii = 'a';
                lowerMaxAscii = 'z';
                upperMinAscii = 'A';
                upperMaxAscii = 'Z';
                break;
        }

        // Find errors in params
        if (!Pattern.compile("^p-\\d+").matcher(params).find()) {
            System.out.println("Mistake in parameters: p not found (sentence count)");
            return;
        }
        if (!Pattern.compile("^p-\\d+-s-\\d+").matcher(params).find()) {
            System.out.println("Mistake in parameters: s minimum not found (minimum word count per sentence)");
            return;
        }
        if (!Pattern.compile("^p-\\d+-s-\\d+-\\d+").matcher(params).find()) {
            System.out.println("Mistake in parameters: s maximum not found (maximum word count per sentence)");
            return;
        }
        if (!Pattern.compile("^p-\\d+-s-\\d+-\\d+-w-\\d+").matcher(params).find()) {
            System.out.println("Mistake in parameters: w minimum not found (minimum letter count per word)");
            return;
        }
        if (!Pattern.compile("^p-\\d+-s-\\d+-\\d+-w-\\d+-\\d+").matcher(params).find()) {
            System.out.println("Mistake in parameters: w maximum not found (maximum letter count per word)");
            return;
        }

        // Determine params
        String pattern = "^p-(\\d+)-s-(\\d+)-(\\d+)-w-(\\d+)-(\\d+)$";
        Pattern regex = Pattern.compile(pattern);
        Matcher matcher = regex.matcher(params);
        matcher.find();
        sentenceCount = Integer.parseInt(matcher.group(1));
        minWordCount = Integer.parseInt(matcher.group(2));
        maxWordCount = Integer.parseInt(matcher.group(3));
        minWordLength = Integer.parseInt(matcher.group(4));
        maxWordLength = Integer.parseInt(matcher.group(5));

        // Create generators
        LetterGenerator upperLG = new LetterGenerator(upperMinAscii, upperMaxAscii);
        LetterGenerator lowerLG = new LetterGenerator(lowerMinAscii, lowerMaxAscii);
        WordGenerator lowerWG = new WordGenerator(lowerLG, upperLG, minWordLength, maxWordLength, false);
        WordGenerator capitalWG = new WordGenerator(lowerLG, upperLG, minWordLength, maxWordLength, true);
        SentenceGenerator sg = new SentenceGenerator(lowerWG, capitalWG, minWordCount, maxWordCount);
        for (int i = 0; i < sentenceCount; i++) {
            System.out.print(sg.generate());
            System.out.print(" ");
        }
    }
}
