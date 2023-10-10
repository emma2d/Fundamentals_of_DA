import numpy as np

pos_int = np.array.a.any((range(1, 1001)))
pos_ints=[pos_int]

for i in pos_ints:

    if pos_int % 2 == 0:                  # if it is an even number
        pos_int = pos_int/2               # it is divided by 2
        pos_ints.append(int(pos_int))    
    else:
        pos_int % 2 !=0                  # or else if it is an odd number
        pos_int = (pos_int * 3) + 1      # multiply by 3 and add 1
        pos_ints.append(int(pos_int))


print(i, end = ' ')                   # print the list of numbers generated without commas or brackets