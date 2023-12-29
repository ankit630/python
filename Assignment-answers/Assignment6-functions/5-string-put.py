'''
5) Write a function that takes a string as input and returns a dictionary with key as character and value as number of occurrences of that character.
Expected output:
If function name is count_letters
Then count_letters("hello") should give output as
{'h':1,'e':1,'l':2,'o':1}
'''

string="hello"

def count_letters(string):
    d = {}
    i = 0
    for i in range(0, len(string)):
        key = string[i]
        value = string.count(string[i])
        if value >= 1:
            if key not in d:
                d[key]=value
            else:
                continue
        i = i+1
    print(d)

count_letters(string)
