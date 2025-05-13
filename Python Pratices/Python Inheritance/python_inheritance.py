class Parent:
    def greet(self):
        print("Hello from Parent class")

class Child(Parent):  # Inheriting from Parent
    def display(self):
        print("This is Child class")

# Creating object of Child
c = Child()
c.greet()     # Accessing method from Parent
c.display()   # Accessing method from Child


# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Inheritance> python python_inheritance.py
# Hello from Parent class
# This is Child class




class demo:
    def ganesh(test):
        print("i am ganesh mogal")

class demo1(demo):
    def display(test):
        print("i am from shirdi") 

c = demo1()
c.ganesh()
c.display()


# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Inheritance> python python_inheritance.py
# i am ganesh mogal
# i am from shirdi
               