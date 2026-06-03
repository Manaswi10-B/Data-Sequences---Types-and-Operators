#Creating a tuple
my_tuple=(10,20,30,40,50)
print("Original Tuple:",my_tuple)

#Accessing elements
my_tuple=(10,20,30,40,50)
print("First Element:",my_tuple[0])
print("Last Element:",my_tuple[4])

#Index
my_tuple=(10,20,30,40,50)
print("Index of 40 is:",my_tuple.index(40))

#Slicing
my_tuple=(10,20,30,40,50)
print("Elements from 0-3:",my_tuple[0:3])
print("Element from 2-4:",my_tuple[2:4])

#Concatentaion
my_tuple1 = (10, 20, 30)
my_tuple2 = (40, 50, 60)
new_tuple = my_tuple1 + my_tuple2
print("After Concatenation:", new_tuple)

#Deleting
temp_tuple = (10,20,30,40,50,60)
print("Tuple before deletion:", temp_tuple)

del temp_tuple
print("Tuple deleted successfully.")

#Nested tuple
# Nested Tuples
nested_tuple = ((10, 20, 30), (40, 50, 60), (70, 80, 90))

print("Nested Tuple:", nested_tuple)
print("First Tuple:", nested_tuple[0])
print("Second Tuple:", nested_tuple[1])
print("Element 60:", nested_tuple[1][2])