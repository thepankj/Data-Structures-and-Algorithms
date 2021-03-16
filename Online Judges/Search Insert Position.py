#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid = round(start + (end-start)/2)
            
            if nums[mid] == target:
                return(mid)
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return(start)

