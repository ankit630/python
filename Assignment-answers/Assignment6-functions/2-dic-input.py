'''
2) Write a function that accepts a dictionary and returns 2 separate lists first one has the keys
second one has the values

Expected output:

If input_dict={'Ram':23,'Shyam':20,'Bheem':30}
and function name is lists_from_dict then
lists_from_dict(input_dict)
should give output as

Names are ['Ram','Shyam','Bheem']
Ages are [23,20,30]
'''


def lists_from_dict(input_dict):
    keys = []
    values = []
    for key,value in input_dict.items():
        keys.append(key)
        values.append(value)
    print(f"Names are {keys}")
    print(f"Ages are {values}")

lists_from_dict({'Ram':23,'Shyam':20,'Bheem':30})
