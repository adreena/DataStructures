"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longest_time_on_call(calls):
    numbers_with_time = {}
    max_time = 0
    number = None
    for call in calls:
        phone1 = call[0]
        phone2 = call[1]
        time = int(call[-1])
        if phone1 in numbers_with_time:
            numbers_with_time[phone1] += time
        else:
            numbers_with_time[phone1] = time
        if phone2 in numbers_with_time:
            numbers_with_time[phone2] += time
        else:
            numbers_with_time[phone2] = time

    for phone, time in numbers_with_time.items():
        if number is None:
            max_time = time
            number = phone
        else:
            if time > max_time:
                number = phone
                max_time = time
    print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(number, max_time))
    
longest_time_on_call(calls)