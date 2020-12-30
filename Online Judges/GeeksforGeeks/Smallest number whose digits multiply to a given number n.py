#!/usr/bin/env python
# coding: utf-8

# In[31]:


def getSmallest(N):
    res = ''
    if N < 10:
        return str(N)
    else:
        for i in range(9, 1, -1):
            while N%i == 0:
                N = N/i
                res = res+str(i)
    print(res[::-1])

