'''
3) Write a Program to take password as input from the user

Expected output:

Enter the number 789
The sum of digits of 789 is 24
'''

num=int(input("enter the number \n"))
num_str=str(num)

sum_of_num=0
index=0
while index < len(num_str):
    sum_of_num=int(num_str[index]) + sum_of_num
    index=index+1
    continue

print(f"The sum of digits of {num} is {sum_of_num}")
