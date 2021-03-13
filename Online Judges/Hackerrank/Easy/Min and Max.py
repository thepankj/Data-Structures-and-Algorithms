#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np
n, m = map(int, input().split())
arr = np.array([input().split() for i in range(n)], int)
mi = np.min(arr, axis = 1)
ma = np.max(mi)
print(ma)

