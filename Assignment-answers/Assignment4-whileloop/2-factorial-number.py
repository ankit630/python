'''
2) Write a Program to find the factorial of a given number.

Expected output:

enter the number5
The factorial of 5 is 120
'''

num=int(input("enter the number \n"))

ele=1
factorial_value=1
while ele in range(1,num+1):
    factorial_value=factorial_value*ele
    ele=ele+1
    continue

print(factorial_value)
