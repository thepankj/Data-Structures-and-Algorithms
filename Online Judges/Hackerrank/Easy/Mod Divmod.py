#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = int(input())
b = int(input())

quo = a//b
rem = a%b
tup = divmod(a,b)
print('{}\n{}\n{}'.format(quo, rem, tup))

