# ✅ What is a Class?
# A class is like a template or blueprint to create objects.

# It defines properties (variables) and behaviors (methods).


class first:
    x = 50

obj = first()
print(obj.x)  # Output: 50

# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Classes and Objects> python python_class.py
# 50



class demo:
    x = 50
    y = 30

obj1 = demo()
print(obj1.x + obj1.y)

# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Classes and Objects> python python_class.py
# 80



class faculty:
    def putdata(self):  # method1: to input data
        self.id = int(input("enter faculty id"))
        self.name = input("enter name")
        self.salary = float(input("enter faculty salary"))

    def display(self):  # method2: to display data
        print("faculty id:", self.id)
        print("faculty name:", self.name)
        print("faculty salary", self.salary)


a = faculty()      # create an object of the class
a.putdata()        # call method to enter data
a.display()        # call method to display data


'''PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Classes and Objects> python python_class.py
enter faculty id201
enter nameganesh
enter faculty salary30000.7
faculty id: 201
faculty name: ganesh
faculty salary 30000.7'''


# explanation-

# Simple Explanation:
# Part	What It Does
# class faculty:	Creates a new class named faculty. Think of this like a blueprint.
# def putdata(self):	This function (method) asks the user to enter faculty details.
# self.id	Saves the faculty ID entered by the user.
# self.name	Saves the faculty name entered by the user.
# self.salary	Saves the faculty salary entered by the user.
# def display(self):	This function shows the entered details on the screen.
# a = faculty()	Creates a new object a of class faculty.
# a.putdata()	Calls the function to ask user to enter data.
# a.display()	Calls the function to show entered data.

 