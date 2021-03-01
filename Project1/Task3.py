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

"""PART A SOLUTION"""
def caller_area_codes(caller_num):
    if caller_num.startswith('(0'):
        return caller_num.split(')')[0] + ')'
    if (caller_num.startswith('7') or caller_num.startswith('8') or caller_num.startswith('9')):
        return caller_num[:4]
    if caller_num.startswith('140'):
        return '140'

    return None

def find_bangalore_numbers():
    new_list = set()

    for number in range(len(calls)):
        if calls[number][0].startswith('(080)'):
            new_list.add(caller_area_codes(calls[number][1]))

    called_codes_list = list(new_list)
    print('The numbers called by people in Bangalore have codes: {}'.format(called_codes_list.sort()))

    for sender in called_codes_list:
        print(sender)

find_bangalore_numbers()

"""PART B SOLUTION"""
def call_percentage():
    count1 = 0
    count2 = 0

    for number in range(len(calls)):
        if calls[number][0].startswith('(080)'):
            count1 += 1
            if calls[number][1].startswith('(080)'):
                count2 += 1

    print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(round(count2 / count1*100, 2)))

call_percentage()

