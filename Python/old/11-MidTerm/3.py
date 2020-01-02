xmovnebi = ["a", "e", "i", "o", "u"]

word = input("sheiyvanet sityva: ")

xmovaniCount = 0

for char in word:
	if (not char.isnumeric()) and (char in xmovnebi):
		xmovaniCount += 1

print(xmovaniCount)