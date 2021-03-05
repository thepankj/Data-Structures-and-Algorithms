#!/usr/bin/env python
# coding: utf-8

# In[32]:


K = int(input())
rno = list(map(int, input().split()))

unique_rno = list(set(rno))

s1 = set()
s2 = set()
for room in rno: s1.add(room) if room not in s1 else s2.add(room)
cap_rno = s1.difference(s2)
print(cap_rno.pop())

