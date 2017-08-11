'''
	SCOPES IN PYTHON ARE WHERE A VARIABLE CAN BE LOOKED UP.
	THERE ARE FOUR DIFFERENT SCOPES IN PYTHON

	LOCAL : LOCAL TO A FUNCTION

	ENCLOSING : SCOPE OF VARIABLE IS IN FUNCTION AND ALL ENCLOSING FUNCTIONS

	GLOBAL : DEFINED AT TOP LEVEL OF MODULE

	BUILT-IN : DEFINED BY BUILT IN TYPE 


'''


import math
value  = 25

def doubleValue():
	root = math.sqrt(value)
	print(root)


def countValue():
	global value # Here we refer to global value and therefore global value changes.
	value = 81
	print(value)


print(value)

doubleValue()

countValue()

print(value)