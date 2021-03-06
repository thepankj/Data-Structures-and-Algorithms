#!/usr/bin/env python
# coding: utf-8

# In[ ]:


A = set(map(int, input().split()))
n = int(input())
out = 1
for i in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B):
        out = 0
        break

print(bool(out))

