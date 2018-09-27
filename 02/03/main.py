"""
    ნიკა ოთიაშვილი, დავალება 2.3.

    გადაჰყავს ნიშნიანი ათობითი რიცხვი ორობითში და პირიქით ოთხი გზით:
    1. ნიშანი-სიდიდე - signed magnitude;
    2. ფუძის დამატებითი - two's complement;
    3. შეკვეცილი ფუძის დამატებითი - one's complement;
    4. წანაცვლებითი - excess-bias / biased representation.
    მეხუთე არჩევანი ოთხივეს პასუხს მოგვცემს

    ათობითიდან ორობითში გადაყვანისას ბიტების რაოდენობას ავტომატურად 
    ადგენს გადაცემულ რიცხვთან უახლოესი ზედა ორის ხარისხით (ჩვენ რომ 
    არ მოგვიწიოს ყოველ ჯერზე ბიტების რაოდენობის მითითება).
"""

def flip_bits(num):
    """ატრიალებს ორობითი რიცხვის ბიტებს."""
    ans = ""
    for c in num:
        if c == "0":
            ans = "{}{}".format(ans, "1")
        else:
            ans = "{}{}".format(ans, "0")
    return ans

def to_bin(num):
    """გადაიყვანს ათობითიდან ორობითში უნიშნოდ."""
    ans = ""
    quotent = num
    while True:
        remainder = quotent % 2
        ans = "{}{}".format(remainder, ans)
        if quotent == remainder:
            break
        quotent = int((quotent - remainder) / 2)
    return ans

def get_bit_size(dec_num):
    """გამოიტანს ათობითი რიცხვის ორობითში ჩასაწერად საჭირო ბიტების 
    რაოდენობას."""
    quotent = dec_num
    bit_size = 0
    while True:
        bit_size += 1
        remainder = quotent % 2
        if quotent == remainder:
            break
        quotent = int((quotent - remainder) / 2)
    return bit_size

def to_dec(num, sign="+"):
    """გადაიყვანს ორობითიდან ათობითში."""
    ans = 0
    for i, c in enumerate(num):
        pos = len(num) - i - 1
        digit = int(c) * (2**pos)
        ans += digit
    # მივუწეროთ ნიშანი პასუხს
    if sign == "+":
        return ans
    elif sign == "-":
        return "{}{}".format("-", ans)

def get_dec_sign(dec_num):
    """აბრუნებს ათობითი რიცხვის ნიშანს ("-" ან "+")."""
    if dec_num[0] == "-":
        return "-"
    else:
        return "+"

def signed_magnitude_dec_to_bin(dec_num):
    """გადაიყვანს ნიშნიან ათობით რიცხვს ორობით ნიშნიან გამოსახულებაში."""
    sign = get_dec_sign(dec_num)
    raw_num = dec_num
    if dec_num[0] == "-" or dec_num[0] == "+":
        raw_num = dec_num[1:]
    bin_num = to_bin(int(raw_num))
    if sign == "-":
        return "{}{}".format("1", bin_num)
    elif sign == "+":
        return "{}{}".format("0", bin_num)

def signed_magnitude_bin_to_dec(bin_num):
    """აბრუნებს ნიშნიანი გამოსახულებით ჩაწერილი ორობითი რიცხვის ათობით
    მნიშვნელობას."""
    # დავითრიოთ ნიშანი
    sign = "+"
    if bin_num[0] == "1":
        sign = "-"
    raw_bin_num = bin_num[1:]
    raw_dec_num = to_dec(raw_bin_num)
    dec_num = raw_dec_num
    # მივუწეროთ მინუსი თუ უარყოფითია
    if sign == "-":
        dec_num = "{}{}".format(sign, dec_num)
    return dec_num

