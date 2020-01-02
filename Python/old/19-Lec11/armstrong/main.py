in_list = [9, 10, 153, 154]

def get_armstrong_sum(num):
	str_num = str(num)
	ans = 0
	l = len(str_num)
	for char in str_num:
		ans += int(char)**l
	return ans

# For testing

#

# for num in in_list:
# 	print(num == get_armstrong_sum(str(num)))

for i in range(1, 3000):
	if i == get_armstrong_sum(i):
		print(i)
