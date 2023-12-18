'''
1) Write a Program to find all the indices of a value in the list

Expected output

If input_list = [1,2,3,4,2,'h','e','l','l','o','2','0','0',100,200,'200','300',[300,400],'300']
output:
indices of '300'
16,18
'''

input_list = [1,2,3,4,2,'h','e','l','l','o','2','0','0',100,200,'200','300',[300,400],'300']
input_list_length = len(input_list)
occurence=[]
for i in range(0,input_list_length):
    if input_list[i] == '300':
        occurence.append(i)
        continue
    else:
        continue
print("indices of '300'")
length_of_occurence = len(occurence)
for i in range(0,length_of_occurence):
    print(occurence[i],end=', ')
