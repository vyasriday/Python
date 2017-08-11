# IN THIS MODULE WE WILL STUDY sets.

t = set(tuple([1,2,3,4,4,4,4]))
print(t)

# sets in python works in the same way as sets in Math works
# Each element in set is immutable

p = {1,2,3,4,5,6,7,8,8}
print("Set p is ",p)

p.add(12)

print(p)
print(type(p))

p.remove(1)
print(p)

# remove produces key error if the element is not present in the list
# So we can also use dicard() methos which will silently ignore the keyerror

p.discard(12)
p.discard(12)
print(p)
# How to create an empty set . This can be done using set() constructor

empty_set = set()

print(empty_set)

for i in range(0,100,7):
	empty_set.add(i)

print(empty_set) # Sets are unordered collections of elements

for i in empty_set:
	print(i)

# Update Method can be used to add multiple elements from another set or tuple oe a list

t = (1,2,3,4,5)
print(type(t))

empty_set.update(t)
print(empty_set)

new_Set = empty_set.copy()
print(new_Set)

print(new_Set is empty_set) 

# SET ALGEBRA
''' WE CAN USE SET UNION SET INTERSECTION METHODS ON SETS'''
x = {1,'Harry','Levester',0,10}
print(empty_set.union(x)) # Set operation is commutative
print(x.union(empty_set))
print(x.union(empty_set) == empty_set.union(x))

print(x.difference(empty_set)) # To find A-B OR B-A use difference method 

print(x.intersection(empty_set))

# Use symmetric_difference() to explicitly find differece i.e elements in either A or B but not both
p = {1,2,3,4,5,6,7}
q = {2,3,10,11,12,15,0,0}
print(p.symmetric_difference(q))

# Using issubset() method to check whether one set is subset of another, issuperset() to check superset and isdisjoint() method to check disjoint sets

print(p.issubset(q))
print(p.issuperset(q))
print(p.isdisjoint(q))