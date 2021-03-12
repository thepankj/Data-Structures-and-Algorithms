#!/usr/bin/env python
# coding: utf-8

# In[114]:


s = input()
num = list(filter(str.isdigit, s))
o_num = filter(lambda x: int(x)%2 != 0, num)
e_num = filter(lambda x: int(x)%2 == 0, num)
upp = filter(str.isupper, s)
low = filter(str.islower, s)
ans = ''.join(sorted(low)+sorted(upp)+sorted(o_num)+sorted(e_num))
print(ans)

