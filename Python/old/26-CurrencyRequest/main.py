from actions import init_actions, check_currency, view_history, quit

# Constants
API_KEY = "27b50a1b6f25849297dcebe7d96d7bd5"
BASE_CURRENCY = "EUR"
URL = f"http://data.fixer.io/api/latest?format=1&access_key={API_KEY}&base={BASE_CURRENCY}"
HISTORY_FILE_NAME = "history.txt"
HISTORY_ENTRY_LIMIT = 5
VALID_CHOICES = {
	0: f"Check currency against {BASE_CURRENCY}", 
	1: "View history", 
	2: "Quit"
}
DEFAULT_CHOICE = -1
QUIT_CHOICE = list(VALID_CHOICES.keys())[-1]

# ACTIONS are mapped to keys from VALID_CHOICES
ACTIONS = {
	0: check_currency,
	1: view_history,
	2: quit
}

def ask_choice():
	"""Asks the user for what they want to do and returns input"""
	choices = "\n"
	for num, description in VALID_CHOICES.items():
		choices += f"{num} - {description}\n"
	return input(f"{choices}Your choice: ")


def is_valid_choice(choice):
	"""Checks if input choice is valid"""
	try:
		if str(choice).isnumeric():
			n = int(choice)
			return n in VALID_CHOICES.keys()
	except:
		return False



# Initialize actions.py
init_actions(URL, BASE_CURRENCY, HISTORY_FILE_NAME, HISTORY_ENTRY_LIMIT)

choice = DEFAULT_CHOICE
# Run program while user doesn't want to quit
while choice != QUIT_CHOICE:
	# Revert choice to default after each action
	choice = DEFAULT_CHOICE
	# Keep asking until the choice is valid
	while not is_valid_choice(choice):
		choice = ask_choice()
	choice = int(choice)
	# Perform action
	ACTIONS[choice]()