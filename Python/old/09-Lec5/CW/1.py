from random import randint

rand = randint(1, 25)
guess = ""
tryCount = 0
hintLimit = 3
maxTries = 5

while (tryCount < maxTries):
	tryCount += 1
	guess = ""
	while (not guess.isnumeric()):
		guess = input("Your guess: ")
	guessInt = int(guess)

	if (guessInt == rand):
		print("You win!")
		break
	if (tryCount == maxTries):
		print("You lose!")
	elif (tryCount >= hintLimit):
		if (guessInt > rand):
			print("Go lower")
		else:
			print("Go higher")



