# ✅ What is input() in Python?
# In Python, the built-in function input() is used to take input from the user.

# By default, the input is always returned as a string.


name = input("Enter your name: ")
age = int(input("Enter your age: "))
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price

print(f"\nInvoice for {name} (Age {age}):")
print(f"Product: {product}")
print(f"Quantity: {quantity}")
print(f"Price per item: ₹{price}")
print(f"Total cost: ₹{total}")


# output:-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python User Input> python Python_User_Input.py
# Enter your name: ganesh
# Enter your age: 21
# Enter product name: hrms
# Enter quantity: 11
# Enter price per item: 12

# Invoice for ganesh (Age 21):
# Product: hrms
# Quantity: 11
# Price per item: ₹12.0
# Total cost: ₹132.0
