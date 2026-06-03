# Creating a Set
my_set = {10, 20, 30, 40, 50}
print("Original Set:", my_set)

# Accessing Elements
print("Elements in the set:")
for item in my_set:
    print(item)

# Index
print("Sets do not support indexing.")

# Slicing
print("Sets do not support slicing.")

# Order
print("Sets are unordered collections.")

# Adding Elements
my_set.add(60)
print("After adding 60:", my_set)

# Removing Elements
my_set.remove(60)
print("After removing 60:", my_set)

# Duplicate Elements
my_set = {10, 20, 30, 20, 40, 10, 50}
print("Set after removing duplicates automatically:", my_set)

# Changeable Elements
my_set.add(70)
print("After adding 70:", my_set)

my_set.remove(20)
print("After removing 20:", my_set)