# Objects of the Python language should
# sign up to the file only in the form of lines

X, Y, Z = 43, 44, 45 
S = 'Spam' 
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')           # Creates a file for recording
F.write(S + '\n')                       # Lines end with a symbol \ n
F.write('%s,%s,%s\n' % (X, Y, Z))       # Transforms numbers into lines
F.write(str(L) + ';' + str(D) + '\n')   # Transforms and shares a symbol;
F.close()

# reverse transformations to get
# from lines in a text file Actual objects

F = open('datafile.txt')    # Open the file
line = F.readline()         # Read one line
line.rstrip()               # Delete the end of the line
print(line)                 # Spam


line = F.readline()         # The next line from the file
# This is a line ‘43, 44.45 \ n ’
parts = line.split(',')     # Break to tuning on a comma
print(parts)
numbers = [int(P) for P in parts] # Transform the entire list into numbers
print(numbers)

# transform the list and dictionary

line = F.readline() # “[1,2,3];{‘a’:1, ‘b’:2}\n”
parts = line.split(';') # Break into lines by symbol $
print(parts)

eval(parts[0])              # Transform the line into an object
objects = [eval(P) for P in parts] # Transformation for all lines in the list
print(objects) # List includes a list and dictionary
