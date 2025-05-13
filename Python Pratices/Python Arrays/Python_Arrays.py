# ✅ Short Explanation:-
# In Python, an array is a collection of items stored at contiguous memory locations. You can use:

# 1.List – the most common array-like structure in Python.

# 2.array module – for efficient storage of same data type elements.

# 3.NumPy – for large, multi-dimensional, and fast arrays.


# 1. ✅ Using Python List as an Array

import array

arr = array.array('i', [10, 20, 30, 40])

arr.append(50)           # Add element

arr.insert(1, 15)        # Insert at index 1
arr.remove(30)           # Remove value 30
arr.pop()                # Remove last
print(arr.index(20))     # Find index of 20
arr.reverse()            # Reverse array
print(arr.tolist())      # Convert to list
print(arr)


# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Arrays> python Python_Arrays.py
# 2
# [40, 20, 15, 10]
# array('i', [40, 20, 15, 10])





