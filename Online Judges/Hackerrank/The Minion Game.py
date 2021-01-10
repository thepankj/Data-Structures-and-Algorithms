#!/usr/bin/env python
# coding: utf-8

# In[23]:


def minion_game(string):
    # your code goes here
    stuart, kevin = 0, 0
    vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if stuart > kevin:
        print('Stuart {}'.format(stuart))
    elif kevin > stuart:
        print('Kevin {}'.format(kevin))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

