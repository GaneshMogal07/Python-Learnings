# What is Polymorphism?
# Polymorphism means "many forms".
# In Python, polymorphism allows the same function or method name to behave differently depending on the object.

# Types of Polymorphism in Python
# 1.Duck Typing (Dynamic Typing)
# 2.Operator Overloading
# 3.Method Overriding (Inheritance-based Polymorphism)
# 4.Function Overloading (using default arguments or *args)


# 1. Duck Typing (Pythonic Polymorphism)
# “If it walks like a duck and quacks like a duck, it's a duck.”
# Example:

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

def animal_sound(animal):
    animal.speak()  # No matter what type, it works if it has a 'speak' method

c = Cat()
d = Dog()

animal_sound(c)
animal_sound(d)


# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Polymorphism> python Python_Polymorphism.py
# Meow
# Woof


# 2. Operator Overloading
# You can define how operators like +, -, * behave for your own class.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print("Total pages:", b1 + b2)  # Uses overloaded +

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Polymorphism> python Python_Polymorphism.py
# Meow
# Woof
# Total pages: 300




# 3. Method Overriding (Inheritance)
# When child class defines the same method as the parent, it's called overriding.


class Vehicle:
    def show(self):
        print("I am a vehicle")

class Car(Vehicle):
    def show(self):
        print("I am a car")

v = Vehicle()
c = Car()

v.show()
c.show()  # Overridden version


# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Polymorphism> python Python_Polymorphism.py
# I am a vehicle
# I am a car




# 4. Function Overloading (using default arguments)
# Python doesn't support traditional function overloading, but we can simulate it.

def add(a=0, b=0, c=0):
    return a + b + c

print(add(2, 3))      # 5
print(add(2, 3, 4))   # 9



# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Polymorphism> python Python_Polymorphism.py
# 5
# 9
