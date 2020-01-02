num = ""

while (not num.isnumeric()):
	num = input("Input number of elements: ")

myDict = {}

for i in range(1, int(num) + 1):
	myDict[i] = i*i

print(myDict)