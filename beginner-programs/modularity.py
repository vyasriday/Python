
"""Module docstring should be placed at the beginning of the module before any statements"""
# shebang #! is used in python to tell machine which interpreter to use
#	#!/usr/bin/env python3 shebag is used to run scripts directly from terminal instead of using python abc.py we directly use ./abc.py after making it executable on linux/unix system.
#   From python3.3 this also works on windows but I need to see how?
def even_odd(x):
	""" Each function can have it's own docstring
		argyment : integer numebr
		purpose : checks if a number is odd or even"""
	if(x%2==0):
		print("Even Number")
		return 

	print("Odd Number")


def Square(y):
	if(y>10):
		return y*y
	else:
		return y**3

print(__name__) # this prints the name of our module or file when we run it on REPL

# Following code will help us run our module as python script as well
if __name__== '__main__':

	print( Square(int(input("Ente the No of which you want Square"))))


# HOW WE CAN IMPORT MULTIPLE FUNCTIONS USING IMPORT 
# from modularity import (func1(),func2(),func3() ... ) () after function name are optional

# What if we want to execute multiple functions we can use 
#if __name__ == '__main__':
#	main()

# sys.argv[1] is used to accept command line arguments and can be imported with import sys
  



