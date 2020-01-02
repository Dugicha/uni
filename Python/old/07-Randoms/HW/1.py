# Printavs randomul item-s myList-dan
# Prints random element from myList

import random
myList = ["atami", "vashli", "mandarini", "banani", "yurdzeni"]
print(myList[random.randint(0, len(myList) - 1)])