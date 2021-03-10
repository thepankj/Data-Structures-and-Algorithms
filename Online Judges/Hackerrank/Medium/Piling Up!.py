#!/usr/bin/env python
# coding: utf-8

# In[53]:


from collections import deque
T = int(input())
for i in range(T):
    int(input())
    cube = deque(map(int, input().split()))
for j in reversed(sorted(cubes)):
    if j == cube[0]:
        cube.popleft()
    elif j == cube[-1]:
        cube.pop()
    else:
        print('No')
        break
else: print('Yes')
    

