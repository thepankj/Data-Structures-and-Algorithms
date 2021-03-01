#!/usr/bin/env python
# coding: utf-8

# In[71]:


def split_and_join(line):
    # write your code here
    split = line.split(' ')
    join = '-'.join(split)
    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

