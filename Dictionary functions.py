#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# # Dictionary functions in python

# In[5]:


my_dict = {'captain':19,'ironman':21,'thor':22}


# In[6]:


my_dict['captain']


# In[7]:


my_dict.get('thor') #Returns the value of specified key


# In[8]:


my_dict.keys() #Returns a list containing a dictionary's keys


# In[9]:


my_dict.values() #Returns a list of all the values in the dictionary


# In[10]:


my_dict.items() #Returns alist containing a tuple for each key value pair


# In[15]:


my_dict.fromkeys('captain') #Returns a dictionary with specified keys and value


# In[16]:


my_dict.clear() #Removes all the elements from the list


# In[17]:


print(my_dict)

