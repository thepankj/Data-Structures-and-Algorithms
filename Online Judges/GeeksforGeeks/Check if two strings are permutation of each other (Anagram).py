#!/usr/bin/env python
# coding: utf-8

# In[48]:


def isAnagram(a,b):
    if len(a) != len(b):
        return False
    else:
        a = set(list(a))
        b = set(list(b))
        return a == b

