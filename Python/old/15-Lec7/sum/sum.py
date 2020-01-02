def my_sum(argList):
	ret = 0
	for item in argList:
		if str(item).isnumeric():
			ret += int(item)
	return ret

print(my_sum([700, 21, 400]))