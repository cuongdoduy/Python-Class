#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
print(mytuple[1])


#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new tuple with the specified items.
#Example
#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])