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

def call_time():
    calls_dictionary = {}

    for call in calls:
        if call[0] not in calls_dictionary:
            calls_dictionary[call[0]] = int(call[3])
        else:
            calls_dictionary[call[0]] += int(call[3])
        if call[1] not in calls_dictionary:
            calls_dictionary[call[1]] = int(call[3])
        else:
            calls_dictionary[call[1]] += int(call[3])

        longest_caller = max(calls_dictionary, key=calls_dictionary.get)
        longest_duration = max(calls_dictionary.values())

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_caller, longest_duration))

call_time()