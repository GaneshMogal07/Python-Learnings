# for Loop
# 📌 Definition:
# Used to iterate over a sequence like a list, tuple, string, or range.

# for i in range(1, 6):
#     print(i)


# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python  Loops> python for_loop.py
# 1
# 2
# 3
# 4
# 5

# break: Stop the loop.
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
    
    
# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python  Loops> python for_loop.py
# 1
# 2




# continue: Skip the current iteration.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
# '''output-
# # PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python  Loops> python for_loop.py
# 1
# 2
# 4
# 5
# '''


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python  Loops> python for_loop.py
# apple