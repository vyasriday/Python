# dIFFERENT TYPES OF NUMBERS IN PYTHON
""" In this triple quotes are used for docstrings. We can ourselves provide help guide using docstrings"""
#(zero)0b is used for binary numebr
x = 0b10 # It stands for 2
print(x)

# 0o stands for octal numbers

y = 0o72
print(y)

# 0x stands for Hexadecimal Numbers

z = 0xA

print(z)

# Numbers in strings can be converted to integers using int() function

print(int("1234")) # prints 1234

# Converting any number in string in particular base

print(int("10000" , 3)) # Here "1000" is a string which we need to convert into integer with base 3

print(int("100000",4))

print(int("1000000",5)) # This base thing is only working with 1 followed by multiple zeros type strings

print(int("100",2))

# FLOATING POINT NUMBERS

# Scientific Notation can be used to represent larger or very small numbers

print(3e8) # Prints Speed of Light which is 3 * 10^8

print(9.31e-10) 

# How to convert int in to floats as well strings in floats

print(float(18))
print(float("1234.15"))

print(float("nan")) # Not a number
print(float("inf")) # infinity
print(float("-inf")) # -ve infinity

a = None # None in python is nothing.
if(a==None):
	print("a is none");

if(a is None):
	print("Python has 'is' operator to check condition")

# BOOL TYPES
# bool eiter is True or False with first letter capital

print(bool(0))

print(bool(1234))

# Empty strings or lists or nay type of collection in python convert to False

print(bool([]))

print(bool(""))

print(bool({}))

print(bool([1,2,3]))