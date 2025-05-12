# 1. Access Items – Use square brackets or get() to access dictionary values.
my_dict = {"name": "Alice", "age": 25}
print("Access Items:", my_dict["name"], my_dict.get("age"))
print()

# 2. Change Items – Assign a new value to an existing key.
my_dict["age"] = 26
print("Change Items:", my_dict)
print()

# 3. Add Items – Add a new key-value pair to the dictionary.
my_dict["city"] = "Pune"
print("Add Items:", my_dict)
print()




# 4. Remove Items – Use pop(), del, or popitem() to remove items.
my_dict.pop("city")  # Removes 'city'
del my_dict["age"]   # Removes 'age'
print("Remove Items (after pop and del):", my_dict)
print()



# 5. Loop Dictionaries – Use a for loop to iterate over keys, values, or both.
my_dict = {"name": "Alice", "age": 25, "city": "Pune"}
print("Loop Keys:")
for key in my_dict:
    print(key)
print("Loop Values:")
for value in my_dict.values():
    print(value)
print("Loop Items:")
for key, value in my_dict.items():
    print(key, "->", value)
print()

# 6. Copy Dictionaries – Use copy() or dict() to make a copy of a dictionary.
new_dict = my_dict.copy()
alt_dict = dict(my_dict)
print("Copy Dictionaries:", new_dict, alt_dict)
print()

# 7. Nested Dictionaries – A dictionary inside another dictionary.
family = {
    "child1": {"name": "Max", "age": 5},
    "child2": {"name": "Lily", "age": 7}
}
print("Nested Dictionaries:", family)
print()

# 8. Dictionary Methods – Use built-in methods like keys(), values(), items(), update(), pop(), etc.
print("Dictionary Methods:")
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
my_dict.update({"country": "India"})
print("Updated Dictionary:", my_dict)
print()

# 9. Dictionary Exercises – Practice using all dictionary features together.
student1 = {"name": "John", "score": 85}
student2 = {"name": "Emma", "score": 90}
classroom = {"student1": student1, "student2": student2}
print("Dictionary Exercises - Nested Class Info:", classroom)



'''output-
Access Items: Alice 25

Change Items: {'name': 'Alice', 'age': 26}

Add Items: {'name': 'Alice', 'age': 26, 'city': 'Pune'}

Remove Items (after pop and del): {'name': 'Alice'}

Loop Keys:
name
age
city
Loop Values:
Alice
25
Pune
Loop Items:
name -> Alice
age -> 25
city -> Pune

Copy Dictionaries: {'name': 'Alice', 'age': 25, 'city': 'Pune'} {'name': 'Alice', 'age': 25, 'city': 'Pune'}

Nested Dictionaries: {'child1': {'name': 'Max', 'age': 5}, 'child2': {'name': 'Lily', 'age': 7}}

Dictionary Methods:
Keys: dict_keys(['name', 'age', 'city'])
Values: dict_values(['Alice', 25, 'Pune'])
Items: dict_items([('name', 'Alice'), ('age', 25), ('city', 'Pune')])
Updated Dictionary: {'name': 'Alice', 'age': 25, 'city': 'Pune', 'country': 'India'}

Dictionary Exercises - Nested Class Info: {'student1': {'name': 'John', 'score': 85}, 'student2': {'name': 'Emma', 'score': 90}}'''
