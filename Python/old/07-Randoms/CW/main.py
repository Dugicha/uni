import random

lives = 5
failName = "Voldemort"
continueName = "Albus"

names = ["Harry", "Ron", "Hermione", "Luna", "Severus", "Voldemort", "Albus"]

def win():
	print("You win!")

def fail():
	print("You have lost :(")

def main():
	for i in range(lives):
		print(names)
		chosenName = random.choice(names)
		if (chosenName == failName):
			print("Random name is {}".format(failName))
			fail()
			break
		elif (chosenName == continueName):
			print("Random name is {}".format(continueName))
			continue
		elif (chosenName.lower() == input("Input name: ").lower()):
			win()
			break
		else:
			if (i == lives - 1):
				fail()
				break
			print("Ouch, you have {} lives remaining".format(lives - i - 1))

main()