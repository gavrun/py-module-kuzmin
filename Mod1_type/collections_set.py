#!/usr/bin/env python
# coding: utf-8

#### Set - disordered collection of unique elements

# In[16]:


s1 = {"ab", "cd", "ef"}
s2 = set([1, 2, 3, 4, 5]) # Applys the SET () function by transmitting any iberized object as an argument.
print(s1)
print(s2)


# In[18]:


a = {2, 4, 6, 8, 10}
b = set(range(11))
print(a); print(b)


# In[19]:


b.remove(0)
print(b)


# In[22]:


a.add(12)
print(a)


# In[24]:


print(a & b)


# In[25]:


print(a | b)


# In[26]:


print(a-b)


# In[27]:


print(b-a)


#### Display (dictionaries) - disordered collection of pairs of elements "key -meaning"

# In[35]:


# Several ways to create dictionaries - all of them create the same dictionary:
d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size": 3}
print(d1)
print(d2)


# In[8]:


mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14} # We create a dictionary with numerical and integer indices
print(mydict)
mydict["pi"] = 3.1416 # We change the element of the dictionary under the "Pi" index.
print(mydict)


# In[33]:


dp = {} # empty dictionary
# Filling out the dictionary
dp['color'] = 'red'
dp['index'] = 101
print(dp)


# In[37]:


dp['name'] = input("Enter name:  ")
dp['age'] = int(input("Enter age: "))
print(dp)


# In[39]:


print(dp.keys()) # Only the keys
print(dp.values()) # Only values


# In[ ]:

