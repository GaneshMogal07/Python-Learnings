# Method	Description - 

# capitalize() -	Converts the first character to upper case
# casefold() -	Converts string into lower case
# center() - 	Returns a centered string
# count()	- Returns the number of times a specified value occurs in a string
# encode()-	Returns an encoded version of the string
# endswith() -Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning




text = "  hello world! 123\t\n"

print("capitalize():", text.capitalize())
print("casefold():", text.casefold())
print("center():", text.center(30, "-"))
print("count():", text.count("l"))
print("encode():", text.encode())
print("endswith():", text.endswith("3\t\n"))
print("expandtabs():", text.expandtabs(4))
print("find():", text.find("world"))
print("format():", "Welcome, {}!".format("User"))
print("format_map():", "{name} is {age} years old.".format_map({'name': 'John', 'age': 30}))
print("index():", text.index("world"))
print("isalnum():", "Hello123".isalnum())
print("isalpha():", "Hello".isalpha())
print("isascii():", "Hello".isascii())
print("isdecimal():", "123".isdecimal())
print("isdigit():", "123".isdigit())
print("isidentifier():", "hello_world".isidentifier())
print("islower():", "hello".islower())
print("isnumeric():", "123".isnumeric())
print("isprintable():", "Hello\nWorld".isprintable())
print("isspace():", "   ".isspace())
print("istitle():", "Hello World".istitle())
print("isupper():", "HELLO".isupper())
print("join():", "-".join(["a", "b", "c"]))
print("ljust():", "Hi".ljust(10, "."))
print("lower():", "HELLO".lower())
print("lstrip():", text.lstrip())
print("maketrans() + translate():", "apple".translate(str.maketrans("ae", "12")))
print("partition():", text.partition("world"))
print("replace():", text.replace("world", "Python"))
print("rfind():", text.rfind("l"))
print("rindex():", text.rindex("l"))
print("rjust():", "Hi".rjust(10, "."))
print("rpartition():", text.rpartition(" "))
print("rsplit():", "a,b,c".rsplit(",", 1))
print("rstrip():", text.rstrip())
print("split():", text.split())
print("splitlines():", "Hello\nWorld".splitlines())
print("startswith():", text.startswith("  hello"))
print("strip():", text.strip())
print("swapcase():", "Hello".swapcase())
print("title():", "hello world".title())
print("upper():", "hello".upper())
print("zfill():", "42".zfill(5))
