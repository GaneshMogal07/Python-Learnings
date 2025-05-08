# Python Lists - Examples for All Topics (with One-line Definitions)

# 1. Python Lists - Used to store multiple items in a single variable
my_list = [10, 20, 30, 40, 50]
print("1. Python List:", my_list)

# 2. Access List Items - Access items using index or slice
print("2. Access First Item:", my_list[0])
print("   Access Last Item:", my_list[-1])

# 3. Change List Items - Modify an element by index
my_list[1] = 25
print("3. Change Second Item:", my_list)

# 4. Add List Items - Use 
# append()- apppend is used for add the element of the list  .
# insert(), or extend()
my_list.append(60)
my_list.insert(2, 22)
print("4. Add Items:", my_list)

# 5. Remove List Items - Use remove(), 
# pop()- pop is removes last item, or del
my_list.remove(40)  # Remove by value
popped_item = my_list.pop()  # Remove last item
print("5. Remove Items:", my_list, "| Popped:", popped_item)

# 6. Loop Lists - Iterate using for or while loop
print("6. Looping List:")
for item in my_list:
    print("  ", item)

# 7. List Comprehension - Create list using single-line for loop
squares = [x * x for x in range(1, 6)]
print("7. List Comprehension (Squares):", squares)

# 8. Sort Lists - Arrange items in ascending/descending order
unsorted_list = [3, 1, 4, 2, 5]
unsorted_list.sort()
print("8. Sorted List:", unsorted_list)

# 9. Copy Lists - Use copy(), slicing, or list()
copy_list = my_list.copy()
print("9. Copied List:", copy_list)

# 10. Join Lists - Combine lists using + or extend()
combined = my_list + copy_list
print("10. Joined Lists:", combined)

# 11. List Methods - Built-in functions to manipulate lists
print("11. Index of 25:", my_list.index(25))
print("    Count of 10:", my_list.count(10))

# 12. List Exercises - Practice problems using lists
# Task: Double all even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]
print("12. Doubled Even Numbers:", doubled_evens)





# output-

# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python List> python python_list.py
# 1. Python List: [10, 20, 30, 40, 50]
# 2. Access First Item: 10
#    Access Last Item: 50
# 3. Change Second Item: [10, 25, 30, 40, 50]
# 4. Add Items: [10, 25, 22, 30, 40, 50, 60]
# 5. Remove Items: [10, 25, 22, 30, 50] | Popped: 60
# 6. Looping List:
#    10
#    25
#    22
#    30
#    50
# 7. List Comprehension (Squares): [1, 4, 9, 16, 25]
# 8. Sorted List: [1, 2, 3, 4, 5]
# 9. Copied List: [10, 25, 22, 30, 50]
# 10. Joined Lists: [10, 25, 22, 30, 50, 10, 25, 22, 30, 50]
# 11. Index of 25: 1
#     Count of 10: 1
# 12. Doubled Even Numbers: [4, 8, 12]
