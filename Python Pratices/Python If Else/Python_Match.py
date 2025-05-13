#The match statement is used to perform different actions based on different conditions.

# match is available only from Python 3.10+.
# The _ pattern works as a default case.

'''match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block'''
    
#Example
day = 4

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")
    
    # output- 
    # PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python if Else> python Python_Match.py
    # Thursday
    
    
    
    # Match example in Python 3.10+
command = "start"

if command == "start":
    print("Starting the engine...")
elif command == "stop":
    print("Stopping the engine...")
elif command == "pause":
    print("Pausing the engine...")
else:
    print("Unknown command")
    
# output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python if Else> python Python_Match.py
# Thursday
# Starting the engine...


test = "go"

if test == "run the first line":
    print("final you can set the process")
    
elif test == "go":
    print("done")   
    
    # output-
    # done 





    
    
    
