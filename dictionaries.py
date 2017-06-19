'''
 IN PYTHON DICTIONARIES ARE key:value PAIRS IN WHICH keys MUST BE IMMUTABLE BUT VALUES CAN BE MUTABLE VALUES
 ITEMS IN DICTIONARIES ARE NOT STORES IN ANY PARTICULAR ORDER
 DICTIONARIES IN PYTHON ARE KEY MAPPING AND ARE MUTABLE

 
 dict is a keyword in python
'''

# dict constructor can be used to convert any key value pair to a dictionary

l = [('Hena',234),('Rajama',456),('Joomla',112)]
d = dict(l)

print(d)
print(l) # Original list is not modified

dict1 = {'key1':'value1','key2':'value2'}

print(dict1)

# Copying  a dictionary

d1 = d.copy()
print(" Copied Dictionary is " ,d1)

# Another way of copying the dictionary is 

d2 = dict(d)

print(" d2 is ",d2)

dict1['key1'] = 'RAM' # we are assigning a new value to key1
 
print(dict1)

# Let us print a value corressponding to a particular key in a dictionary

print(dict1['key2'])

print(dict1.values()) # Method to print all the values corressponding to all the keys in a dictionary

print(dict1.keys())   # Similarly this method is used to print all the keys in the dictionary

# USING FOR LOOPS IN DICTIONARIES

dict2 = {1:12,2:13,3:14,4:15,6:27}

for values in dict2:
	print(values,  dict2[values]) # This will print keys of the dictionary
	


# HOW DO WE UPDATE AN EXISTING DICTIONARY 

print(d)

# Now we will modify the dictionary d using update method
# If the keys which are already present  in the dictionary and when we update the dictionary then the old values of existing keys are replaced with new values
# dictionaries are iterable so they can be used with for loops
g = {'1':'updates ','2':'list'}
d.update(g)

for key in d:
	print("{key} => {value}".format(key=key,value=d[key]))
print(d)

# dict.items returns the each key : value pair in the dictionary and dict.keys() and dict.values() are used to retrieve keys and values respectively from the dictionary
print("\nPrinting itesm keys and values of a dictionary using for loops\n")
for i in d.items():
	print(i)

for keys in d:
	print(keys)


print(d.values())

m = {'H': [1,0,1],'He':[4,5,6],'Li': [8,9,9]}
print(m)

m['H'] += [7,7,7] # This will add extend the list for H

print(m)

#Since Dictionaries are mutable we can add new pairs in it

m['B'] = [10,11,12]

print(m)

# For better readability we can use pprint from pprint module

from pprint import pprint as pp

pp(m)