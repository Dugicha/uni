original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]

def flatten(int_list):
	if isinstance(int_list, list):
		if len(int_list) == 1:
			return int_list[0]
		else:
			return list(map(lambda x: flatten(x), int_list))
	else:
		return int_list

print(flatten(original_list))