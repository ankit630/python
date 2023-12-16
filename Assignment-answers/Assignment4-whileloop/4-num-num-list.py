'''
4) Write a Program that asks for
a) The number of numbers that you want in a list
b) Space separated numbers(those many numbers as you mentioned below)

Start a loop(repeat execution as the number of numberds) and accept the numbers one after the other and finally print the average of numbers

Note:- Don't use map function

Expected output
Enter how many numbers you want in the list 4
Enter the numbers 2 4 6 8
Average of the numbers in the list['2','4','6','8'] is 5.0
'''

count_of_numbers=int(input("Enter how many numbers you want in the list \n"))
numbers=input("Enter the numbers \n")
length_of_numbers=len(numbers)

list_numbers=[]
index = 0
while index < length_of_numbers:
    if numbers[index] != ' ':
        list_numbers.append(numbers[index])
        index = index+1
        continue
    else:
        index = index+1
        continue

index_list=0
sum = 0
while index_list < len(list_numbers):
    sum = sum + int(list_numbers[index_list])
    index_list = index_list + 1

average=sum/len(list_numbers)

print(f"Average of the numbers in the list{list_numbers} is {average}")
