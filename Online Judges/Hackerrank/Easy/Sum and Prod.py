#!/usr/bin/env python
# coding: utf-8

# In[57]:


n, m = map(int, input().split())
arr = np.array([input().split() for i in range(n)], int)
s = np.sum(arr, axis = 0)
p = np.prod(s)
print(p)

