'''
1) Write a program to asks for a sub string and main string from the user and counts the number of occurences of the sub string in the main string

Note:- please use also the continue statement

Expected output:
Number of occurences of "Python" in
"PythonPythoni is good. Python supports dynamic typing.Python is used in data analysis"
is
4

Enter the main string PythonPython is good. Python supports dynamic typing.Python is used in data analysis
Enter the sub stringPython
Number of occurences of "Python" in
"PythonPython is good. Python supports dynamic typing.Python is used in data analysis." is
4
'''

main_string = input("Enter the main string \n")
sub_string = input("Enter the sub string \n")

# main_string = "PythonPython is good. Python supports dynamic typing.Python is used in data analysis"
# sub_string = "Python"
length_main_string = len(main_string)
length_sub_string = len(sub_string)
index = 0
count = 0
while index < length_main_string:
    if index == 0:
        if main_string[index] == "P":
            word = main_string[index:index+length_sub_string]
            if word == "Python":
                count = count+1
                index=index+1
                continue
            else:
                index=index+1
                continue
        else:
            index=index+1
            continue
    if main_string[index] == "P":
        word = main_string[index:index+length_sub_string]
        if word == "Python":
            count = count + 1
            index=index+1
            continue
        else:
            index=index+1
            continue
    else:
        index=index+1
        continue
print(count)
