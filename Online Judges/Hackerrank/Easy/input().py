#!/usr/bin/env python
# coding: utf-8

# In[36]:


x, k = map(int, input().split())
exp = input()
test = eval(exp)
print(test == k)

