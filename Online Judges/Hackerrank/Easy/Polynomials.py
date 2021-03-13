#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
coeff = np.array(input().split(), float)
x = int(input())

np.polyval(coeff, x)

