'''
Topic: f-strings

1) Write a Program to display current time using the format from user(according to the format codes for date time in standard C implementation)

Hint: you need to import datetime and find the current time like below

import datetime

current_time = datetime.datetime.now()

Hint: check the format for time specifiers from link

string -- Common string operations -- Python 3.12.0 documentation

Expected output below(1st line actual current time without formatting and second with format specifier)

2023-07-28 11:05:59.383320
current time is Friday-Jul-23 11-05-59
'''

import datetime

current_time=datetime.datetime.now()
print(current_time)

print(f"current time is {current_time.strftime('%A-%b-%y %H-%M-%S')}")
