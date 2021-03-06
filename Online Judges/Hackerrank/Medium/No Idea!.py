#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, m = tuple(map(int, input().split()))

setn = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

happiness = 0
for i in setn:
    if i in setA:
        happiness += 1
    if i in setB:
        happiness -= 1
        
print(happiness)

