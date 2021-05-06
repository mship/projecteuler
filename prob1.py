# going through first 100 problems of Project Euler in Python
# by Michael Shippee
multi_3 = 3
multi_5 = 5
retval = 0
# loop for multiples of 3
while multi_3 < 1000:
    retval += multi_3
    multi_3 += 3
# loop for multiples of 5
while multi_5 < 1000:
    retval += multi_5
    multi_5 += 5
    if multi_5%3 == 0: # no duplicates
        multi_5 += 5 # any number that is divisible by 3, + 5, will no longer be divisible by 3
#effectively our return - returns 233168
print(retval)