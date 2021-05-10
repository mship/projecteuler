# going through first 100 problems of Project Euler in Python
# by Michael Shippee
# Here is the problem:

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrome(somenum):
    str_somenum = str(somenum)
    len_of = len(str_somenum)//2

    if(str_somenum[:len_of] == str_somenum[:len_of:-1]): # if string len is odd, this works
        return True
    elif(str_somenum[:len_of] == str_somenum[:len_of-1:-1]): #need to capture all chars if string len is even
        return True
    else: # not a palindrome
        return False


biggest_palin = 0
for i in range(100,999): # two loops two see all products of 3 digit numbers 
    for j in range(100, 999):
        if ispalindrome(i*j) and i*j > biggest_palin: # run function, check for larger
            biggest_palin = i*j

print(biggest_palin)

