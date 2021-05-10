# going through first 100 problems of Project Euler in Python
# by Michael Shippee
# Here is the problem:

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

gate = 0
start = 20
while(gate == 0):
    # count through numbers and check only divisors that are not covered elsewhere. For example, if a number is divisible by 16, we know it is divisible by 4 without checking
    if start%19 == 0 and start%18 == 0 and start%17 == 0 and start%16 == 0 and start%15 == 0 and start%14 == 0 and start%13 == 0 and start%12 == 0 and start%11 == 0:
        gate = 1
        break
    else:
        start += 20

print(start) #returns 232792560