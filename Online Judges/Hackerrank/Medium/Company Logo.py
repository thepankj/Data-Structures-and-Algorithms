#!/usr/bin/env python
# coding: utf-8

# In[122]:


from collections import Counter
s = input()
sort_by_alph = sorted(s)
c = Counter(sort_by_alph)
sort_by_val = sorted(c, key = c.get, reverse = True)[:3]
for key in sort_by_val:
    print('{} {}'.format(key, c[key]))

