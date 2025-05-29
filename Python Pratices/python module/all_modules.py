# 1.Built-in Module:
# Pre-installed module provided by Python.
# Example:

import math  # For math operations
print(math.sqrt(25))  # 5.0

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python module> python all_modules.py
# 5.0



#  2.User-defined Module:
# A custom .py file you create and import.
# Example:
# mymodule.py
def say_hello(): print("ganesh mogal i am shirdi")

# main.py
import mymodule
mymodule.say_hello()  # ganesh mogal i am shirdi

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python module> python main.py
# ganesh mogal i am shirdi



def add(a,b):
    return a + b