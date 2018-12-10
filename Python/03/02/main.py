"""
    ნიკოლოზ ოთიაშვილი, დავალება 3.2.

    გამოითვლის რიცხვების საშუალო არითმეტიკულს გადაცემული სიიდან 
"""

# ფაილი, სადაც რიცხვებია ჩაწერილი
INPUT_FILE = "input.txt"

def average(numbers):
    """აბრუნებს გადაცემული რიცხვების საშუალო არითმეტიკულს""" 
    number_count = len(numbers)
    arithmetic_sum = 0
    for number in numbers:
        arithmetic_sum += number
    return arithmetic_sum / number_count

def main():
    """გამოიტანს ფაილში ჩაწერილი რიცხვების საშუალო არითმეტიკულს"""
    file = open(INPUT_FILE, "r")
    str_numbers = file.read().split(" ")
    file.close()
    # გადავიყვანოთ წაკითხული რიცხვები ნამდვილ რიცხვებში
    numbers = []
    numbers = [float(n) for n in str_numbers]
    
    avg = average(numbers)
    print("Average:", avg)

main()