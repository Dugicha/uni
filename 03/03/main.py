"""
    ნიკოლოზ ოთიაშვილი, დავალება 3.3.

    დაადგენს არის თუ არა შეტანილი სამი მთელი რიცხვი ერთმანეთისგან 
    განსხვავებული
"""

def compare(a, b, c):
    """დააბრუნებს True-ს თუ სამივე რიცხვი განსხვავებულია, წინააღმდეგ 
    შემთხვევაში დააბრუნებს False-ს"""
    if a == b:
        return False
    if a == c:
        return False
    if b == c:
        return False
    return True

def main():
    """შეატანინებს სამ მთელ რიცხვს და გამოიტანს პასუხს"""
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    print(compare(a, b, c))

main()