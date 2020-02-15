package btu;

public class SentenceGenerator implements IGenerator {
    private WordGenerator lowerWordGenerator;
    private WordGenerator capitalWordGenerator;
    private int minWordCount, maxWordCount;

    public SentenceGenerator(WordGenerator lowerWordGenerator, WordGenerator capitalWordGenerator, int minWordCount,
                             int maxWordCount) {
        this.lowerWordGenerator = lowerWordGenerator;
        this.capitalWordGenerator = capitalWordGenerator;
        this.minWordCount = minWordCount;
        this.maxWordCount = maxWordCount;
    }

    @Override
    public String generate() {
        int count = (int) (minWordCount + Math.random() * (maxWordCount - minWordCount) + 1);
        // Generate first word with capital letter and run loop 1 less times
        String sentence = capitalWordGenerator.generate();
        // Run loop one less time since we generate last word outside the loop
        for (int i = 0; i < count - 2; i++) {
            sentence = sentence.concat(lowerWordGenerator.generate().concat(" "));
        }
        // Generate last word ending with period;
        sentence = sentence.concat(lowerWordGenerator.generate().concat("."));
        return sentence;
    }
}
