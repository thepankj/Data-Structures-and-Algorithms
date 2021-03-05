#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input())
nos_set = set(map(int, input().split()))

N = int(input())

for i in range(N):
    cmd = input().split()
    key = cmd[0]
    if key != 'pop':
        arg = cmd[1]
    else:
        arg = ''
    
    eval('nos_set.'+key+'('+arg+')')

print(sum(nos_set))

