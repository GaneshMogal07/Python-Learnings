# 🔄 Types of Inheritance in Python:
# Type	-                  Description	                                            Example

# Single	 -   One child class inherits from one parent class                  	✅ Supported
# Multiple -	One child class inherits from multiple parents	                    ✅ Supported
# Multilevel -	Inheritance from a class that is already derived                	✅ Supported
# Hierarchical -	Multiple child classes inherit from a single parent	            ✅ Supported
# Hybrid   -	Combination of any of the above types	                                ✅ Supported




# 1.Single Inheritance Example-

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Inheritance> python python_inheritance_type.py
# Animal speaks
# Dog barks


# 2. Multiple Inheritance Example

class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):  # Inherits from both
    def own_skill(self):
        print("Child: Painting")

c = Child()
c.skills()     # Executes Father's skill due to Method Resolution Order (MRO)
c.own_skill()

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Inheritance> python python_inheritance_type.py
# Father: Gardening
# Child: Painting


# 3.Multilevel Inheritance Example-


class Grandparent:
    def family(self):
        print("Grandparent: Values")

class Parent(Grandparent):
    def house(self):
        print("Parent: House")

class Child(Parent):
    def car(self):
        print("Child: Car")

c = Child()
c.family()
c.house()
c.car()

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Inheritance> python python_inheritance_type.py
# Grandparent: Values
# Parent: House
# Child: Car


# 4.Hierarchical Inheritance Example
class Parent:
    def home(self):
        print("Parent: House")

class Son(Parent):
    def bike(self):
        print("Son: Bike")

class Daughter(Parent):
    def scooty(self):
        print("Daughter: Scooty")

s = Son()
d = Daughter()
s.home(); s.bike()
d.home(); d.scooty()


# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Inheritance> python python_inheritance_type.py
# Parent: House
# Son: Bike
# Parent: House
# Daughter: Scooty

