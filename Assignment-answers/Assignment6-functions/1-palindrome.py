'''
1) Write a function that takes a string as input and returns whether it is palindrome or not.
Call the function twice once with a palindrome and another time with non-palindrome string.

Expected output:

If function name is palindrome then below two lines
palindrome("madam")
palindrome("hello")

should give output as

Palindrome
Not palindrome
'''

def palindrome(input_string):
    len_input_string = len(input_string)-1
    half_len = round(len(input_string)/2)
    i = 0
    while i in range(0, half_len+1):
        if input_string[i] == input_string[len_input_string-i]:
            value = 'Palindrome'
            i = i + 1
        else:
            value = 'Not palindrome'
            break
    print(value)

palindrome("madam")
palindrome("hello")
