# 1. Create and Access Dictionary Elements
student = {
    "name": "Snehal",
    "age": 20,
    "course": "Computer Engineering"
}

print("Original Dictionary:", student)

# Access elements
print("Name:", student["name"])
print("Age:", student.get("age"))


# 2. Update Dictionary
student["age"] = 21              # Update existing value
student["city"] = "Nashik"       # Add new key-value pair

print("\nAfter Updating:", student)


# 3. Removing Elements
student.pop("course")            # Remove specific key
# student.clear()                # Uncomment to remove all elements

print("\nAfter Removing 'course':", student)


# 4. Merging Dictionaries
extra_info = {
    "grade": "A",
    "status": "Active"
}

# Method 1: Using update()
student.update(extra_info)

print("\nAfter Merging (using update):", student)

# Method 2: Using unpacking (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}

print("\nMerged Dictionary (using **):", merged_dict)