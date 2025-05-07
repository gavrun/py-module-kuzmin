# String declaration
string1 = "This is a string."
string2 = "  This is another string."

# String concatenation
combined = string1 + string2
print("Combined:", combined)

# String functions
print("Length:", len(string1))                # get length of the string

print("Title case:", string1.title())         # capitalize each word
print("Lower case:", string1.lower())         # convert to lower case
print("Upper case:", string1.upper())         # convert to upper case

print("Right stripped:", string2.rstrip())    # remove trailing spaces
print("Left stripped:", string2.lstrip())     # remove leading spaces
print("Stripped:", string2.strip())           # remove both leading and trailing spaces

print("'00023400'.strip('0'):", '00023400'.strip('0'))  # remove specific characters from both ends

# Character extraction with indexing
d = "qwerty"
ch = d[2]      # extracts 'e'
print("Character at index 2:", ch)

# Slicing strings
print("Slice d[1:3]:", d[1:3])       # 'we'
print("Slice d[1:]:", d[1:])         # from index 1 to end
print("Slice d[:3]:", d[:3])         # from start to index 3 (not inclusive)
print("Slice d[:]:", d[:])           # full string copy
print("Slice d[1:5:2]:", d[1:5:2])   # from index 1 to 5 with step 2

# Attempt to change a character (will raise an error)
try:
    d[2] = 'o'   # strings are immutable in Python
except TypeError as e:
    print("Error:", e)
