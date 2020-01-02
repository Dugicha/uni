def toBinary(integer):
	if (integer < 0): return 0
	quotent = integer
	output = ""

	while (True):
		remainder = quotent % 2
		output = str(remainder) + output

		if (quotent == remainder): break

		quotent = int((quotent - remainder) / 2)

	return output

# Adds two decimals and converts the result to binary
def plus(f, s):
	return toBinary(f + s)

# Subtracts two decimals and converts the result to binary
def minus(f, s):
	return toBinary(f - s)

# Multiplies two decimals and converts the result to binary
def multi(f, s):
	return toBinary(f * s)

# Divides two decimals and converts the result to binary
def div(f, s):
	return toBinary(int(f / s))

'''def addBin(fBin, sBin):
	f = str(fBin)
	s = str(sBin)
	if (len(f) > len(s)):
		s = "0" * (len(f) - len(s))
	elif (len(f) < len(s)):
		f = "0" * (len(s) - len(f))

	ret = ""
	for i in range(0, len(f)):
		ret = str(int(s[i]) + int(f[i])) + ret
'''
'''
# Multiplies binary numbers
def mutliBin(fBin, sBin):
	f = str(fBin)
	s = str(sBin)
	
	# Shorter length x2 is array column count
	# Longer length is array row count
	rows = 0
	columns = 0
	if (len(f) < len(s)): 
		columns = len(f) * 2
		rows = len(s)
	else: 
		columns = len(s) * 2
		rows = len(f)

	# Init array with 0s
	lines = [["0"] * columns for row in range(rows)]

	for i in range(0, columns):
		for j in range(0, rows):
		lines[i][j]
	ret = ""
	for i in range(len(str(fBin)), -1, -1):
		for j in range(len(str(fBin)), -1, -1):
'''

actions = {"+": plus, "-": minus, "*": multi, "/": div}

def main():
	first = int(input("First integer: "))
	fBin = toBinary(first)

	action = input("Action: ")

	second = int(input("Second integer: "))
	sBin = toBinary(second)

	ans = actions[action](first, second)
	print(str(fBin) + " " + action + " " + str(sBin) + " = " + str(ans))

main()
