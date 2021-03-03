#!/usr/bin/env python
# coding: utf-8

# In[100]:


import string
def print_rangoli(size):
    # your code goes here
    rows = 2*size-1
    cols = 2*rows-1

    alphabets = string.ascii_lowercase

    lower = []
    for i in range(rows//2+1):
        lower.append('-'.join(alphabets[i:size][:0:-1]+alphabets[i:size]))
        
    full_list = lower[::-1]+lower[1:]

    for j in full_list:
        print(j.center(cols, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

