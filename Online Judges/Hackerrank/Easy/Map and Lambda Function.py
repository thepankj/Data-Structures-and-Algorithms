#!/usr/bin/env python
# coding: utf-8

# In[17]:


cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    ans = [0, 1]
    for i in range(2,n):
        ans.append(ans[-2] + ans[-1])
    return(ans[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

