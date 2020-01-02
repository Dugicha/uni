final_sum = 0

a = 0

def add_lines_max(str_lines):
	if len(str_lines) == 0:
		return 0
	elif len(str_lines) == 1:
		return max(list(map(lambda x: int(x), str_lines[0])))
	else:
		return add_lines_max(str_lines[:-1]) + add_lines_max(str_lines[-1:])

parsed_lines = []
with open("input.txt", "r") as file:
	for line in file:
		parsed_lines.append(list(map(lambda x: x.strip("\n"), line.split(" "))))
print(add_lines_max(parsed_lines))
