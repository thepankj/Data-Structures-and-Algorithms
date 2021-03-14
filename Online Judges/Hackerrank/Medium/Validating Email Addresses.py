#!/usr/bin/env python
# coding: utf-8

# In[75]:


import re

def fun(s):
    try:
        uname, web, ext = re.split('@|\.', s)
    except ValueError as v:
        return(False)
    if not uname.replace('-', '').replace('_', '').isalnum():
        return(False)
    elif not web.isalnum():
        return(False)
    elif not len(ext) < 4:
        return(False)
    else:
        return(True)

