'''
4)	Write a Program that accepts a main string and old sub string and a new sub string all as inputs from the user and returns a new string by replacing only first 2 occurrences of the old with the new sub string.
Hint: use string methods

Expected output like below

Enter the main stringPython’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.
Enter the old sub stringPython
Enter the new sub stringJava
Java’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Java programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.
'''

main_string = input("Enter the main string \n")
old_sub_string = input("Enter the old sub string \n")
new_sub_string = input("Enter the new sub string \n")

print(main_string.replace(old_sub_string, new_sub_string, 2))
