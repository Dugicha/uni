package btu;

public class LetterGenerator implements IGenerator {

    private char minAscii, maxAscii;

    public LetterGenerator(char minAscii, char maxAscii) {
        this.minAscii = minAscii;
        this.maxAscii = maxAscii;
    }

    @Override
    public String generate() {
        return Character.toString((char) (minAscii + Math.random() * (maxAscii - minAscii) + 1));
    }
}
