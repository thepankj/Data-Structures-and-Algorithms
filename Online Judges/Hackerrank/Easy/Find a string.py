#!/usr/bin/env python
# coding: utf-8

# In[78]:


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        temp = string[i:]
        if temp.startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

