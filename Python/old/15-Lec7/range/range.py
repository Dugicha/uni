def my_range(start, end = 0):
	if end < start:
		temp = end
		end = start
		start = temp

	ret = []
	i = start
	while i < end:
		ret.append(i)
		i += 1
	return ret

print(my_range(10))
print(my_range(4, 10))