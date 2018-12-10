'''
    ნიკა ოთიაშვილი, დავალება 1.2.
    გადაიყვანს რიცხვებს ერთი პოზიციური სისტემიდან მეორეში.
'''

# რიცხვების 11-ობითიდან 36-ობითამდე ჩაწერის მაგიდა
table = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G",
    17: "H",
    18: "I",
    19: "J",
    20: "K",
    21: "L",
    22: "M",
    23: "N",
    24: "O",
    25: "P",
    26: "Q",
    27: "R",
    28: "S",
    29: "T",
    30: "U",
    31: "V",
    32: "W",
    33: "X",
    34: "Y",
    35: "Z"
}
max_base = len(list(table.keys())) + 10 # +10 პირველი ათი ციფრის გამო

# რიცხვების ჩაწერის შემოტრიალებული მაგიდა
inv_table = {v: k for k, v in table.items()}

def dec_to_base(num, base):
    # გადაიყვანს ათობითიდან base-ობითში. აბრუნებს სტრინგს
    assert base <= max_base

    ans = ""
    quotent = num
    while True:
        remainder = quotent % base
        digit = table.get(remainder, str(remainder))
        ans = digit + ans

        if quotent == remainder:
            break

        quotent = int((quotent - remainder) / base)
    return ans

def base_to_dec(num, base):
    # გადაიყვანს base-ობითიდან ათობითში. აბრუნებს int-ს
    assert base <= max_base
    assert type(num) is str

    ans = 0
    for i, c in enumerate(num):
        pos = len(num) - i - 1
        '''უფრო მოკლედ ჩავწერდი temp = inv_table.get(c, int(c)) მაგრამ 
        int(c) ახურებს როცა c სიმბოლოა. ამიტომ მიწევს აქ if ის დაწერა'''
        temp = inv_table.get(c)
        if temp == None:
            temp = int(c)

        digit = temp * (base**pos)
        ans += digit

    return ans

def convert(num, from_base, to_base):
    # მაქსიმუმი შევამოწმოთ
    assert from_base <= max_base
    assert to_base <= max_base

    # თუ ტოლია პოზიციები, არ გავირჯეთ ტყუილად
    if from_base == to_base:
        return num

    # გადავიყვანოთ from_base-ობითიდან ათობითში
    dec = base_to_dec(num, from_base)
    # გადავიყვანოთ ათობითიდან to_base-ობითში
    ans = dec_to_base(dec, to_base)
    return ans

print("Max base: 36")
number = input("number: ")
from_base = int(input("from base: "))
to_base = int(input("to base: "))
ans = convert(number, from_base, to_base)
print(ans)