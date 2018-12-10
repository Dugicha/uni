"""
    ნიკოლოზ ოთიაშვილი, დავალება 3.1.
    
    აბრუნებს გადაცემულ ფაილში მთავრული ასოების რაოდენობას
"""

# ფაილი, სადაც ჩვენი ტექსტია მოთავსებული
INPUT_FILE = "input.txt"

def count_capitals(text):
    """აბრუნებს გადაცემულ ტექსტში მთავრული ასოების რაოდენობას"""
    count = 0
    for c in text:
        if c.isupper():
            count += 1
    return count

def main():
    """კითხულობს ფაილიდან ტექსტს და გამოაქვს მასში მთავრული ასოების
    რაოდენობა"""
    file = open(INPUT_FILE)
    text = file.read()
    file.close()
    cap = count_capitals(text)
    print("Capitals:", cap)

main()