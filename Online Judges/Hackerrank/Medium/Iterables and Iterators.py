#!/usr/bin/env python
# coding: utf-8

# In[28]:


from itertools import combinations
N = int(input())
letters = input().split()
K = int(input())

combs = list(combinations(letters, K))
fav_outcome = 0
for i in combs:
    if 'a' in i:
        fav_outcome += 1
tot_outcome = len(combs)
prob = round(fav_outcome/tot_outcome, 3)
print(prob)

