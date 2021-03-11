#!/usr/bin/env python
# coding: utf-8

# In[29]:


N, X = map(int, input().split())
subj_lst = []
for i in range(X):
    temp = list(map(float, input().split()))
    subj_lst.append(temp)

std_tup = zip(*subj_lst)

for std in std_tup:
    ans = round(sum(std)/X, 1)
    print(ans)

