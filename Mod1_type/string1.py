# A string is an ordered, immutable sequence of Unicode characters

''' 1. How to join two strings? '''
x = str("AXTR") # x becomes 's1'
y = str(567) # y becomes '2'
xy = x + y
print(xy)

''' 2. How to join three strings?
join() is a method that allows you to join N strings with an arbitrary separator
join() is a method of the string object that takes a list as an argument
and returns a new string as output '''
names = ["John", "Paul", "Ringo", "George"]
allNames = "; ".join(names)
print(allNames) # John; Paul; Ringo; George

""" Task: implement your own implementation of the join() method"""

''' 3. How to split a string?
The split() method is applied to the target string, and the separator is passed as an argument
note the difference in the use of join and split'''
st = "Mom, I washed the frame"
stm = st.split(",")
print(stm) # ['Mom', ' I washed the frame']

''' slices
The s[x:y] slice allows you to get a substring from character x to character y
With the optional third parameter s[x:y:N], you can select every N-th character from the substring '''

#get only characters at even positions:
s = "a123y56t89"
print(s[::2]) # a2y68
# get only characters at odd positions:
print(s[1::2]) # 135t9

'''Searching in a string
Simple search:
Check if (does) the string end with the selected characters.
Python has special string methods for this '''
s = "0123456789"
print(s.startswith("012")) # True
print(s.endswith("69")) # False

"""For searching for a substring in an arbitrary place, there is the find() method - it will return
the index of the beginning of the found occurrence of the substring in the string,
or -1 if nothing was found """
s = "0123456789"
print(s.find("45")) # 4
print(s.find("42")) # -1

'''
Complex search:
If you need to find not a specific sequence of characters, but a certain pattern, then - regular expressions
'''
import re
s = "http://itcenter.itmo.ru/inzhener_programmist_750";
result = re.match(r"^(http|https)://([^/]+)(.*)$", s)
print(result.group(1)) # http
print(result.group(2)) # itcenter.itmo.ru
print(result.group(3)) # /inzhener_programmist_750

'''
Replacement in a string
Using slicing and gluing strings, you can replace anything '''
s = "Hello, darling! How are you?"
s1 = s[:7] + "Vasily" + s[14:]
print(s1) # 'Hello, Vasily! How are you?'
'''
Using the replace() method '''
s2 = s.replace("darling", "Vasily")
print(s2) #'Hello, Vasily! How are you?'
'''
Any problem can be solved with regular expressions.
In case of replacement, you need the re.sub() method '''
s = "ttp://itcenter.itmo.ru/inzhener_programmist_750";
s3 = re.sub('[a-z]', 'Y', s)
print(s3) # YYY://YYYYYYYY.YYYY.YY/YYYYYYYYY_YYYYYYYYYYY_750

'''
Formatting strings
A standard task: to form a string by substituting the result of the program into it.
Starting with Python 3.6, this can be done using f-strings '''
sf = f"The string '{s}' contains {len(s)} characters."
print(sf) # "The string 'Hello, world!' contains 13 characters."
'''
In earlier versions of the language '''
sf1 = "String '%s' contains %d characters" % (s, len(s))
sf2 = "String '{}' contains {} characters".format(s, len(s))
print(sf1,'\n', sf2)