def twos_complement_dec_to_bin(dec_num):
    """გადაიყვანს ნიშნიან ათობით რიცხვს ორობით ფუძის დამატებით 
    გამოსახულებაში."""
    # დავადგინოთ ნიშანი
    sign = get_dec_sign(dec_num)
    # წავაჭრათ ნიშანი (იგივე რაც abs ოღონდ სტრინგისთვის)
    raw_dec_num = 0
    if dec_num[0] == "-" or dec_num[0] == "+":
        raw_dec_num = int(dec_num[1:])
    else:
        raw_dec_num = int(dec_num)
    # ბიტების რაოდენობა დავიმახსოვროთ
    bit_size = get_bit_size(raw_dec_num)
    # თუ დადებითია, პირდაპირ გადავიყვანოთ
    if sign == "+":
        bin_num = to_bin(raw_dec_num)
        # გავზარდოთ ბიტების რაოდენობა თუ გადასცდა მაქსიმუმს (2^(n-1)-1)
        if raw_dec_num >= 2**(bit_size - 1) - 1:
            bin_num = "{}{}".format("0", bin_num)
        return bin_num
    # თუ უარყოფითია, განვაგრძოთ
    # გადავიყვანოთ ორობითში
    raw_bin_num = to_bin(raw_dec_num)
    # დავატრიალოთ ბიტები
    flipped_bin_num = flip_bits(raw_bin_num)
    # გადავიყვანოთ ათობითში, დავუმატოთ 1 და გადმოვიყვანოთ ორობითში 
    # TODO: აქ იკარგება მარცხენა ნულები
    temp_dec = to_dec(flipped_bin_num) + 1
    bin_num = to_bin(temp_dec)
    # დავუმატოთ ათობითში და მერე ორობითში გადაყვანისას დაკარგული ბიტები
    if len(bin_num) < len(flipped_bin_num):
        lost_bits = flipped_bin_num[:len(flipped_bin_num) - len(bin_num)]
        bin_num = "{}{}".format(lost_bits, bin_num)
    # გავზარდოთ ბიტების რაოდენობა თუ გასცდა უარყოფით ლიმიტს (2^(n-1))
    if raw_dec_num >= 2**(bit_size - 1):
        # მივუწეროთ 1-იანი
        bin_num = "{}{}".format("1", bin_num)
    return bin_num
    
def twos_complement_bin_to_dec(bin_num):
    """აბრუნებს ფუძის დამატებითი გამოსახულებით ჩაწერილი ორობითი
    რიცხვის ათობით მნიშვნელობას."""
    # დავადგინოთ ნიშანი
    sign = "+"
    if bin_num[0] == "1":
        sign = "-"
    # თუ დადებითია, პირდაპირ გადავიყვანოთ
    if sign == "+":
        return to_dec(bin_num)
    # დავატრიალოთ ბიტები
    flipped_bin_num = flip_bits(bin_num)
    # გადავიყვანოთ ათობითში და დავუმატოთ ერთი
    raw_dec_num = to_dec(flipped_bin_num) + 1
    # მივუწეროთ ნიშანი
    dec_num = "{}{}".format(sign, raw_dec_num)
    return dec_num

def ones_complement_dec_to_bin(dec_num):
    """გადაიყვანს ნიშნიან ათობით რიცხვს ორობით შეკვეცილ ფუძის 
    დამატებით გამოსახულებაში."""
    # დავითრიოთ ნიშანი
    sign = get_dec_sign(dec_num)
    # წავაჭრათ ნიშანი
    raw_dec_num = 0
    if dec_num[0] == "+" or dec_num[0] == "-":
        raw_dec_num = int(dec_num[1:])
    else:
        raw_dec_num = int(dec_num)
    # დავიმახსოვროთ ბიტების ზომა
    bit_size = get_bit_size(raw_dec_num)
    # თუ დადებითია, პირდაპირ გადავიყვანოთ
    if sign == "+":
        bin_num = to_bin(raw_dec_num)
        # თუ გადაცდა მაქსიმუმს (2^(n-1)-1) გავზარდოთ ზომა ერთი ბიტით
        if raw_dec_num >= 2**(bit_size - 1) - 1:
            bin_num = "{}{}".format("0", bin_num)
        return bin_num
    # თუ უარყოფითია, განვაგრძოთ
    # გადავიყვანოთ ორობითში
    raw_bin_num = to_bin(int(raw_dec_num))
    # გავზარდოთ ზომა ერთი ბიტით თუ გასცდა მინიმუმის ლიმიტს (2^(n-1)-1)
    if raw_dec_num >= 2**(bit_size - 1) - 1:
        raw_bin_num = "{}{}".format("0", raw_bin_num)
    # დავატრიალოთ ბიტები
    bin_num = flip_bits(raw_bin_num)
    return bin_num


def ones_complement_bin_to_dec(bin_num):
    """აბრუნებს შეკვეცილი ფუძის დამატებითი გამოსახულებით ჩაწერილი 
    ორობითი რიცხვის ათობით მნიშვნელობას."""
    # დავადგინოთ ნიშანი
    sign = "+"
    if bin_num[0] == "1":
        sign = "-"
    # თუ დადებითია, პირდაპირ გადავიყვანოთ
    if sign == "+":
        return to_dec(bin_num)
    # თუ უარყოფითია, განვაგრძოთ
    # დავატრიალოთ ბიტები
    flipped_bin_num = flip_bits(bin_num)
    # გადავიყვანოთ ათობითში
    raw_dec_num = to_dec(flipped_bin_num)
    # მივუწეროთ ნიშანი
    dec_num = "{}{}".format(sign, raw_dec_num)
    return dec_num

