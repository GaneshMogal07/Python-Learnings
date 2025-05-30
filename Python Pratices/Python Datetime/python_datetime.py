# Python Dates:-
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime

x = datetime.datetime.now()  # Get current date and time
print(x)

print("Current date and time:", x)

# Print date only
print("Today's date is:", x.date())

# Print time only
print("Current time is:", x.time())


# #output:-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Datetime> python python_datetime.py
# 2025-05-29 11:02:47.336122
# Current date and time: 2025-05-29 11:02:47.336122
# Today's date is: 2025-05-29
# Current time is: 11:02:47.336122

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# output:-
# 2025
# Thursday