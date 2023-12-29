'''
3) Write a function that takes 2 separate lists as inputs and returns the sum of the corresponding elements of the lists as a new list.
Assume that both are equal length lists.
Expected output:
If function name is add_two_lists then
add_two_lists([1,2,3],[4,5,6])
should give output as
[5,7,9]
'''

input_lists=([1,2,3],[4,5,6])
list1,list2 = input_lists

def add_two_lists(list1, list2):
    sum_list = []
    i = 0
    if len(list1) == len(list2):
        for i in range(0, len(list1)):
            value = list1[i] + list2[i]
            sum_list.append(value)
            i = i+1
        print(sum_list)

add_two_lists(list1, list2)
