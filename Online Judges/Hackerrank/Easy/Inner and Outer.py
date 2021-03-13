#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np
arrA = np.array(input().split(), int)
arrB = np.array(input().split(), int)

print(np.inner(arrA, arrB))
print(np.outer(arrA, arrB))

