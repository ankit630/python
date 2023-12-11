'''
Write a Program to get the below output
Hint: use the align from format specifiers

price of item1 is ********30
price of item2 is *******200
price of item3 is *****20000
price of item4 is ****200000
price of item5 is ***2000000
price of item6 is **20000000
price of item7 is *200000000
price of item8 is 2000000000
'''
item1='30'
item2='200'
item3='2000'
item4='20000'
item5='200000'
item6='2000000'
item7='20000000'
item8='200000000'

print(f"price of item1 is {item1:*>9s}")
print(f"price of item2 is {item2:*>9s}")
print(f"price of item3 is {item3:*>9s}")
print(f"price of item4 is {item4:*>9s}")
print(f"price of item5 is {item5:*>9s}")
print(f"price of item6 is {item6:*>9s}")
print(f"price of item7 is {item7:*>9s}")
print(f"price of item8 is {item8:*>9s}")

