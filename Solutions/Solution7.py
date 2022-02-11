# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10 001st prime number?
import timeit

start = timeit.default_timer()
def PrimeCheck(n=10):
    if n == 1:return False
    i = 2
    while n>=i*i:
        if n % i == 0:return False
        i += 1
    return True
def nThPrime(n=10001):
    count=0
    num=1
    while count!=n:
        num += 1
        if PrimeCheck(num):
            count+=1
    return num
print(nThPrime())
stop = timeit.default_timer()

print('Time: ', stop - start)  