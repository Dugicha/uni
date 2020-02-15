package btu;

public class WordGenerator implements IGenerator {
    private LetterGenerator lowerLetterGenerator, upperLetterGenerator;
    private int minLength, maxLength;
    private boolean capitalized;

    public WordGenerator(LetterGenerator llg, LetterGenerator ulg, int minLength, int maxLength, boolean capitalized) {
        this.lowerLetterGenerator = llg;
        this.upperLetterGenerator = ulg;
        this.minLength = minLength;
        this.maxLength = maxLength;
        this.capitalized = capitalized;
    }

    @Override
    public String generate() {
        int len = (int) (minLength + Math.random() * (maxLength - minLength) + 1);
        String word = "";
        // If capitalized, generate first letter and run loop 1 less time
        if (capitalized) {
            word = upperLetterGenerator.generate();
            len -= 1;
        }
        for (int i = 0; i < len; i++) {
            word = word.concat(lowerLetterGenerator.generate());
        }
        return word;
    }
}
