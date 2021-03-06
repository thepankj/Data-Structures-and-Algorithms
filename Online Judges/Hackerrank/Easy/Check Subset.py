#!/usr/bin/env python
# coding: utf-8

# In[ ]:


T = int(input())
for _ in range(T):
    nA = int(input())
    A = set(map(int, input().split()))
    nB = int(input())
    B = set(map(int, input().split()))
    print(True) if A.issubset(B) else print(False)

