'''
2) Write a program that accepts two numbers from the user i.e. One positive and one negative number and displays the output with + and - signs

Expected output:
Enter first number is 5
Enter second number is -7
The first number you entered is +5
The second number you entered is -7
'''

first_number=int(input("Enter first number \n"))
second_number=int(input("Enter second number \n"))

print(f"The first number you entered is {first_number:+}")
print(f"The second number you entered is {second_number}")
