# Python String Formatting
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# Before Python 3.6 we had to use the format() method.

name = "Ganesh"
age = 25
price = 49.45678
product = "USB Cable"
quantity = 3

# 1. f-string formatting
print(f"My name is {name} and I am {age} years old.")

# 2. format() method
print("Product: {} | Quantity: {} | Price per item: {:.2f}".format(product, quantity, price))

# 3. Old-style formatting (% operator)
print("Hello %s, you bought %d %s(s)." % (name, quantity, product))

# 4. Alignment and padding
print(f"{'Item':<10} {'Qty':^5} {'Price':>10}")
print(f"{product:<10} {quantity:^5} {price:>10.2f}")

# 5. Padding numbers with leading zeros
invoice_number = 7
print(f"Invoice No: {invoice_number:03}")  # Output: Invoice No: 007



# output:-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python String Formatting> python python_string_formatting.py
# My name is Ganesh and I am 25 years old.
# Product: USB Cable | Quantity: 3 | Price per item: 49.46
# Hello Ganesh, you bought 3 USB Cable(s).
# Item        Qty       Price
# USB Cable    3        49.46
# Invoice No: 007
