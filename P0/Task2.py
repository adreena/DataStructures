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
def get_month_name(month_num):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'Octobre', 'November', 'December']
    return months[month_num-1]


# Time complexity: O(n)
# Loop thought calls: O(n) 
# splitting phone number: O(m) which is not significant
# getting month_name : O(1)
def longest_time_on_call(calls):
    longest_time = None
    telephone_number = None
    date = None
    for call in calls:
        if telephone_number is None or float(call[-1])>longest_time:
            longest_time = float(call[-1])
            telephone_number = call[0]
            date = call[-2].split(' ')[0]
    if date is not None:
        date_values = date.split('-')
        year = date_values[-1]
        month = get_month_name(int(date_values[0]))
        print('{} spent the longest time, {} seconds, on the phone during {} {}.'.format(telephone_number, longest_time, month, year))
    
longest_time_on_call(calls)