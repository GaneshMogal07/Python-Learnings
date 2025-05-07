# Identity Operators Examples

a = [1, 2, 3]
b = a        # b refers to the same object as a
c = [1, 2, 3]  # c is a separate object with the same content

# 1. is
# Definition: Returns True if both variables point to the same object (same memory location)
print("1. a is b → " + str(a is b))  # True
print("2. a is c → " + str(a is c))  # False

# 2. is not
# Definition: Returns True if both variables do NOT point to the same object
print("3. a is not b → " + str(a is not b))  # False
print("4. a is not c → " + str(a is not c))  # True



# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python_operators> python python_identity_Operators.py
# 1. a is b → True
# 2. a is c → False
# 3. a is not b → False
# 4. a is not c → True
