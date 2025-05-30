# Python Try Except
# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("You must enter a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Success! Result is:", result)
finally:
    print("This block always runs (cleanup, closing files, etc).")
    
    
    
# output:-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Try Except> python python_try_Except.py
# Enter a number: 2
# Success! Result is: 5.0
# This block always runs (cleanup, closing files, etc).
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Try Except>    
