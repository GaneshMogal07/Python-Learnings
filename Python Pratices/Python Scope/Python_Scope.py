#  What is Scope in Python?
# Scope refers to where a variable is accessible in your code. In Python, scope defines the visibility and lifetime of variables.

# 🔑 Python Uses the LEGB Rule:
# Level	     Meaning	                       Description
# L	         Local	         Inside the current function
# E	       Enclosing	     In the outer function (for nested functions)
# G	        Global	         At the top level of the script/module
# B	        Built-in	     Python's built-in names like print, len, etc.


# 1. Global Scope
# Definition:
# Variable declared outside any function, accessible anywhere in the program.

# Real-Life Example:
# Like your mobile balance – you can check it from anywhere.


balance = 1000  # Declared outside any function

def show_balance():
    print("Your balance is:", balance)  # Accessible inside function

show_balance()
print("Outside function access:", balance)

# Output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python scope> python python_scope.py
# Your balance is: 1000
# Outside function access: 1000




# 2. Local Scope
# 📘 Definition:
# Variable declared inside a function, only accessible within that function.

# Real-Life Example:
# Like a password stored inside an app not accessible globally.


def use_password():
    password = "1234"  # Local variable
    print("Inside function - Password is:", password)

use_password()
# print(password)  #Error: password is not accessible outside

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python scope> python python_scope.py
# Inside function - Password is: 1234




# 3. Enclosing Scope (Nested Functions)
# Definition:
# Variables defined in outer (enclosing) function, accessible by inner function.

# Real-Life Example:
# Inner room can use light switch of the outer room.


def outer_room():
    light = "Outer Light"  # Enclosing scope

    def inner_room():
        print("Inner room using:", light)  # Can access outer variable

    inner_room()

outer_room()

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python scope> python python_scope.py
# Inner room using: Outer Light





# 4. Built-in Scope
# Definition:
# Predefined names in Python, like print(), len(), etc.

# Real-Life Example:
# Ready-made tools given by Python.

a="ganesh"
print("Length of 'Ganesh' is:", len(a))

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python scope> python python_scope.py
# Length of 'Ganesh' is: 6

points = 10  # Global

def recharge():
    global points
    points = 100
    print("Inside function - Updated points:", points)

recharge()
print("Outside function - points now:", points)
