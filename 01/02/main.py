'''
    ნიკა ოთიაშვილი, დავალება 1.2 და 1.3.
'''

def convert(number, from_notation, to_notation):
    '''
    გარდაქმნის number რიცხვს, რომელიც from_notation-ობით არის ჩაწერილი,
    to_notation-ობით რიცხვამდე.
    '''
    if number <= 0:
        return 0 # უარყოფითი რიცხვები არ არსებობს ამ სამყაროში
    quotent = integer
    output = ""

    while (True):
        remainder = quotent % 2
        output = str(remainder) + output

        if (quotent == remainder): break

        quotent = int((quotent - remainder) / 2)

    return output