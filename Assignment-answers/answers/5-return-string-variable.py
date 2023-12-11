'''
5)	Write a Program that declares variable country with value Pakistan and returns a new string Afghanistan.

	First find the starting index of istan substring in Pakistan and
	Extract that istan slice from country variable and reassign it to the same variable by joining with “Afghan” string

Expected Output:
Afghanistan

'''

country="pakistan"
slice=country[country.find("istan"):]
country="Afghan"+slice
print("Afghan",slice, sep="")
