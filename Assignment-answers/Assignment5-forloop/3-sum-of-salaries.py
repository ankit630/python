'''
3) Write a Program that accepts name and salary of an employee from a dictionary and return the sum of salaries

if input_dict = {"Ram":10000,"Shyam":20000,"Mark":40000}

Expected output:

Sum of salaries is 70000

Note: input_dict here is just for an example, you can try with different inputs.
'''

input_dict = {"Ram":10000,"Shyam":20000,"Mark":40000}
sum_values=0
for key in input_dict:
    sum_values=sum_values+input_dict[key]
    continue
print(sum_values)
