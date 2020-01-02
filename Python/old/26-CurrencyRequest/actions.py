# Has all the actions the user can take
import urllib.request, json, datetime
from utils import *

# Variables to inject from init()
initialized = False
api_url = None
base_currency = None
history_file_name = None
history_entry_limit = None

# Inject variables
def init_actions(inj_api_url, inj_base_currency, inj_history_file_name, inj_history_entry_limit):
	"""Initializes actions.py: injects api_url and base_currency from main.py"""
	global initialized
	initialized = True

	global api_url
	api_url = inj_api_url
	global base_currency
	base_currency = inj_base_currency
	global history_file_name
	history_file_name = inj_history_file_name
	global history_entry_limit
	history_entry_limit = inj_history_entry_limit

def check_init(func):
	"""Decorator. Checks if actions.py is initialized and required variables have been injected""" 
	def wrapper():
		if initialized:
			func()
		else:
			raise Exception("actions.py not initialized. Blame the programmer!")
	return wrapper

def check_history_exists(func):
	"""Decorator. Checks if history file exists (if not, creates it)"""
	def wrapper():
		try:
			history_file = open(history_file_name, "r")
			history_file.close()
		except:
			print("History doesn't exist. Creating history file...")
			history_file = open(history_file_name, "w")
			history_file.close()
		finally:
			func()
	return wrapper
	
@check_init
@check_history_exists
def check_currency():
	"""ACTION: Checks the currency against BASE_CURRENCY"""
	# Get requested currency
	req_currency = ""
	while not is_valid_currency(req_currency):
		req_currency = input("Enter currency: ")

	# Clean up input
	req_currency = clean_input(req_currency)

	# Send request
	with urllib.request.urlopen(get_currency_url(api_url, req_currency)) as response:
		data = json.load(response)

		if (data["success"]):
			req_currency_value = data["rates"][req_currency]
			ans = get_request_answer(base_currency, req_currency, req_currency_value)
			print(ans)
			add_to_history(ans)
		else:
			error_code = data["error"]["code"]
			error_info = data["error"]["info"]
			print_request_error(error_info, error_code)

def add_to_history(entry):
	"""Adds new entry to history"""
	ENTRY_DELIMITER = "\n"
	new_entry = f"{entry} - {datetime.datetime.now()}"
	hist = open(history_file_name, "r+")
	text = hist.read()
	entries = text.split(ENTRY_DELIMITER)

	if len(entries) == 0:
		# If first entry, don't add \n
		hist.write(new_entry)
		hist.close()
	elif len(entries) >= history_entry_limit:
		# If over limit, remove last entry and shift up
		hist.close()
		entries = entries[1: history_entry_limit] 
		# don't use pop() here ^ because history.txt can be altered by user
		entries.append(new_entry)
		# Replace whole file with new entry list
		with open(history_file_name, "w+") as new_hist:
			new_hist.write(ENTRY_DELIMITER.join(entries))
	else:
		# Add entry with \n
		hist.write(f"{ENTRY_DELIMITER}{new_entry}")
		hist.close()


@check_init
@check_history_exists
def view_history():
	"""ACTION: Shows history"""
	print("\n")
	with open(history_file_name, "r") as hist:
		text = hist.read()
		if len(text) == 0:
			print("History empty")
		else:
			print(f"History:\n{text}")

@check_init
def quit():
	"""ACTION: Prints goodbye message"""
	print("Goodbye!")
