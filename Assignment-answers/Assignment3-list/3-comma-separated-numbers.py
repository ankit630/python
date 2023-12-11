'''
3) Write a program that accepts space separated numbers
And display them as a tuple.

Expected output below

Enter the numbers100 200 300
['100','200','300']
'''

t1=input("Enter the numbers \n")
print(f"{tuple(t1.split())}")
