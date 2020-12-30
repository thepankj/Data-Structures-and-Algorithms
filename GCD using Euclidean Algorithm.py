#!/usr/bin/env python
# coding: utf-8

# In[16]:


#GCD using Euclidean Algo

def gcd(a, b):
    if a == 0:
        return b
    else:
        return(gcd(b%a, a))
gcd(120, 0)

