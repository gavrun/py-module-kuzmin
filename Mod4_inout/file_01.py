dirfile = "D:\\data\\"
myfile = open(dirfile+"myfile.txt", 'w+') # Opens the file (creates/cleans)
k = myfile.write("hello text file\n") # Records a line of text
print(k)  # Python 3.0 Write method returns the number of recorded characters

myfile.write("goodbye text file\n")
myfile.close()

myfile = open(dirfile+"myfile.txt", 'r') # OPEN FIEL: ‘R’
content = myfile.read() # Read the whole file
print("Content:\n", content) 

myfile.close()

lis = ['First line \ n', 'second line \ n', 'third line \ n']
myfile = open("myfile.txt", 'a')    # Opens the file (adds)
myfile.writelines(lis)              # Recording all lines from the list to file

filename = "myfile2.txt"
names = ['Petya', 'Kolya', 'Vasya']
f1 = open(filename, 'w')
for it in names:                    # Recording all lines from the list to file
    f1.write(it + '\t')
f1.close()

myfile = open(filename, 'r')        # OPEN FIEL: ‘R’
content = myfile.read()             # Read the file entirely in the line
print(content) 
myfile.close()


myfile = open("myfile.txt")         # Outdoles the file: ‘R’ - by default
print(myfile.readline())            # Reads the line

fs = open("myfile.txt").read()      # Read the file entirely in the line
print("--", fs)

# View the contents of the file string behind the line
# File reading operations is not used
# Files have an iterator who automatically reads information from the line line behind the line in the context of the cycle for
for lin in open("myfile.txt"):
    print("---", lin, end='')

# Reading the file entirely in the list of lines (including the symbol of the end of the line)
fl = open("myfile.txt").readlines()
print(fl)
