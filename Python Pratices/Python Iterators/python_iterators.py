'''🔷 What is an Iterator in Python?
An iterator is an object that allows you to loop through (iterate) over a sequence (like list, tuple, string, etc.) 
one element at a time.

✅ Key Concepts:
Iterator must implement two methods:

__iter__() – returns the iterator object.
__next__() – returns the next item from the sequence.

🧱 Simple Example of an Iterator:
my_list = [10, 20, 30]
my_iter = iter(my_list)   # Get iterator

print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
# print(next(my_iter))  # This will raise StopIteration
👉 iter() is used to get the iterator, and next() gets each item.'''


# ---------------------------------------
# 1. Built-in Iterable (list) with iter() and next()
print("🔹 Built-in Iterable:")
my_list = [10, 20, 30]
my_iter = iter(my_list)

print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
# next(my_iter)  # Uncommenting this will raise StopIteration

# ---------------------------------------
# 2. For Loop uses iterator internally
print("\n🔹 For loop with Iterable:")
for item in [100, 200, 300]:
    print(item)

# ---------------------------------------
# 3. Behind the scenes of for loop (manual iteration)
print("\n🔹 Manual iteration (simulating for loop):")
numbers = [1, 2, 3]
it = iter(numbers)

while True:
    try:
        val = next(it)
        print(val)
    except StopIteration:
        break

# ---------------------------------------
# 4. Custom Iterator Class Example
print("\n🔹 Custom Iterator class:")

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

counter = Counter(1, 5)
for num in counter:
    print(num)

# ---------------------------------------
# 5. Iterator vs Iterable Check
print("\n🔹 Iterable vs Iterator:")

data = [7, 8, 9]
print("Is data iterable?", hasattr(data, '__iter__'))  # True
print("Is data iterator?", hasattr(data, '__next__'))  # False

it_obj = iter(data)
print("Is it_obj iterator?", hasattr(it_obj, '__next__'))  # True

print(next(it_obj))  # 7
print(next(it_obj))  # 8
print(next(it_obj))  # 9




'''output-
PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Iterators> python python_iterators.py
🔹 Built-in Iterable:
10
20
30

🔹 For loop with Iterable:
100
200
300

🔹 Manual iteration (simulating for loop):
1
2
3

🔹 Custom Iterator class:
1
2
3
4
5

🔹 Iterable vs Iterator:
Is data iterable? True
Is data iterator? False
Is it_obj iterator? True
7
8
9
'''