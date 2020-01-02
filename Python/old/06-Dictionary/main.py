dict1 = {"nika": 17}
print("Number of items in dict1 : {}".format(len(dict1)))

tuple1 = ("guido", "tim")

inName = input("Input name: ")
inAge = input("Input age: ")

if (inName in tuple1):
	dict1[inName] = inAge

print("Number of items in dict1 : {}".format(len(dict1)))