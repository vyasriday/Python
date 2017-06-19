# Strings in Python are immutable sequences of unicode code points nad have a type str

a = "Strng"
print(type(a))

# We can use escape sequences to print our string on multiple lines
print("Hello World \n This will be printed on a new line\n")

#We can also use 3 quotes to print multiple line strings

print(''' This way multiple
	line strings are printed''')

# PYTHON RAW STRINGS

path = 'C:\\Users\\MrRobot\\Desktop'
print(path) #Results in Error if we don;t tell python that we need a \ there and it is not a escape sequence using two \\ which looks ugly sometimes

path_Better = r'C:\Users\MrRobot\Desktop' #Here r stands for raw strings which will automatically put  backslashes in path string and error won't be generated
print(path_Better)  # Prints C:\Users\MrRobot\Desktop

# AS STRNGS ARE SEQUENCES OF CHARACTRES WE CAN SEE THEM AS ARRAY (AS IN C/C++) AND CERTAIN INDEXING CAN BE DONE ON THEM

b  = 'This is a string'

print(b[0])
print(b[5])

for i in b:
	print(i)

print(path[3]) # printd U

print(path[2]) # Prints \

# CHARACTERS IN STRINGS ARE SINGLE ELEMENT STRINGS. THERE IS NO SEPARATE DATA TYPE FOR CHARACTERS IN STRING

B = 'X'
print(type(B))

#There are different types of methods in strings

small = 'yrlv'
print(small.capitalize()) # Capitalizes first letter but does not change original string
print(small)
a = "MY NAME IS ROBOT"
print(a[0:5:2])

#BYTES IN PYTHON
#bytes are immutable sequences of bytes 
# bytes are prefixed with b 

x = b'DATA'

print(type(x))
print(x)

y  = b"THIS IS BYTES TYPE"
print(y)

#We can also use indexing in bytes. Same as strings bytes is a sequences of bytes. DATA TYPE is bytes not byte
print(b[0])

# We can also perform perform encode and decode methods on bytes and can interconvert them into different formats

p = "adja ljdaouewi akdfja;dl lad ka;jd ;al [apd aj a;ldfkja'fkjff"
print(p.encode("utf-8")) # Here we are converting a normal string into streams of bytes

# CONVERSION BETWEEN BYTES AND STRINGS CAN BE DONE USING decode and encode methods

byteData = b'This is a stream of bytes'
print(byteData)

print(byteData.decode('utf-8')) # This will convert byteData into strings
 strings = "strings"
# print(strings.encode('byte-encoding')) encode is used to convert strings in to bytes Encoding must be known in advance 
 