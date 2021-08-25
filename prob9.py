# going through first 100 problems of Project Euler in Python
# by Michael Shippee
# Here is the problem:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2 <- these are squares

# For example, 32 + 42 = 9 + 16 = 25 = 52. <- also squares

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# first need to simplify problem

# a + b + c = 1000 
# square both sides -> a^2 + ab + ac + b^2 + ab + bc + c^2 + ac + bc = 1000000
# simplify -> a^2 + b^2 + c^2 + 2ab + 2ac + 2bc = 1000000
# from above, c^2 == a^2 + b^2 -> a^2 + b^2 + a^2 + b^2 + 2ab + 2ac + 2bc = 1000000
# simplify -> a^2 + b^2 + ab + ac + bc = 500000
# c = 1000 - a - b -> a^2 + b^2 + ab + a*(1000 - a - b) + b*(1000 - a - b) = 500000
# rewrite -> a^2 + b^2 + ab + 1000a - a^2 - ab + 1000b - ab - b^2 = 500000
# simplify -> 1000a - ab + 1000b = 500000
# rewrite -> 1000(a - (ab/1000) + b) = 500000 -> a - (ab/1000) + b = 500

for a in range(500):
    for b in range(a, 500):
        div1000 = (a*b)/1000
        if(a+b-div1000) == 500:
            c = 1000 - a - b
            print(a*b*c) # returns 31875000