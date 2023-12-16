'''
5) Write a Program that takes a space separated list of words and prints the longest word. 
Expected output:

enter the words 
hello hi python

The longest word is python
'''

words=input("Enter the words \n")

len_words=len(words)

index = 0
letter = ''
list_letter = []
while index < len_words:
    if words[index] != ' ':
        letter = letter + words[index]
        index = index+1
        if index == len_words:
            list_letter.append(letter)
            break
        continue
    else:
        list_letter.append(letter)
        list_letter.append(' ')
        letter = ''
        index = index+1
        continue

index1 = 0
length_list_letter=len(list_letter)
greatest_length_word = 0
while index1 < length_list_letter:
    if list_letter[index1] != " ":
        if greatest_length_word != index1:
            if len(list_letter[greatest_length_word]) > len(list_letter[index1]):
                index1=index1 + 1
                continue
            else:
                greatest_length_word = index1
                index1=index1 + 1
                continue
        else:
            greatest_length_word = greatest_length_word + index1
            index1=index1 + 1
            continue
    else:
        index1=index1 + 1
        continue

print(f"The longest word is {list_letter[greatest_length_word]}")
