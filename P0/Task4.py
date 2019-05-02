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

# Time Complexity: O(n*m) + O(nlogn), if m is a big list O(n^2) and if m is not significant: O(nlogn)
#   find_telemarketers:
#    - checking text recieveer and senders: O(n*m)
#    	- O(n) loop throught texts 
#       - check numbers in texters list: O(m)
#    - checking phone calls list if received a call: O(n*m)
#       - O(n) loop through calls
#       - O(m) check if already in list of received calls to avoid dplication
#    - checking phone calls list if caller is telemarker:O(n*m)
#       - O(n) loop through calls
#       - O(m) check if it's not in 2 lits of recevied_calls and texters
#   sorting: O(nlogn)
#     - print: O(n)

def is_possibly_telemarketer(phone):
	mid = int(len(phone)/2)
	if phone[0] != '(' and phone[mid] != ' ':
		return True
	return False


def find_telemarketers(calls, texts):
	received_calls=[]
	telemarketers = []
	texters= []
	for text in texts:
		phone_1 = text[0]
		phone_2 = text[1]
		if is_possibly_telemarketer(phone_1) and phone_1 not in texters:
			texters.append(phone_1)
		if is_possibly_telemarketer(phone_2) and phone_2 not in texters:
			texters.append(phone2)

	for call in calls:
		phone = call[1]
		if is_possibly_telemarketer(phone)  and phone not in received_calls:
			received_calls.append(phone)

	for call in calls:
		phone = call[0]
		# never receive call:
		if is_possibly_telemarketer(phone) and phone not in received_calls:
			if phone not in texters and phone not in telemarketers:
				telemarketers.append(phone)

	telemarketers.sort()
	print("These numbers could be telemarketers: ")
	for phone in telemarketers:
		print(phone)

find_telemarketers(calls, texts)
