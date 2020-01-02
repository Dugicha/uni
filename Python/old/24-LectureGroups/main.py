from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, random, sys

# If you're seeing this, feel free to use this info in any way you want :^)
sender_email = "macecactus@mail.com"
sender_password = "Weapon69!"

# Open files
try:
	students_file = open("./students.txt", "r")
	lecturers_file = open("./lecturers.txt", "r")
except:
	print("Error while reading files. Make sure they exist!")

# Read students
students = students_file.read().split("\n")

# Read lecturers { lecturer_name : lecturer_email }
lecturers = {}
for line in lecturers_file:
	name = line.split()[0]
	email = line.split()[2]
	lecturers[name] = email


groups = {} # { lecturer_name : [student_names] }
min_students_in_group = len(students) // len(lecturers)
ungrouped_students = students[:]

def poprandom(array):
	return array.pop(random.randint(0, len(array) - 1))

# Distribute students evenly
for name, email in lecturers.items():
	students = []
	for i in range(min_students_in_group):
		students.append(poprandom(ungrouped_students))
	groups[name] = students[:]

# Distribute any extra students
if (len(ungrouped_students) != 0):
	for lecturer, students in groups.items():
		students.append(poprandom(ungrouped_students))

		# Check if everyone grouped
		if (len(ungrouped_students) == 0):
			break

# Login to email server
try:
	server = smtplib.SMTP("smtp.mail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(sender_email, sender_password)
except smtplib.SMTPAuthenticationError:
	sys.exit("Error authenticating email, check your credentials.")
else:
	print("Auth successful!")

def send_email(server, from_email, to_email, subject, body):
	# Create email obj
	msg = MIMEMultipart()
	msg["From"] = from_email
	msg["To"] = to_email
	msg["Subject"] = subject
	msg.attach(MIMEText(body, "plain"))
	# Send
	server.sendmail(from_email, to_email, msg.as_string())

# Send emails
for name, email in lecturers.items():
	student_names = ", ".join(str(n) for n in groups[name])
	subject = "Your group"
	body = "Dear, {}\n\tYour students are: {}.\nRegards,\nPython".format(name, student_names)
	try:
		send_email(server, sender_email, email, subject, body)
	except: # smtplib.SMTPRecipientsRefused:
		print("Email not sent to {} :(".format(email))
	else:
		print("Sent!")