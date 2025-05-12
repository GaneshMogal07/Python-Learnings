def my_function():
  print("Hello from a function")

my_function()


def ganesh():
  print("i am ganesh mogal from shirdi")
  
ganesh()
  
def test(a,b):
 print(a+b)
 print(a-b)
 print(a*b)

test(10,21)


'''output-
PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Function> python Creatingfunction.py
31
-11
210'''

   
   
    
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#'''output-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python Function> python Creatingfunction.py
# 15
# 25
# 45'''




def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)