myList = ["Deus", -80, 45, "Vult", 54, "!", 1080]

strSum = ""
intSum = 0

for item in myList:
	if type(item) is int:
		intSum += item
	elif type(item) is str:
		strSum += "{} ".format(item)

print(intSum)
print(strSum)