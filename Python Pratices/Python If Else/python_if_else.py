'''# Python If...Else Conditions with Examples

if condition:
    # code block if condition is True
elif another_condition:
    # code block if another condition is True
else:
    # code block if none of the conditions are True '''\
        
        

# Equals (==): Returns True if both values are equal
a = 5
b = 5
if a == b:
    print("a is equal to b") 
    

# Not Equals (!=): Returns True if values are not equal
a = 5
b = 3
if a != b:
    print("a is not equal to b")

# Less than (<): Returns True if left value is smaller
a = 3
b = 7
if a < b:
    print("a is less than b")

# Less than or equal to (<=): True if left value is smaller or equal
a = 7
b = 7
if a <= b:
    print("a is less than or equal to b")

# Greater than (>): Returns True if left value is greater
a = 10
b = 5
if a > b:
    print("a is greater than b")

# Greater than or equal to (>=): True if left value is greater or equal
a = 10
b = 10
if a >= b:
    print("a is greater than or equal to b")

# Full example using if, elif, and else
a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")
    
    
    
    
    
    
    '''output-
    PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python If Else> python python_if_else.py
b is not eual to a
a is not equal to b
a is less than b
a is less than or equal to b
a is greater than b
a is greater than or equal to b
a is less than b'''

