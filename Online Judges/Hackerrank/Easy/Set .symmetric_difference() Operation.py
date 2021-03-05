#!/usr/bin/env python
# coding: utf-8

# In[14]:


n = int(input())
setn = set(map(int, input().split()))
b = int(input())
setb = set(map(int, input().split()))

union = setn.symmetric_difference(setb)
print(len(union))

