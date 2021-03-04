#!/usr/bin/env python
# coding: utf-8

# In[44]:


M = int(input())
setM = set(map(int, input().split()))
N = int(input())
setN = set(map(int, input().split()))

for i in sorted(list((setM.difference(setN))) + list((setN.difference(setM)))): print(i)

