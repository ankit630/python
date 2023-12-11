'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(input())
    # Initialize an empty list to store the commands
    commands = []
    
    # Using _ is just a common convention in situations where the variable is intentionally unused.
    for _ in range(N):
        # Read each of input command from the user and converts it into list
        command = input().split()
        # appends the command list to the list of commands
        commands.append(command)
    
    # Initialize an empty list to perform the opeartions on
    my_list = []
    
    # Iterate over each element in the new commands list
    for command in commands:
        # Extracts the operation (e.g., insert, print, remove) from the command.
        operation = command[0]
        if operation == "insert":
            # Storing elements of command as position and element
            position = int(command[1])
            element = int(command[2])
            # insert the above elements in the empty list my_list with insert method
            my_list.insert(position, element)
        # otherwise print the my list
        elif operation == "print":
            print(my_list)
        # otherwise remove the element from list using remove method
        elif operation == "remove":
            element = int(command[1])
            my_list.remove(element)
        # otherwise append the element from list using append method
        elif operation == "append":
            element = int(command[1])
            my_list.append(element)
        # otherwise sort the list
        elif operation == "sort":
            my_list.sort()
        # print was previously used so dont need again since if print is there first one would be used to print and will not come in 2nd only once it will enter and program will stop
        # otherwise pop the list
        elif operation == "pop":
            my_list.pop()
        # otherwise reverse the list
        elif operation == "reverse":
            my_list.reverse()
        # print was previously used so dont need again since if print is there first one would be used to print and will not come in 2nd only once it will enter and program will stop
                    
