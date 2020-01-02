# Used to generate constructors of Person class for testing the secret santa program (17-Lec9)

import random

def get_rand_name(length = None):
	letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	ret = ""
	for i in range(0, length):
		ret += random.choice(letters)
	return ret

def main():
	sexes = ["female", "male"]
	random.seed()

	f = open("code.txt", "w+")
	for i in range(1000):
		n = get_rand_name(25)
		f.write('\tPerson("{0}", "{0}@btu.edu.ge", "{1}"),\n'.format(n, random.choice(sexes)))

	f.close()

main()