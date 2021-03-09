#!/usr/bin/env python
# coding: utf-8

# In[58]:


#collections.Counter()
from collections import Counter
X = int(input())
shoe_s = list(map(int, input().split()))
N = int(input())
quant = []
for i in range(N):
    quant.append(tuple(map(int, input().split())))
    
shoes_count = Counter(shoe_s)
profit = 0
for i in quant:
    if i[0] in shoes_count and shoes_count[i[0]]>0:
        profit += i[1]
        shoes_count[i[0]] -= 1
print(profit)


# In[161]:


#collections.defaultdict
from collections import defaultdict
n, m = list(map(int, input().split()))
groupA = defaultdict(list)
for i in range(1, n+1):
    temp = input()
    groupA[temp].append(i)
    
ans = []
for j in range(m):
    temp = input()
    if temp in groupA:
        ans.append(list(groupA[temp]))
    else:
        ans.append(-1)
    
for i in ans:
    if type(i) == list:
        print(*i)
    else:
        print(i)


# In[33]:


#collections.namedtuple()
from collections import namedtuple
N = int(input())
columns = namedtuple('Columns', input())
tot_marks = 0
for i in range(N):
    temp = input().split()
    t1, t2, t3, t4 = temp
    students = columns(t1, t2, t3, t4)
    tot_marks += int(students.MARKS)
average = round(tot_marks/N, 2)
print(average)


# In[66]:


#Collections.OrderedDict
from collections import OrderedDict
N = int(input())
odict = OrderedDict()
for i in range(N):
    temp = input().split()
    item_name, net_price = ' '.join(temp[:-1]), int(temp[-1])
    if item_name in odict:
        odict[item_name] += int(net_price)
    else:
        odict[item_name] = int(net_price)
for key, value in odict.items():
    print('{} {}'.format(key, value))


# In[126]:


#collections.deque
from collections import deque
N = int(input())
deq = deque()
for i in range(N):
    cmd = input().split()
    method = cmd[0]
    try:
        val = cmd[1]
    except:
        val = ''
    exe = 'deq.'+method+'('+val+')'
    eval(exe)
    
print(*deq)

