#!/usr/bin/env python
# coding: utf-8

# In[11]:


n = int(input())
setn = set(map(int, input().split()))
b = int(input())
setb = set(map(int, input().split()))

union = setn.union(setb)
print(len(union))


# In[ ]:


####################################################################
n = int(input())
setn = set(map(int, input().split()))
b = int(input())
setb = set(map(int, input().split()))

union = setn.intersection(setb)
print(len(union))

