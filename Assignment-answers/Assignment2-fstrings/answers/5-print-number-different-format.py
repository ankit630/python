'''
5. Write a program that accepts a number from the user as input (may be a variable a) and print that number in different 
formats

Expected output

Enter the number 50
Value in different format is

decimal 50
binary 110010
octal 62
hexadecimal 32
'''

a=int(input("Enter the number \n"))

print(f'''Value in different format is       
      decimal {int(a)} 
      binary {bin(a)[2:]} 
      octal {oct(a)[2:]} 
      hexadecimal {hex(a)[2:]} ''')

