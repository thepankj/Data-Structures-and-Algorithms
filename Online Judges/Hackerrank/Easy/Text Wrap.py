#!/usr/bin/env python
# coding: utf-8

# In[78]:


import textwrap

def wrap(string, max_width):
    
    return textwrap.fill(string, max_width) #textwrap.fill() returns a string containing \n after maximum width characters 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[75]:


import textwrap

