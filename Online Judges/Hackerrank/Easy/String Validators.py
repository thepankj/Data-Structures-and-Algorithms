#!/usr/bin/env python
# coding: utf-8

# In[21]:


if __name__ == '__main__':
    s = input()
    alnum_check = any([i.isalnum() for i in s])
    alpha_check = any([i.isalpha() for i in s])
    digit_check = any([i.isdigit() for i in s])
    lower_check = any([i.islower() for i in s])
    upper_check = any([i.isupper() for i in s])

    print('{}\n{}\n{}\n{}\n{}'.format(alnum_check, alpha_check, digit_check, lower_check, upper_check))

