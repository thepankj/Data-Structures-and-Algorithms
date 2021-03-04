#!/usr/bin/env python
# coding: utf-8

# In[22]:


def average(array):
    # your code goes here
    nos = set(array)
    avg = sum(nos)/len(nos)
    return(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

