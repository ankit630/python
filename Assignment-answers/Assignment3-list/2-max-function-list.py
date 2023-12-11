'''
2) Write a program that accepts two groups of separated numbers and joins them into list and displays it.

Hint: explore the max function

Enter the first group of numbers1 7 34
Enter the second group of numbers2 3 56
all numbers from both groups are['1','7','34','2','3','56']
The maximum number from both groups is 56
'''
first_group=input("Enter the first group of numbers \n")
second_group=input("Enter the second group of numbers \n")

print(f"all numbers from both groups are {first_group.split() + second_group.split()}")
total_group_str_element=first_group.split() + second_group.split()
total_group_int_element=list(map(int, total_group_str_element))
print(f"The maximum number from both groups is {max(total_group_int_element)}")
