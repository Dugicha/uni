myStr = "red pink green pink black orange red pink black white black black orange pink pink red red white red"
myList = myStr.split(" ")
myDict = {}

for item in myList:
	if item not in myDict:
		myDict.update({item: 1})
	else:
		myDict[item] = myDict[item] + 1

print(myDict)