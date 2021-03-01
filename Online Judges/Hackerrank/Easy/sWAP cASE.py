#!/usr/bin/env python
# coding: utf-8

# In[69]:


s = input()
new_str = ''
for i in s:
    if i.isupper():
        new_str += i.lower()
    else:
        new_str += i.upper()

