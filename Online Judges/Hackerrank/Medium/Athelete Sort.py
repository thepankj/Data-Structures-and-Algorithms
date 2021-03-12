#!/usr/bin/env python
# coding: utf-8

# In[59]:


n, m = map(int, input().split())
ele = [list(map(int, input().split())) for i in range(n)]
k = int(input())

sort_list = sorted(ele, key = lambda x:x[k])

for i in sort_list:
    print(*i)

