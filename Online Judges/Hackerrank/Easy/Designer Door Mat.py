#!/usr/bin/env python
# coding: utf-8

# In[19]:


n, m = map(int, input().split())

pattern = [('.|.'*(2*i+1)).center(m, '-') for i in range(n//2)]

for i in pattern: print(i)
print('WELCOME'.center(m, '-'))
for i in pattern[::-1]: print(i)

