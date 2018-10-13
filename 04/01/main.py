"""
    ნიკა ოთიაშვილი, დავალება 4.3.
    წრფივი ძებნა დალაგებულ მასივში.
"""

def compare(x, y):
    if x < y:
        return -1
    if x == y:
        return 0
    if x > y:
        return 1

def sorted_sequential_search(array, target):
    """ეძებს ზრდადობით დალაგებულ მასივში რიცხვს და აბრუნებს მის პოზიციას. 
    თუ ვერ იპოვა, აბრუნებს -1-ს"""
    # თუ უმცირესზე ნაკლებია საძებნი რიცხვი, -1 დავაბრუნოთ
    if compare(target, array[0]) == -1:
        return -1
    # თუ უდიდესზე მეტია საძებნი რიცხვი, -1 დავაბრუნოთ
    if compare(target, array[len(array) - 1]) == 1:
        return -1
    # დავუაროთ ყველა ელემენტს და შევადაროთ
    i = 0
    while i < len(array):
        if target == array[i]:
            return i
        i += 1
    # თუ აქამდე მოვედით, არ არის რიცხვი მასივში და დავაბრუნოთ -1
    return -1
