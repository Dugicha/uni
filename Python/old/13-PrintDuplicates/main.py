f = open("ads.txt", "r")
s = f.read()
#myList = f.readlines()
myList = s.split(".")
newList = []
for item in myList:
	if item not in newList:
		#print(item)
		newList.append(item)
	else:
		print (item)