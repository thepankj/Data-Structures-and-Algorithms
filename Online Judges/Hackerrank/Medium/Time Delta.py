#!/usr/bin/env python
# coding: utf-8

# In[81]:


from datetime import datetime as dt

T = int(input())
form = '%a %d %b %Y %H:%M:%S %z'
for i in range(T):
    t1 = dt.strptime(input(), form)
    t2 = dt.strptime(input(), form)
    print(int(abs(t1-t2).total_seconds()))

