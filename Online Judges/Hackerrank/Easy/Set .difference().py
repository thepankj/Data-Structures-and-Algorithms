#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
setn = set(map(int, input().split()))
b = int(input())
setb = set(map(int, input().split()))

diff = setn.difference(setb)
print(len(diff))

