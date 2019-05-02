"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def is_possibly_telemarketer(phone):
	mid = int(len(phone)/2)
	if phone[0] != '(' and phone[mid] != ' ':
		return True
	return False


def find_telemarketers(calls, texts):
	all_numbers=[]
	incoming_call = []
	telemarketers = []
	texters = []
	for item in texts+calls:
		phone_1 = item[0]
		phone_2 = item[1]
		if phone_1 not in all_numbers:
			all_numbers.append(phone_1)
		if phone_2 not in all_numbers:
			all_numbers.append(phone_2)

	for call in calls:
		phone = call[1]
		if phone not in incoming_call:
			incoming_call.append(phone)

	for text in texts:
		phone_1 = call[0]
		phone_2 = call[1]
		# never receive call:
		if phone_1 not in texters:
			texters.append(phone_1)
		if phone_2 not in texters:
			texters.append(phone_2)

	for number in all_numbers:
		if number not in texters and number not in incoming_call:
			telemarketers.append(number)
	telemarketers.sort()
	print("These numbers could be telemarketers: ")
	for phone in telemarketers:
		print(phone)

find_telemarketers(calls, texts)
