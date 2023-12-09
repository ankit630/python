'''
Write a program that accepts a number from a user and displays it with , as a thousand separator.
    
Expected output

Enter the number 251332
The number is 251,332
'''

num=int(input("Enter the number \n"))

print(f"The number is {num:,}")
