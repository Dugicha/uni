import random
import os

students = []
questions = []
questions_in_test = 5

# Get all students
f_students = open("students.txt")
students = f_students.read().split("\n")
f_students.close()

# Get all questions
f_questions = open("questions.txt")
questions = f_questions.read().split("\n")
f_questions.close()

# Create tests folder
tests_dir = "tests"
if not os.path.exists(tests_dir):
	os.makedirs(tests_dir)

available_questions = questions[:]

def writeQuestions():
	random.seed()
	for student in students:
		f_test = open("{}/{}.txt".format(tests_dir, student), "w")
		for i in range(questions_in_test):
			f_test.write("{}\n".format(available_questions.pop(random.randint(0, len(available_questions) - 1))))

def printQuestions():
	random.seed()
	for student in students:
		print("test for {}\n".format(student))
		for i in range(questions_in_test):

			print("{}\n".format(available_questions.pop(
				random.randint(0, len(available_questions) - 1))
			))

#printQuestions()
writeQuestions()