#!/usr/bin/env python
# coding: utf-8

# In[ ]:


na = int(input())
A = set(map(int, input().split()))

N = int(input())
for i in range(N):
    cmd = input().split()
    op = cmd[0]
    temp = set(map(int, input().split()))
    expression = 'A.'+op+'('+ 'temp' +')'
    eval(expression)

print(sum(A))

