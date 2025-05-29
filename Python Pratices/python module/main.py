import mymodule
mymodule.say_hello()  # Hello

result1 = mymodule.add(10, 5)

result2 = mymodule.sub(10, 5)

print("Addition:", result1)
print("substarction :", result2)


#Using the dir() Function
#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

x = dir(mymodule)
print("dir fuction :",x)

#output:-
#PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\python module> python main.py
#ganesh mogal i am shirdi
#Addition: 15
#substarction : 5
#dir fuction : ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'say_hello', 'sub'] 
