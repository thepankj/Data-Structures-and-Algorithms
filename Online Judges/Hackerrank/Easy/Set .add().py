#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input())
countries = set()
for i in range(n):
    inp = input()
    countries.add(inp)
    
print(len(countries))

