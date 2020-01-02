# Utility functions for actions.py

def get_currency_url(base_url, req_currency):
	"""Gets api url for req_currency value against BASE_CURRENCY"""
	return f"{base_url}&symbols={req_currency}"

def get_request_answer(base_currency, req_currency, value):
	return f"1 {base_currency} is {value} {req_currency}"

def print_request_error(error_message, error_code = None):
	if error_code:
		print(f"Error Code: {error_code}")

	print(f"Error: {error_message}")

def is_valid_currency(req_currency):
	"""Checks whether the given currency is formatted correctly"""
	try: 
		req_currency = req_currency.replace(" ", "")
		return len(req_currency) == 3 and req_currency != "\n"
	except:
		return False

def clean_input(input_str):
	"""Cleans up currency input by removing spaces and CAPSing"""
	return str(input_str).replace(" ", "").upper()