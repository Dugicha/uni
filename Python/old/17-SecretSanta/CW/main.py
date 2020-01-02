import random

class Person:
	def __init__(self, name, email, sex):
		self.name = name
		self.email = email
		self.sex = sex
		self.sends_to = None
		self.receives_from = None

	def set_pair(sender, receiver):
		sender.set_sends_to(receiver)
		receiver.set_receives_from(sender)

	def has_partner(self):
		return self.sends_to != None and self.receives_from != None

	def sends(self):
		return self.sends_to != None

	def receives(self):
		return self.receives_from != None

	def is_female(self):
		return self.sex == "female"

	def is_male(self):
		return self.sex == "male"

	def set_sends_to(self, person):
		self.sends_to = person

	def set_receives_from(self, person):
		self.receives_from = person

def get_available_receivers(people):
	ret = []
	for person in people:
		if not person.receives():
			ret.append(person)
	return ret

def get_available_senders(people):
	ret = []
	for person in people:
		if not person.sends():
			ret.append(person)

def get_random_partner(sender, people):
	receivers = get_available_receivers(people)
	# Remove current sender from list
	if not sender.receives():
		del receivers[get_index_by_email(sender.email, receivers)]
	if len(receivers) != 0:
		return random.choice(receivers)
	else:
		return None
	
def get_index_by_email(email, people):
	for i, person in enumerate(people):
		if person.email == email:
			return i

def print_pairs(people):
	# Sends messages to every pair
	for sender in people:
		receiver = sender.sends_to
		print("\nTo: {}| Dear {}, your secret santa is {}, with email {}"
				.format(sender.email, sender.name, receiver.name, receiver.email))

def everyone_paired(people):
	# Checks if everyone is properly paired to one another
	for person in people:
		if not person.has_partner():
			return False
	return True

def pair_everyone(people):
	# Pairs up every person
	random.seed()

	for sender in people:
		receiver = get_random_partner(sender, people)
		if receiver != None:
			Person.set_pair(sender, receiver)

def main():
	# Initializing people
	people = [
		Person("Garrosh", "garrosh@btu.edu.ge", "male"),
		Person("Valeera", "valeera@btu.edu.ge", "female"),
		Person("Rexxar", "rexxar@btu.edu.ge", "male"),
		Person("Anduin", "anduin@btu.edu.ge", "male"),
		Person("Thrall", "thrall@btu.edu.ge", "male"),
		Person("Jaina", "jaina@btu.edu.ge", "female"),
	]

	while not everyone_paired(people):
		pair_everyone(people)
	print_pairs(people)

main()