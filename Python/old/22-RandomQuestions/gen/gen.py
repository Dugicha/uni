import random

f = open("students.txt", "w")
endings = ["shvili", "ia", "dze", "iani"]
letters = "qwertyuiopasdfghjklzxcvbnm"
for i in range(0, 20):
	gvari = ""
	for i in range(0,6):
		gvari += random.choice(letters)
	gvari += random.choice(endings)
	f.write(gvari + "\n")
