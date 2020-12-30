#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#program
def snakePattern(lst, size):
    twoDArray = [lst[x:x+size] for x in range(0, len(lst), size)] #breaks the 1D array int 2D array
    ans = []
    for i in range(len(twoDArray)):
        if i%2 == 0:
            ans.extend(twoDArray[i])
        else:
            ans.extend(twoDArray[i][::-1])
            
    print(' '.join(map(str, ans)))

#for input
t_cases = int(input())
inp = []
for i in  range(t_cases):
    lenOfMatrix = int(input())
    elementsInMatrix = list(map(int, list(input().split())))
    inp.append((lenOfMatrix, elementsInMatrix)) 

#driver
for i in inp:
    snakePattern(i[1], i[0])

