def main():
	name1 = "Dato"
	age1 = "90"
	name2 = input("saxeli:")
	age2 = input("asaki:")

	print("{} aris {} wlis.".format(name1, age1))
	print("{} aris {} wlis.".format(name2, age2))

def meore():
	a1 = input("Nebismieri arsebiti saxeli: ")
	a2 = input("Meore nebismieri arsebiti saxeli: ")
	if (a1[len(a1) - 1] == "i"):
		b1 = a1[:len(a1) - 1] + "ma"
		b2 = a2[:len(a2) - 1] + "s"
		print("{} {} {} esrola".format(b1, b2, a2))

meore()