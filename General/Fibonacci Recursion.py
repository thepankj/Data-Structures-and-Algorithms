#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

