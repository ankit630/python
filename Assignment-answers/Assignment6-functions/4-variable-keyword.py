'''
4) Write a function that can accept variable number of keyword arguments and returns the number of the keyword arguments passed

Expected output:
If function name in count_keyword_args
Then below line
count_keyword_args(a=1,b=2,c=3)
should give output as
3

'''


def count_keyword_args(**args):
    print(len(args))

count_keyword_args(a=1,b=2,c=3)
