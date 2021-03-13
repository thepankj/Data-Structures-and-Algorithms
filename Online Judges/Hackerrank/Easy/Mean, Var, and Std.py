#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np
numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
arr = np.array([input().split() for i in range(n)], int)
mea = np.mean(arr, axis = 1)
var = np.var(arr, axis = 0)
std = np.std(arr)
print(mea,var,,std, sep = '')

