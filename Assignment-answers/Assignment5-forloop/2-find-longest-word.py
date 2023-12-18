'''
2) Write a Program to find longest word in a list of words


if input_list = ["Hello","Hi","Bye","hello","Python"]
Expected output:

Python
'''

input_list = ["Hello","Hi","Bye","hello","Python"]
length_input_list = len(input_list)
index = 0

greatest_length = 0
for index in range(0,length_input_list):
    if index == greatest_length:
        greatest_length = index
        continue
    elif index > greatest_length:
        greatest_length = index
        continue
    else:
        continue
print(input_list[greatest_length])
