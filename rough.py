import numpy as np
import random

pos_int = random.randint(1, 10001)
#pos_int = range(1, 10001)
print(pos_int)
pos_ints=[pos_int]

#for i in pos_int:
while pos_int >1: 
    if pos_int % 2 == 0:                  # if it is an even number
        pos_int = pos_int/2               # it is divided by 2
        pos_ints.append(int(pos_int))    
    else:
        pos_int % 2 !=0                  # or else if it is an odd number
        pos_int = (pos_int * 3) + 1      # multiply by 3 and add 1
        pos_ints.append(int(pos_int))


#print(pos_ints, end = ' ')                   # print the list of numbers generated without commas or brackets

from random import choice
from time import sleep

n = choice([x for x in range(2, 10000) if all(x%y != 0 for y in range(2, x))])
ls = []
ls.append(n)
while True:
    if n % 2 == 0:
        n = n // 2
        ls.append(n)
    elif n % 2 != 0:
        n = (3 * n) + 1
        ls.append(n)
    if n == 1:
        break
print(ls)