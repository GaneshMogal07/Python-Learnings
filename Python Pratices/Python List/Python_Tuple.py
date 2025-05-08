# Python Tuples - Examples for All Topics (with One-line Definitions)

# 1. Python Tuples - Tuples are used to store multiple items in a single variable (immutable)
my_tuple = (10, 20, 30, 40, 50)
print("1. Tuple:", my_tuple)

#output-(10,20,30,40,50)



# 2. Access Tuples - Access elements using index or slice
print("2. Access First Item:", my_tuple[0])
#output-(10)
print("   Access Last Item:", my_tuple[-1])
#output-(50)



# 3. Update Tuples - Convert to list, modify, then convert back (since tuples are immutable)
temp_list = list(my_tuple)
temp_list[1] = 25
my_tuple = tuple(temp_list)
print("3. Updated Tuple:", my_tuple)
#output-Updated Tuple: (10, 25, 30, 40, 50)



# 4. Unpack Tuples - Assign each tuple value to a variable
a, b, c, d, e = my_tuple
print("4. Unpacked Values:", a, b, c, d, e)
#output-Unpacked Values: 10 25 30 40 50



# 5. Loop Tuples - Use a loop to iterate through tuple items
print("5. Looping Through Tuple:")
for item in my_tuple:
    print("  ", item)
    
    

# 6. Join Tuples - Combine two or more tuples using +
tuple2 = (60, 70)
joined_tuple = my_tuple + tuple2
print("6. Joined Tuple:", joined_tuple)



# 7. Tuple Methods - Built-in functions like count() and index()
print("7. Count of 25:", my_tuple.count(25))
print("   Index of 40:", my_tuple.index(40))



# 8. Tuple Exercises - Practice task: Filter and print items greater than 30
filtered = tuple(x for x in my_tuple if x > 30)
print("8. Items > 30:", filtered)



# output-

# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python List> python python_Tuple.py
# 1. Tuple: (10, 20, 30, 40, 50)
# 2. Access First Item: 10
#    Access Last Item: 50
# 3. Updated Tuple: (10, 25, 30, 40, 50)
# 4. Unpacked Values: 10 25 30 40 50
# 5. Looping Through Tuple:
#    10
#    25
#    30
#    40
#    50
# 6. Joined Tuple: (10, 25, 30, 40, 50, 60, 70)
# 7. Count of 25: 1
#    Index of 40: 3
# 8. Items > 30: (40, 50)
