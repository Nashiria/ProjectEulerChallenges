# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import timeit

start = timeit.default_timer()
def PrimeCheck(n=10):
    if n == 1:return False
    i = 2
    while n>=i*i:
        if n % i == 0:return False
        i += 1
    return True
def SumOfPrimesBelowN(n=2000000):
    sum=0
    for num in range(n-1):
        if PrimeCheck(num+2):
            sum+=num+2
    return sum
print(SumOfPrimesBelowN())
stop = timeit.default_timer()

print('Time: ', stop - start)  