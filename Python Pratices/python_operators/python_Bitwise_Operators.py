# Bitwise Operators Examples

a = 10  # In binary: 1010
b = 4   # In binary: 0100

# 1. & (AND)
# Definition: Performs bitwise AND on each bit
print("1. a & b → " + str(a & b))  # 1010 & 0100 = 0000 0100 = 4

# 2. | (OR)
# Definition: Performs bitwise OR on each bit
print("2. a | b → " + str(a | b))  # 1010 | 0100 = 1110 = 14

# 3. ^ (XOR)
# Definition: Performs bitwise XOR on each bit (1 if bits are different)
print("3. a ^ b → " + str(a ^ b))  # 1010 ^ 0100 = 1110 = 14

# 4. ~ (NOT)
# Definition: Inverts all the bits (returns -(n+1))
print("4. ~a → " + str(~a))        # ~10 = -(10 + 1) = -11

# 5. << (Left Shift)
# Definition: Shifts bits to the left, adding zeros on the right
print("5. a << 2 → " + str(a << 2))  # 1010 << 2 = 101000 = 40

# 6. >> (Right Shift)
# Definition: Shifts bits to the right, dropping bits on the right
print("6. a >> 2 → " + str(a >> 2))  # 1010 >> 2 = 0010 = 2



# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python_operators> python python_Bitwise_Operators.py
# 1. a & b → 0
# 2. a | b → 14
# 3. a ^ b → 14
# 4. ~a → -11
# 5. a << 2 → 40
# 6. a >> 2 → 2