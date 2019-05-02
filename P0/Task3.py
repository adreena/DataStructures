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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# --------------------------
# Part A
# --------------------------
def is_fixed_line(phone):
	if phone[0] == '(':
		return True
	return False
def is_mobile(phone, length):
	mid = int(length/2)
	if phone[mid] == ' ':
		return True
	return False

def is_telemarketer(phone):
	if phone[0:3] == '140':
		return True
	return False

def get_fixed_line_code(phone):
	code = phone.split(')')[0]
	code = code[1:]
	return code

def find_code(phone):
	length = len(phone)
	if is_fixed_line(phone):
		code = get_fixed_line_code(phone)
	elif is_mobile(phone, length):
		code = phone[:int(length/2)]
	elif is_telemarketer(phone):
		code = '140'
	else:
		code = None
	return code


def find_codes(data):
	codes = []
	for row in data:
		phone_1 = row[0]
		phone_2 = row[1]
		code_1 = find_code(phone_1)
		code_2 = find_code(phone_2)
		if code_1 == '080':
			if code_2 is not None:
				if code_2 not in codes:
					codes.append(code_2)
	return codes

def print_sorted_codes(codes):
	codes.sort()
	for code in codes:
		print(code)

all_codes = find_codes(calls)
print_sorted_codes(all_codes)


# ---------------------------------------
# PART B
# ----------------------------------------
def count_calls_by_code(calls, code='080'):
	outgoing = 0
	incoming = 0
	for call in calls:
		phone_1 = call[0]
		phone_2 = call[1]
		if is_fixed_line(phone_1):
			code_1 = get_fixed_line_code(phone_1)
			if code_1 == code:
				outgoing +=1
				if is_fixed_line(phone_2):
					code_2 = get_fixed_line_code(phone_2)
					if code_2 == code:
						incoming += 1
	percent = 0
	if outgoing > 0:
		percent = (incoming/outgoing)*100
	print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))

count_calls_by_code(calls)