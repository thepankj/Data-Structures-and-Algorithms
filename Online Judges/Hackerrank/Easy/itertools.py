#!/usr/bin/env python
# coding: utf-8

# In[113]:


#itertools.itertools.combinations_with_replacement()
import itertools
S, k = list(input().split())
S = sorted(S)
k = int(k)

for i in list(itertools.combinations_with_replacement(S, k)):
    print(''.join(i))


# In[110]:


#itertools.combinations()
import itertools
S, k = list(input().split())
S = sorted(S)
k = int(k)

for j in range(1, k+1):    
    for i in list(itertools.combinations(S, j)):
        print(''.join(i))


# In[95]:


#itertools.permutations()
import itertools
S, k = list(input().split())
k = int(k)

ans = []
for i in list(itertools.permutations(S, k)):
    ans.append(''.join(i))
    
for i in sorted(ans):
    print(i)


# In[ ]:


#itertools.product()
import itertools
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

for i in list(itertools.product(A, B)):
    print(i, end=' ')

