#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np
n = int(input())
arrA = np.array([input().split() for i in range(n)], int)
arrB = np.array([input().split() for i in range(n)], int)

print(np.dot(arrA, arrB))

