#!/usr/bin/env python
# coding: utf-8

# In[50]:


N = int(input())
arr = list()
    
for i in range(N):
    inp = input()
    temp = inp.split()
    cmd = temp[0]
    args = temp[1:]
    if cmd != 'print':
        cmd += '(' + ','.join(args) + ')'
        expression = 'arr' + '.' + cmd
        eval(expression)
    else:
        print(arr)

