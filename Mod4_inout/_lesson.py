#!/usr/bin/env python
# coding: utf-8

# # Lesson 4: Perform Input and Output Operations

# ## Working With Files

# ### Write to the file

# In[55]:


dirfile = "D:\\data\\"    # can be replaced with your catalog
namefile = dirfile + "myfile.txt"    # Full way to file
myfile = open(namefile, 'w')     # Opens the file (creates/cleans)
k = myfile.write("hello text file\n")       # Writes the line of text
print(k)  # Python 3.0 Write method returns the number of recorded characters
myfile.write("goodbye text file\n")
myfile.close()


# In[48]:


lis = ['First line \ n', 'second line \ n', 'third line \ n']
myfile = open(namefile, 'a')       # Opens the file (opening for derivibe, information is added to the end of the file)
myfile.writelines(lis)             # Write all lines from the list to file


# In[51]:


names = ['Petya', 'Kolya', 'Vasya']
f1 = open(namefile, 'a')
for it in names:          # Write all lines from the list to file
    f1.write(it + '\t')
f1.close()


# ### Reading from the file

# In[52]:


myfile = open(namefile, 'r') # Opens the file: ‘r’ - for reading
content = myfile.read()      # Read the file entirely in the line
print(content) 
myfile.close()


# In[37]:


myfile = open(namefile)  # Opens the file: ‘r’ - by default
print(myfile.readline()) # Reads the line


# In[38]:


fs = open(namefile).read() # Read the file entirely in the line
print(fs)


# In[54]:


# View the contents of the file string behind the line
for lin in open(namefile):
    print(lin, end='')


# In[61]:


# Reading the file entirely in the list of lines (including the symbol of the end of the line)
fl = open(namefile).readlines()
print(fl)


# ### with ... as - Context managers

# Construction with ... as used to wrap the executions of the instructions by the manager of context

# In[60]:


# The previous example can be recorded using With ... as the functionality will not change
with open(namefile, 'r') as fobj:
    f = fobj.readlines()
    print(f)     


# ### Working with CSV format

# In[62]:


# Read the CSV file using the csv module
import csv
with open('D:\data\input.csv') as csvfile:
    inputcsv = csv.reader(csvfile, delimiter=',')
    for i in inputcsv:
        print(i)


# In[ ]:




