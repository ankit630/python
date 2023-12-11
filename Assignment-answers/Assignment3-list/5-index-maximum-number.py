'''
5) Write a Program that accepts a space separated group of numbers and joins them into a list and returns the index of the maximum value in the list.

Expected output

Enter the numbers100 20 40 10 300 16
Index of the maximum number is 
'''

n1=input("Enter the numbers \n")
n2=n1.split()
n3=list(map(int, n2))
max_number=max(n3)
print(f"Index of the maximum number is {n3.index(max_number)}")


