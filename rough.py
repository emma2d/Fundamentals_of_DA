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


print(pos_ints, end = ' ')                   # print the list of numbers generated without commas or brackets