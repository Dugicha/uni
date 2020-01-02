from pprint import pprint
import requests
import json

# Constants
URL = "https://api.tbcpay.ge/api/Service/NextStep"
DEFAULT_VALUE = ""
PAYLOAD = {
	"context":[
		{
			"key": "HAVEACCOUNT",
			"value": "1",
			"formatedValue": "1"
		},
		{
			"key": "account",
			"value": DEFAULT_VALUE
		}
	],
	"serviceId": 1213,
	"stepOrder": 2
}

def input_user_number():
	return input("Input your mobile number: ")

def format_user_number(num):
	return num[:3] + "-" + num[3:]

def get_payload_for_number(num):
	ret = PAYLOAD
	ret["context"][1]["value"] = num 
	return ret

def get_post_result(url, payload):
	return requests.post(url, json=payload)	

def get_carrier_from_result(res):
	return res.json()["data"]["title"]

# Main
raw_number = input_user_number()
number = format_user_number(raw_number)
payload = get_payload_for_number(number)
result = get_post_result(URL, payload)
carrier = get_carrier_from_result(result)
print(f"Your carrier is {carrier}")