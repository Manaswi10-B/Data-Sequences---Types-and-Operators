# Creating a Dictionary
my_dict = {
    "Name": "Manaswi",
    "Age": 18,
    "City": "Pune"
}
print("Original Dictionary:", my_dict)

# Accessing a Dictionary
print("Name:", my_dict["Name"])
print("Age:", my_dict["Age"])

# Adding Elements
my_dict["Course"] = "AI and Analytics"
print("After Adding Element:", my_dict)

# Removing Elements
my_dict.pop("City")
print("After Removing Element:", my_dict)

# Accessing Keys
print("Keys:", my_dict.keys())

# Accessing Values
print("Values:", my_dict.values())

# Index
print("Dictionaries do not support indexing.")

# Ordered
print("Dictionaries are ordered in Python 3.7 and later versions.")

# Duplicate Keys
my_dict = {
    "Name": "Manaswi",
    "Age": 18,
    "Age": 20
}
print("Dictionary with Duplicate Key:", my_dict)
print("Duplicate keys are not allowed. The last value is kept.")