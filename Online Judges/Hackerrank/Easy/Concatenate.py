#!/usr/bin/env python
# coding: utf-8

# In[130]:


import numpy as np
n, m, p = map(int, input().split())
arrN = np.array([input().split() for i in range(n)], int)
arrM = np.array([input().split() for i in range(m)], int)
final = np.concatenate((arrN, arrM), axis=0)
print(final)

