# - signed magnitude - MSB denotes sign (1 is negative, 0 positive)
# - two's complement - flip bits and add 1 to get negative
# - one's complement - flip bits
# - excess-bias representation - numbers are shifted by bias B

'''
    ნიკა ოთიაშვილი, დავალება 2.3.
    გადაჰყავს ნიშნიანი ათობითი რიცხვი ორობითში და პირიქით 
'''
debug_mode = True
def log(msg, *m):
    if debug_mode:
        print("LOG:", msg, *m)

def flip_bits(num):
    # ატრიალებს ორობითი რიცხვის ბიტებს
    assert type(num) is str
    ans = ""
    for c in num:
        if c == "0":
            ans = "{}{}".format(ans, "1")
        else:
            ans = "{}{}".format(ans, "0")
    return ans

def to_bin(num):
    # გადაიყვანს ათობითიდან ორობითში უნიშნოდ
    assert type(num) is int
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
    # გამოიტანს ათობითი რიცხვის ორობითში ჩასაწერად საჭირო ბიტების რაოდენობას
    assert type(dec_num) is int
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
    # გადაიყვანს ორობითიდან ათობითში
    assert type(num) is str
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
    # აბრუნებს ათობითი რიცხვის ნიშანს ("-" ან "+")
    if dec_num[0] == "-":
        return "-"
    else:
        return "+"

def signed_magnitude_dec_to_bin(dec_num):
    # გადაიყვანს ნიშნიან ათობით რიცხვს ორობით ნიშნიან გამოსახულებაში
    assert type(dec_num) is str
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
    # აბრუნებს ნიშნიანი გამოსახულებით ჩაწერილი ორობითი რიცხვის ათობით მნიშვნელობას
    assert type(bin_num) is str
    # დავითრიოთ ნიშანი
    sign = "+"
    if bin_num[0] == "1":
        sign = "-"
    raw_bin_num = bin_num[1:]
    raw_dec_num = to_dec(raw_bin_num)
    return "{}{}".format(sign, raw_dec_num)

def twos_complement_dec_to_bin(dec_num):
    # გადაიყვანს ნიშნიან ათობით რიცხვს ორობით ფუძის დამატებით გამოსახულებაში
    assert type(dec_num) is str
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
    log("bit_size:", bit_size)
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
    log("raw_bin_num:", raw_bin_num)
    # დავატრიალოთ ბიტები
    flipped_bin_num = flip_bits(raw_bin_num)
    log("flipped_bin_num:", flipped_bin_num)
    # გადავიყვანოთ ათობითში, დავუმატოთ 1 და გადმოვიყვანოთ ორობითში 
    # TODO: აქ იკარგება მარცხენა ნულები
    temp_dec = to_dec(flipped_bin_num) + 1
    log("temp_dec:", temp_dec)
    bin_num = to_bin(temp_dec)
    log("bin_num:", bin_num)
    # დავუმატოთ ათობითში და მერე ორობითში გადაყვანისას დაკარგული ბიტები
    if len(bin_num) < len(flipped_bin_num):
        lost_bits = flipped_bin_num[:len(flipped_bin_num) - len(bin_num)]
        bin_num = "{}{}".format(lost_bits, bin_num)
    # გავზარდოთ ბიტების რაოდენობა თუ გასცდა უარყოფით ლიმიტს (2^(n-1))
    if raw_dec_num >= 2**(bit_size - 1):
        # მივუწეროთ 1-იანი
        bin_num = "{}{}".format("1", bin_num)
    #elif len(bin_num) > bit_size: # მოვაჭრათ მარცხნიდან თუ ზედმეტია
    #    bin_num = bin_num[len(bin_num) - bit_size:]
    # გამოვიტანოთ პასუხი
    return bin_num
    
def twos_complement_bin_to_dec(bin_num):
    # აბრუნებს ფუძის დამატებითი გამოსახულებით ჩაწერილი ორობითი რიცხვის ათობით მნიშვნელობას
    assert type(bin_num) is str
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
    # გადაიყვანს ნიშნიან ათობით რიცხვს ორობით შეკვეცილ ფუძის დამატებით გამოსახულებაში
    assert type(dec_num) is str
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
    # გაბრუნებს შეკვეცილი ფუძის დამატებითი გამოსახულებით ჩაწერილი ორობითი რიცხვის ათობით მნიშვნელობას
    assert type(bin_num) is str
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

def main():
    # შევიყვანოთ ინფორმაცია
    number = input("Number: ")    
    choice = int(input('''Choose the base of your number: 
        1) Base 10
        2) Base 2\n'''))
    # method = int(input('''Choose method: 
    #     1)signed magnitude
    #     2)two's complement
    #     3)one's complement
    #     4)excess-bias\n'''))
    if choice == 1:
        base = 10
        print("Signed magnitude:", signed_magnitude_dec_to_bin(number))
        print("Two's complement:", twos_complement_dec_to_bin(number))
    elif choice == 2:
        base = 2
        print("Signed magnitude:", signed_magnitude_bin_to_dec(number))
        print("Two's complement:", twos_complement_bin_to_dec(number))
