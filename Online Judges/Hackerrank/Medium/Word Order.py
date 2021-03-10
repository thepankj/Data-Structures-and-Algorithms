#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import OrderedDict
n = int(input())
ans_dict = OrderedDict()
for i in range(n):
    word = input()
    if word in ans_dict:
        ans_dict[word] += 1
    else:
        ans_dict[word] = 1

print(len(ans_dict))
for j in ans_dict.items():
    print(j[1], end = ' ')

