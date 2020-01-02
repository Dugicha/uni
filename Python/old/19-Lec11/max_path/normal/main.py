final_sum = 0

with open("input.txt", "r") as file:
	for line in file:
		parsed_line = line.split(" ")
		final_sum += max(list(map(lambda x: int(x), parsed_line)))

print(final_sum)
