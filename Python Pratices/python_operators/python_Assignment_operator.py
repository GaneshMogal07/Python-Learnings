# Assignment Operators Examples with Definitions

# 1. = (Assign)
# Definition: Assigns the value on the right to the variable on the left.
a = 10
print("1. '=' (Assign): a = 10 → a =", a)

# 2. += (Add and Assign)
# Definition: Adds the right operand to the left and assigns the result to the left operand.
a += 5  # a = a + 5
print("2. '+=' (Add and Assign): a += 5 → a =", a)

# 3. -= (Subtract and Assign)
# Definition: Subtracts the right operand from the left and assigns the result to the left operand.
a -= 3  # a = a - 3
print("3. '-=' (Subtract and Assign): a -= 3 → a =", a)

# 4. *= (Multiply and Assign)
# Definition: Multiplies the left operand by the right and assigns the result to the left operand.
a *= 2  # a = a * 2
print("4. '*=' (Multiply and Assign): a *= 2 → a =", a)

# 5. /= (Divide and Assign)
# Definition: Divides the left operand by the right and assigns the result (float) to the left operand.
a /= 4  # a = a / 4
print("5. '/=' (Divide and Assign): a /= 4 → a =", a)

# 6. %= (Modulus and Assign)
# Definition: Takes modulus using the right operand and assigns the result to the left operand.
a %= 3  # a = a % 3
print("6. '%=' (Modulus and Assign): a %= 3 → a =", a)

# Reset a for further examples
a = 10

# 7. //= (Floor Divide and Assign)
# Definition: Performs floor division and assigns the result (integer division) to the left operand.
a //= 3  # a = a // 3
print("7. '//=' (Floor Divide and Assign): a //= 3 → a =", a)

# Reset a for exponent example
a = 2

# 8. **= (Exponent and Assign)
# Definition: Raises the left operand to the power of the right and assigns the result.
a **= 4  # a = a **  4     3*3
print("8. '**=' (Exponent and Assign): a **= 4 → a =", a)






# Output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python_operators> python python_Assignment_operator.py
# 1. a = 10 → 10
# 2. a += 5 → 15
# 3. a -= 3 → 12
# 4. a *= 2 → 24
# 5. a /= 4 → 6.0
# 6. a %= 3 → 0.0
# 7. a //= 3 → 3
# 8. a **= 4 → 16
