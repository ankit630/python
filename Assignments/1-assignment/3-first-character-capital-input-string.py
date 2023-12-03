'''
3)	Write a Program that accepts a string and returns the capitalized(ony first becomes upper case) copy of it.

Hint: use string methods

Expected output like below

Enter any stringpython is good
Python is good
'''

input_string = str(input("Enter the string \n"))
print(input_string[0].upper() + input_string[1:])
