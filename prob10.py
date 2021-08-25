# going through first 100 problems of Project Euler in Python
# by Michael Shippee
# Here is the problem:

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math
primes = [2, 3, 5, 7] # list to hold prime numbers to check for others
sum = 17 # sum of seeded list
target = 2000000 # count to 2,000,000

# this is a brute force solution. just check through all numbers to target, and see if they are prime, then tally them
# very slow. One idea for a better solution is to make a list of all numbers 2-2000000, then count up and remove 
# multiples from the list. might run faster because as things are removed from the list, we speed up the iterations
for i in range(2, target):
    print(i)
    for j in primes:
        if i % j == 0:
            break
        if j == primes[-1]:
            if i not in primes:
                primes.append(i)    
                sum += i
print(sum) # prints 142913828922