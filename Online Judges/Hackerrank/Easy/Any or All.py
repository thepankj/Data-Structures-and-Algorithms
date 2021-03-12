#!/usr/bin/env python
# coding: utf-8

# In[37]:


N = int(input())
inp = list(map(int, input().split()))
chk_pos = all([i > 0 for i in inp])
chk_pal = any([str(i) == str(i)[::-1] for i in inp])

ans = all([chk_pos and chk_pal])
print(ans)

