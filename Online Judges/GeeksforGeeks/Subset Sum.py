#!/usr/bin/env python
# coding: utf-8

# In[90]:


def equalPartition(self, N, arr):
    # code here
    if sum(arr)%2 != 0:
        return 0
    else:
        s = sum(arr)//2
        t = [[-1 for i in range(s+1)] for j in range(N+1)]

        for _ in range(s+1):
            t[0][_] = 0
        for _ in range(N+1):
            t[_][0] = 1

        for i in range(1, N+1):
            for j in range(1, s+1):
                if arr[i-1] <= j:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]

        return t[N][s]

