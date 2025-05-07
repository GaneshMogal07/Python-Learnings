# # This Not correct saynhax for string formats.

age = 36
txt = "My name is John, I am " + age
print(txt)



# output-
#  C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python Strings> python Formatstring.py
# Traceback (most recent call last):
#   File "Formatstring.py", line 2, in <module>
#     txt = "My name is John, I am " + age
# TypeError: can only concatenate str (not "int") to str




age=36
txt = f" My name is Ganesh {age}"
print(txt)

# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python Strings> python Formatstring.py
#  My name is Ganesh 36


price = 20000
txt = f"this my rent ammount {price:.2f}"
print(txt)
# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python Strings> python Formatstring.py
# this my rent ammount 20000.00



