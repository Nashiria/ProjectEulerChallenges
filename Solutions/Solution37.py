# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import timeit

start = timeit.default_timer()
def PrimeCheck(n=10):
    if n == 1:return False
    i = 2
    while n>=i*i:
        if n % i == 0:return False
        i += 1
    return True
  

def truncatable(number):
    length=len(str(number))
    if not PrimeCheck(number):return False
    for i in range(1,length):
        if not PrimeCheck(int(str(number)[i:])):
            return False
        if not PrimeCheck(int(str(number)[:i])):
            return False
    return True

def truncPrime(target):
    count=0
    sums=0
    n=10
    while count<target:
        if truncatable(n):sums+=n;count+=1
        n+=1
    return sums
print(truncPrime(11))

stop = timeit.default_timer()

print('Time: ', stop - start)  