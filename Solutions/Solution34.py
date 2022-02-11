# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import timeit

start = timeit.default_timer()

def isCuriousNumber(number):
    import math
    tmp=0
    for digit in str(number):
        tmp+=math.factorial(int(digit))
    if tmp==number:
        return True
    return False

def sumOfCuriousNumbers():
    sums=0
    for num in range(3,(9**6)):
        if isCuriousNumber(num):
            sums+=num
    return sums
print(sumOfCuriousNumbers())

stop = timeit.default_timer()

print('Time: ', stop - start)  