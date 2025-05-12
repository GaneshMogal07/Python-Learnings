'''What is a Lambda Function in Python?
A lambda function in Python is a small anonymous function — meaning, it doesn't have a name like regular functions defined using def.

Syntax:
lambda arguments: expression

1.You can have multiple arguments.
2.You can have only one expression (no statements, loops, etc.).
3.It's mainly used for short, simple functions, especially as arguments to other functions like map(), filter(), sorted(), etc.'''



x = lambda a : a + 10
print(x(5))

# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Lambda Function> python Lambda_Function.py
# 15

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Lambda Function> python Lambda_Function.py
# 8


test = lambda x ,y: x*y
print(test(10,5))

# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Lambda Function> python Lambda_Function.py
# 50


test = lambda x,y,z : x*y+z
print(test(100,200,2))



# When to Use Lambda Functions?
# When you need a short function for a short time.

# Useful with functional tools like map(), filter(), reduce(), and sorted().



from functools import reduce

# map: double each number
doubled = list(map(lambda x: x * 2, [1, 2, 3, 4]))

# filter: keep even numbers
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))

# reduce: multiply all numbers
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])

# sorted: sort list of tuples by second element
sorted_tuples = sorted([(1, 'b'), (3, 'a'), (2, 'c')], key=lambda x: x[1])

# print all results
print("Doubled (map):", doubled)
print("Even numbers (filter):", evens)
print("Product (reduce):", product)
print("Sorted tuples (sorted):", sorted_tuples)

# output-
# Doubled (map): [2, 4, 6, 8]
# Even numbers (filter): [2, 4]
# Product (reduce): 24
# Sorted tuples (sorted): [(3, 'a'), (1, 'b'), (2, 'c')]
