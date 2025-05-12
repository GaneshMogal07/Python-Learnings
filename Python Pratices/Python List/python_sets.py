# 1. Access Set Items – You can loop through a set using a for loop because sets do not support indexing.
my_set = {"apple", "banana", "cherry"}
print("Access Set Items:")
for item in my_set:
    print(item)
print()

# 2. Add Set Items – Use add() to insert a single item and update() to add multiple items to a set.
my_set = {"apple", "banana"}
my_set.add("cherry")  # Adds one item
my_set.update(["orange", "mango"])  # Adds multiple items
print("Add Set Items:", my_set)
print()



# 3. Remove Set Items – Use remove(), discard(), or pop() to delete items from a set.
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")  # Removes 'banana'
my_set.discard("cherry")  # Removes 'cherry'
# my_set.remove("mango")  # Would raise an error if uncommented
my_set.pop()  # Removes a random item
print("Remove Set Items:", my_set)
print()



# 4. Loop Sets – Looping through a set is done using for item in set: to access each element.
my_set = {"apple", "banana", "cherry"}
print("Loop Sets:")
for fruit in my_set:
    print(fruit)
print()

# 5. Join Sets – Combine sets using union(), update(), or operators like |.
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
print("Join Sets (union):", set1.union(set2))  # Combines all elements
set1.update(set2)  # Adds elements from set2 to set1
print("Join Sets (update):", set1)
print()

# 6. Set Methods – Python provides built-in methods like copy(), difference(), intersection(), issubset(), and more.
my_set = {1, 2, 3}
print("Set Methods:")
print("Copy:", my_set.copy())                          # Copy the set
print("Difference:", my_set.difference({2, 3, 4}))     # {1}
print("Intersection:", my_set.intersection({2, 3, 4})) # {2, 3}
print("Is Disjoint:", my_set.isdisjoint({4, 5}))       # True
print("Is Subset:", my_set.issubset({1, 2, 3, 4}))     # True
print("Is Superset:", my_set.issuperset({1, 2}))       # True
print()

# 7. Set Exercises – Practice problems help reinforce understanding of set operations and behavior.
even = {2, 4, 6, 8}
odd = {1, 3, 5, 7}
print("Set Exercises:")
print("All numbers (union):", even.union(odd))             # All numbers without duplicates
print("Common numbers (intersection):", even.intersection(odd))  # Should be empty



"""output-
PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python List> python python_sets.py
Access Set Items:
banana
cherry
apple

Add Set Items: {'orange', 'apple', 'banana', 'mango', 'cherry'}

Remove Set Items: set()

Loop Sets:
banana
cherry
apple

Join Sets (union): {'e', 'b', 'a', 'c', 'd'}
Join Sets (update): {'e', 'b', 'a', 'c', 'd'}

Set Methods:
Copy: {1, 2, 3}
Difference: {1}
Intersection: {2, 3}
Is Disjoint: True
Is Subset: True
Is Superset: True

Set Exercises:
All numbers (union): {1, 2, 3, 4, 5, 6, 7, 8}
Common numbers (intersection): set() """






