# Python JSON :- 
# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

# Import the json module:
#example package is :-
# import json

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



xx ={
    "name":"ganesh",
    "city":"pune",
    "Location":"shirdi",
    "phone Number": 9511951568
    
}
print(xx)

# output:-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python JSON> python Python_json.py 
# 30
# {'name': 'ganesh', 'city': 'pune', 'Location': 'shirdi', 'phone Number': 9511951568}





# 2.Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


import json

# a Python object (dict):
x = {
  "name": 'John',
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# output:-
# {"name": "John", "age": 30, "city": "New York"}





import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


# output:-
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}







