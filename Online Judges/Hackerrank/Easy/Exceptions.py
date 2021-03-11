#!/usr/bin/env python
# coding: utf-8

# In[95]:


T = int(input())
for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)

