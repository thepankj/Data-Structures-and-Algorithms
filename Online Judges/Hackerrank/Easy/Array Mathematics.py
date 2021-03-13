#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
n, m = list(map(int, input().split()))

arrA = np.array([input().split() for _ in range(n)], int)
arrB = np.array([input().split() for _ in range(n)], int)

add = np.add(arrA, arrB)
sub = np.subtract(arrA, arrB)
mul = np.multiply(arrA, arrB)
div = arrA//arrB
mod = np.mod(arrA, arrB)
pow = np.power(arrA, arrB)

print('{}\n{}\n{}\n{}\n{}\n{}'.format(add, sub, mul, div, mod, pow))

