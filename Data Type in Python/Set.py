#Set are used to store multiple items in a single variable.
#A set is a collection which is both unordered and unindexed.
#Sets are written with curly brackets.
#Example
#Create a Set:
myset = {"apple", "banana", "cherry","apple"}
print(myset)
#Access Items
print("banana" in myset)
#Change Items
#Once a set is created, you cannot change its items, but you can add new items.
#Add Items
#To add one item to a set use the add() method.
#To remove an item in a set, use the remove(), or the discard() method.
#Example
#Add an item to a set, using the add() method:
myset.add("orange")
myset.remove("banana")
print(myset)
