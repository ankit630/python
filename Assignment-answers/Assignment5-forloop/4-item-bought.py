'''
4) Write a Program to calculate the total number of items bought by all guests.

Take below nested dictionary as input

allguests = {
	"Mark":{"icecreams":4,"cool drinks":5},
	"Ram":{"icecreams":6,"cool drinks":2},
	"Shyam":{"icecreams":7,"cool drinks":3}
}

Expected output:

{'icecreams':17,'cool drinks':10}
'''

allguests = {
    "Mark":{"icecreams":4,"cool drinks":5},
    "Ram":{"icecreams":6,"cool drinks":2},
    "Shyam":{"icecreams":7,"cool drinks":3}
}

total_icecreams = 0
total_cooldrinks = 0
for key in allguests:
    present = allguests[key]
    for key1 in present:
        if key1 == "icecreams":
            k1 = key1
            total_icecreams = total_icecreams + present[key1];
        elif key1 == "cool drinks":
            k2 = key1
            total_cooldrinks = total_cooldrinks + present[key1]
            continue

dict= { k1:total_icecreams, k2:total_cooldrinks}
print(f'{dict}')
