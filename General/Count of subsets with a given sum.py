#!/usr/bin/env python
# coding: utf-8

# In[109]:


'''
This function counts the number of subsets in the array arr which equal the sum s.

For example, if arr = [1, 2, 12, 6, 14, 8, 5] and s = 14

>> arr = [1, 2, 12, 6, 14, 8, 5]
>> s = 14
>> subsetSum(arr, s)
... 7

Explaination:
The count of subsets in arr with sum 14 is 5 - {1, 2, 6, 5}, {1, 8, 5}, {2, 12}, {6, 8}, {14}
'''

def subsetCount(arr, s):
    # code here
    N = len(arr)
    t = [[-1 for i in range(s+1)] for j in range(N+1)]
    
    for _ in range(s+1):
        t[0][_] = 0
    for _ in range(N+1):
        t[_][0] = 1
        
    for i in range(1, N+1):
        for j in range(1, s+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    
    return t[N][s]

