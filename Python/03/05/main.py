"""
    ნიკოლოზ ოთიაშვილი, დავალება 3.5.

    გამოიტანს სიიდან მეორე უდიდესი რიცხვის ინდექსს
"""

# რიცხვების სია (მაგალითი)
numbers = [0, 1, 5, 1, 7, 11, -4, 12]

def get_second_largest(numbers):
    """აბრუნებს მეორე ყველაზე დიდ რიცხვს გადაცემული სიიდან"""
    li = 0 # ყველაზე დიდის ინდექსი (largest index)
    sli = 0 # მეორე ყველაზე დიდის ინდექსი (second largest index)
    for i, num in enumerate(numbers):
        if num > numbers[li]:
            sli = li
            li = i
    return numbers[sli]

print("List:", numbers)
print("Second largest:", get_second_largest(numbers))