#  What is RegEx?
# RegEx (short for Regular Expression) is a sequence of characters that defines a search pattern.
# Used for:

# Searching

# Matching

# Replacing patterns in text

# Python provides the re module to work with RegEx.

# most important is firs you can import the module  - re 

# 1 Searching
import re

text = "My name is Ganesh and my number is 9876543210."

# Check if the string contains a 10-digit mobile number
match = re.search(r"\d{10}", text)

if match:
    print("Phone number found:", match.group())
else:
    print("Phone number not found.")
    
    
# output:-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python RegEx> python Python_RegEx.py
# Phone number found: 9876543210




# 2 Matching :- 

text = "Ganesh is 25 years old. Email: ganesh@example.com"

# 1. Find all digits
print(re.findall(r"\d+", text))  # ['25']

# 2. Check if line starts with "Ganesh"
print(re.match(r"Ganesh", text))  # Match object

# 3. Replace email with [hidden]
print(re.sub(r"\S+@\S+", "[hidden]", text))


# output:-
# PS C:\Users\GaneshMogal\Python-Learnings\Python Pratices\Python RegEx> python Python_RegEx.py
# Phone number found: 9876543210
# ['25']
# <re.Match object; span=(0, 6), match='Ganesh'>
# Ganesh is 25 years old. Email: [hidden]


'''

| Pattern | Description                    |    |
| ------- | ------------------------------ | -- |
| `\d`    | Digit (0–9)                    |    |
| `\D`    | Non-digit                      |    |
| `\w`    | Word character (a-z, A-Z, 0-9) |    |
| `\s`    | Space                          |    |
| `.`     | Any character except newline   |    |
| `^`     | Start of string                |    |
| `$`     | End of string                  |    |
| `+`     | One or more                    |    |
| `*`     | Zero or more                   |    |
| `{n}`   | Exactly n times                |    |
| \`      | \`                             | OR |
| `[]`    | Set of characters              |    |'''




