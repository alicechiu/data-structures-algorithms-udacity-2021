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
def suspect_telemarketers():
    call_senders = set([record[0] for record in calls])
    call_receivers = set([record[1] for record in calls])
    text_senders = set([record[0] for record in texts])
    text_receivers = set([record[1] for record in texts])

    telemarketers = []

    for call_sender in call_senders:
        if (call_sender not in call_receivers and call_sender not in text_senders and
                call_sender not in text_receivers):
            telemarketers.append(call_sender)

    telemarketers.sort()

    print('\nThese numbers could be telemarketers:')
    for telemarketer in telemarketers:
        print(telemarketer)

suspect_telemarketers()
