#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def knapSack(W, wt, val, n):
    '''
    :param W: capacity of knapsack 
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    '''
    # code here
    t = [[-1 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j== 0:
                t[i][j] = 0
            elif wt[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]

    return t[n][W]

