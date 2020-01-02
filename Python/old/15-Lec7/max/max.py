def my_max(argList):
	ret = 0
	for item in argList:
		if item > ret:
			ret = item
	return ret

print(my_max([100, 200, 300]))