def excess_bias_dec_to_bin(dec_num):
    """გადაიყვანს ნიშნიან ათობით რიცხვს ორობით წანაცვლებით 
    გამოსახულებაში."""
    # დავითრიოთ ნიშანი
    sign = get_dec_sign(dec_num)
    # დავითრიოთ უმი (უნიშნო/მოდული) რიცხვი
    raw_dec_num = 0
    if dec_num[0] == "+" or dec_num[0] == "-":
        raw_dec_num = int(dec_num[1:])
    else:
        raw_dec_num = int(dec_num)
    # მოცემული რიცხვის ჩასაწერად საჭირო ბიტების რაოდენობა
    in_bit_size = get_bit_size(raw_dec_num)
    # თუ 1 ან 0-ა მოცემული, ერთ ბიტიანი ჩაწერაა და პირდაპირ გადავიყვანოთ
    if int(dec_num) == 0 or int(dec_num) == 1:
        return to_bin(raw_dec_num)
    # თუ -1 გვაქვს მოცემული, ორი ბიტია საჭირო მის ჩასაწერად
    if in_bit_size == 1:
        in_bit_size = 2
    """დავადგინოთ რამდენი ბიტი დაგვჭირდება ამ რიცხვის ჩასაწერად წანაცვლებით 
    წარმოდგენაში"""
    bit_size = in_bit_size
    # თუ ზედა ან ქვედა ლიმიტს ასცდა, ერთით მეტი ბიტი გვჭირდება მის ჩასაწერად
    if sign == "+" and raw_dec_num > 2**(in_bit_size - 1) - 1:
        bit_size += 1
    elif sign =="-" and raw_dec_num > 2**(in_bit_size - 1):
        bit_size += 1
    # წავანაცვლოთ
    offset = 2**(bit_size - 1)
    offset_dec_num = int(dec_num) + offset
    # გადავიყვანოთ ორობითში
    bin_num = to_bin(offset_dec_num)
    # თუ უარყოფითია, გვიწევს რომ შევავსოთ დარჩენილი ბიტები 0-ებით
    if sign == "-":
        bin_num = "{}{}".format("0" * (bit_size - len(bin_num)), bin_num)
    return bin_num

def excess_bias_bin_to_dec(bin_num):
    """აბრუნებს წანაცვლებითი გამოსახულებით ჩაწერილი ორობითი რიცხვის 
    ათობით მნიშვნელობას."""
    if bin_num == "0" or bin_num == "1":
        return str(to_dec(bin_num))
    # დავითრიოთ ნიშანი
    sign = "+"
    if bin_num[0] == "0":
        sign = "-"
    # შემოტანილი რიცხვის ბიტების ზომა
    bit_size = len(bin_num)
    # წავანაცვლოთ
    offset = 2**(bit_size - 1)
    offset_dec_num = to_dec(bin_num)
    dec_num = offset_dec_num - offset
    return str(dec_num)

def main():
    """ვეკითხებით მომხმარებელს გადასაყვან რიცხვს და წარმოდგენის ფორმას. 
    შემდგომ გამოგვაქვს პასუხი"""
    # ინფორმაცია ბიტების ავტომატურ დადგენაზე
    print("Bit size is automatically detected depending on your number.")
    # ამოვარჩევინოთ ფუძე (ამეორებს სანამ სწორი არ ამოირჩია)
    base_choice = ""
    while base_choice not in range(1, 3):
        base_choice = int(input('''\nChoose the base of your number: 
            1) Base 10
            2) Base 2\n'''))
        if base_choice not in range(1, 3):
            print("Wrong choice! Try again.")
    # ამოვარჩევინოთ რიცხვი
    number = input("Number: ")
    # წარმოდგენის მეთოდის არჩევანი (ამეორებს სანამ სწორი არ ამოირჩია)
    method = 0
    while method not in range(1, 6):
        method = int(input('''Choose method: 
            1) Signed magnitude
            2) Two's complement
            3) One's complement
            4) Excess-bias
            5) All four\n'''))
        if method not in range(1, 6):
            print("Wrong choice! Try again.")
    # პასუხის გამოტანა
    if base_choice == 1: # ათობითიდან ორობითში
        if method == 1 or method == 5:
            print("Signed magnitude:", signed_magnitude_dec_to_bin(number))
        if method == 2 or method == 5:
            print("Two's complement:", twos_complement_dec_to_bin(number))
        if method == 3 or method == 5:
            print("One's complement:", ones_complement_dec_to_bin(number))
        if method == 4 or method == 5:
            print("Excess-bias:", excess_bias_dec_to_bin(number))
    elif base_choice == 2: # ორობითდან ათობითში
        if method == 1 or method == 5:
            print("Signed magnitude:", signed_magnitude_bin_to_dec(number))
        if method == 2 or method == 5:
            print("Two's complement:", twos_complement_bin_to_dec(number))
        if method == 3 or method == 5:
            print("One's complement:", ones_complement_bin_to_dec(number))
        if method == 4 or method == 5:
            print("Excess-bias:", excess_bias_bin_to_dec(number))

main()