# Here we will try to write code for exceptional handling
from math import log
import sys


def convert(s):
    '''Convert a string to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        #print("Conversion error: {}".format(str(e)), file=sys.stderr)
        print("Conversion Error :" , str(e))
        print(file = sys.stderr)
        return -1


def string_log(s):
    v = convert(s)
    return log(v)

print(convert('hri'))

string_log(100)

def dividebyZero(x,y):

	#x  = int(input("Enter a number x"))
	#y  = int(input("Enter another number y"))

	try:
		print(x//y)

	except ZeroDivisionError:
		pass # Used because empty catch block is not allowed and creates indentation error
#		print(" Divide by Zero is not allowed")

x = int(input("Enter x"))
y = int(input("Enter y"))

dividebyZero(x,y)

def exceptional():
	try:
		x = input("Enter the string")
		y = int(x)
		print(" Successfully Executed " )
		return y

	except (TypeError,ValueError):    # Way to handle multiple type of exceptions
		print("Only Numbers in strings are excepted")
		return -1


print(exceptional())


# The problem here is that catch or except block is empty but it can not be left empty as it results in indentation error


