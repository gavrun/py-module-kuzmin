# A string is an ordered, immutable sequence of Unicode characters

# 1. Convert a number to a string
x = str("s1") # x becomes 's1'
y = str(2) # y becomes '2'
z = str(3.0) # z becomes '3.0'
print(x, type(x), id(x)) # <class 'str'>
a = "Hello, World!"
print(a[1]) # р
# a[1] = 'л' # TypeError: 'str' object does not support item assignment

# 2. Arithmetic operations
# The result type of the operation is determined by the type of the arguments

# s1 + s2
# Concatenates the strings s1 and s2
print("Py" + "thon") # 'Python'
# or just write next to
print("Py" "thon") # 'Python'

# s1 * n
# Makes a string of n repetitions of the string s1
print("на" * 2) # 'папа'

# 3. Equality and comparison
# Result of a logical type
#
# Comparison operations are performed character by character from left to right, taking into account the encoding.
# Unicode character table at http://unicode-table.com/.

# s1 == s2, s1 != s2
# Checking strings for equality/inequality
print("text1" == "text2") # False
print("text1" != "text2") # True

# x > y, x < y, x >= y, x <= y
# Greater than, less than, greater than or equal to, less than or equal to
print("text1" > "text2") # False
print("text1" <= "text2") # True

# Comparison chains are possible
print("text1" < "text12" <= "text2") # True

# s1 in s2
# Checking if string s1 is in s2
print("p" in "Python") # False

# 4. Using string methods
""" Strings are immutable data type, so all methods that convert a string
return a new string, and the original string remains unchanged"""

s = "THIS IS JUST TEXT"
print(ord(s[0])) # 1069 - Returns the character number from the Unicode table
print(chr(1069)) # Э - Returns the character by number from the Unicode table

print(s.upper(), s.lower(), s.title(), s.capitalize(), s.swapcase())
# capitalize() Returns a copy of the string with the first character in uppercase
# title() Returns a copy of the string in which the first characters of each word are converted to uppercase, and all the rest are converted to lowercase.
# swapcase() Returns a copy of the string with the case reversed
# ('THIS IS JUST TEXT', 'this is just text', 'This is Just Text', 'This is just text', 'this is JUST TEXT')

print(s.find("T")) # 1 - position of the first character of the substring (for the first match)

print(s.replace("T", "t")) # 'THIS IS JUST TEXT'

lst1 = s.split() # Returns a list of strings split by the parameter string
print(lst1) # ['THIS', 'just', 'TEXT']

lst2 = s.split('T')
print(lst2) # ['Э', 'О прос', 'о ', 'еКст']
print("-o-".join(lst1)) # 'THIS-is-just-a-Text'

# Checking if a string starts or ends with certain characters
print(s.startswith('ET')) # True
print(s.endswith('st')) # True

b = """Let's write the first line
Now the second
48 is greater than three"""
print("b:",type(b),"\n",b)
lst = b.split('\n')
print(lst)

lst = b.strip() # By default, the strip() method removes whitespace. This set of characters includes: \t\n\r\f\v
print(lst)

# You can pass any characters as an argument to the strip method - then all characters that were specified in the string will be removed from the beginning and end of the string:
print("([123/456])".strip('[])(')) # 123/456

# 5. Formatting strings using the str.format() method

s1 = "The novel ’{0}' was published in {1} year".format("Hard Times", 1854)
print(s1) # The novel ’Hard Times' was published in 1854 year

s2 = "{{{0}}} {1} numeric".format("I'm text", "I'm not")
print(s2) # {I'm text} I'm not numeric

s3 = "{0}{1}".format("The amount due is $", 200)
print(s3) # The amount due is $200

# Using field names (named arguments)

s4 = "{who} turned {age} this year".format(who="She", age=88)
s5 = "The {who} was {0} last week".format(10, who="boy") # in the argument list, named arguments always come after positional ones
print(s4, "\n", s5) # She turned 88 this year
# The boy was 10 last week

# Field names can refer to collections, such as lists

stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
s6 = "We have {0[1]} and {0[2]} in stock".format(stock)
print(s6) # We have envelopes and notepads in stock

# Dictionaries as arguments

d = dict(animal="elephant", weight=12000)
s7 = "The {0[animal]} weighs {0[weight]}kg".format(d)
print(s7) # The elephant weighs 12000kg

# Formatting strings with f-strings
"""
F-strings are string literals with the letter f in front of them.
Inside the f-string, in a pair of curly braces,
the names of the variables to be substituted are specified
f-strings are an expression that is executed
"""
who = "Holly"
age = 99
s4 = f"{who.upper()} turned {age} this year"
print("f:", s4) # HOLLY turned 99 this year