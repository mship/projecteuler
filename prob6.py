# going through first 100 problems of Project Euler in Python
# by Michael Shippee
# Here is the problem:
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 == 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sq_total = 0
sum_total = 0

for i in range(1, 101):
    sq_total += i**2
    sum_total += i

sum_total = sum_total**2

print(sum_total - sq_total) # returns 25164150