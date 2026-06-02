# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Accessing Elements
my_list = [10, 20, 30, 40, 50]
print("First element:", my_list[0])
print("Last element:", my_list[4])

# Index
my_list = [10, 20, 30, 40, 50]
print("Index of 20:", my_list.index(20))

# Slicing
my_list = [10, 20, 30, 40, 50]
print("Elements from index 0 to 2:", my_list[0:3])
print("First two elements:", my_list[0:2])
print("Print the elements:", my_list[0:5])

# Adding elements
my_list = [10, 20, 30, 40, 50]
my_list.append(60)
print("After append:", my_list)

# Removing elements
my_list = [10, 20, 30, 40, 50, 60]
my_list.remove(60)
print("After removing:", my_list)

# Modifying elements
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print("After modifying list:", my_list)

# Searching elements
my_list = [10, 20, 30, 40, 50]
search = 40

if search in my_list:
    print(search, "found in the list")
else:
    print(search, "not found in the list")

# Sorting elements
my_list = [10, 20, 60, 30, 40, 25, 50]
my_list.sort()
print("After sorting:", my_list)

# Reversing elements
my_list = [10, 20, 30, 40, 50]
my_list.reverse()
print("Reversed list:", my_list)
