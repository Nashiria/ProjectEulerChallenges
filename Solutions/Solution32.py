# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import timeit,math
 
start = timeit.default_timer()
def divisors(number):
    divs=[]
    for i in range(1,(int)((number**(1/2)) + 1)) :
        if (number % i == 0) :
            if (number / i == i) :
                divs.append([i,i])
            else:
                divs.append([i,int(number/i)])
    divs.sort()
    if(number in divs):
        divs.remove(number)
    return divs

def pandigital(number):
    if len(str(number))==9:
        for i in range(1,10):
            if str(number).count(str(i))==0:
                return False
        return True
    return False
def multiplicand():
    nums=[]
    for i in range(1,9*8*7*6*5*4*3*2):
        if pandigital(i):
          nums.append(i)
        else:
            divs=divisors(i)
            for j in divs:
                if pandigital(str(j[0])+str(j[1])+str(i)):
                    nums.append(i)
    return sum(set(nums))
print(multiplicand())

stop = timeit.default_timer()
print('Time: ', stop - start)  