#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_formatted(number):
    # your code goes here
    pad = len(bin(number)[2:])
    
    for i in range(1, number+1):
        octal = oct(i)[2:]
        hdecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        
        print('{} {} {} {}'.format(str(i).rjust(pad), octal.rjust(pad), hdecimal.rjust(pad), binary.rjust(pad)))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

