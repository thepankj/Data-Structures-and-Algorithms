#!/usr/bin/env python
# coding: utf-8

# In[10]:


def merge_the_tools(string, k):
    # your code goes here
    n = len(string)

    final = []
    for i in range(0, n, k):
        temp = string[i:i+k]
        u = ''
        for j in temp: 
            if j not in u:
                u += j 
        final.append(u)
        
    for k in final:
        print(k)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

