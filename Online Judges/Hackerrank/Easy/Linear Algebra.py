#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
n = int(input())
a = np.array([input().split() for i in range(n)], float)
print(np.linalg.det(a))

