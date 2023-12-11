'''
4) Write a Program that accepts a space separated list of numbers and joins them into a list and displays the sorted list in descending order.

Enter the numbers30 400 20
['400','30','20']
'''

n1=str(input("Enter the numbers \n"))
n2=n1.split()
n2.sort(reverse=True)
print(n2)
