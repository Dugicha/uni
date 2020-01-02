startNum = 2000
endNum = 3000

for i in range(startNum, endNum):
	if (i % 7 == 0) and (i % 10 != 0):
		print(i)