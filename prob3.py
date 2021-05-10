# going through first 100 problems of Project Euler in Python
# by Michael Shippee
# Here is the problem:

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

large_prime = 600851475143
target = int(large_prime**(1/2))
temp = large_prime
old_temp = 0
for i in range(2, target-1):
    print(i)
    while temp%i == 0:
        old_temp = temp
        if temp != i:
            temp = temp/i
        if temp == old_temp:
            break

print(temp)