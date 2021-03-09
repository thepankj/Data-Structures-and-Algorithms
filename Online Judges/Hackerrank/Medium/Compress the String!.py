#!/usr/bin/env python
# coding: utf-8

# In[23]:


from itertools import groupby

S = input()
ans = []
for key, value in groupby(S):
    temp = (len(list(value)), int(key))
    ans.append(temp)
    

print(*ans, sep = ' ')

