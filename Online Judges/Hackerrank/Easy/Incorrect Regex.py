#!/usr/bin/env python
# coding: utf-8

# In[101]:


import re
T = int(input())
for i in range(T):
    S = input()
    try:
        print(bool(re.compile(S)))
    except:
        print('False')

