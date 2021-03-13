#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
np.set_printoptions(None ,legacy = '1.13')
n, m = list(map(int, input().split()))
print(np.eye(n, m))

