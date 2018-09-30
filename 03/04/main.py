"""
    ნიკოლოზ ოთიაშვილი, დავალება 3.4.

    გამოიტანს შეტანილი სამი რიცხვიდან უდიდესს
"""

def get_largest(a, b, c):
    """აბრუნებს სამი რიცხვიდად უდიდესს"""
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    largest = get_largest(a, b, c)
    print("Largest:", largest)

main()