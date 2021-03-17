#!/usr/bin/env python
# coding: utf-8

# In[144]:


def rotated_search(nums, target):
    s = 0
    l = len(nums)
    e = l-1
    
    while s<=e:
        m = s+(e-s)//2
        pre = (m-1+l)%l
        nex = (m+1)%l
        
        if target == nums[m]:
            return(m)
        
        if nums[s]<=nums[m]: #left rotation ie pivot on right half
            if nums[s]<=target<=nums[m]:
                e = m-1
            else:
                s = m+1
        else: #right rotation ie pivot on left half
            if nums[m]<=target<=num[e]:
                s = m+1
            else:
                e = m-1
    return(-1)

