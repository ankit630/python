'''
Write a program that accepts floating point zero negative number for the user and displays it as positive zero after rounding
    off to precision 2.

Expected output below

Enter the number -0.000045
The number you entered is 0.00
'''

first_number=abs(float(input("Enter the number \n")))

print(f"The number you entered is {first_number:.2f}")

