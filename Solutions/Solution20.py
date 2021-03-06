# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!
import timeit

start = timeit.default_timer()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
def sumOfDigits(n):
    return sum([int(x) for x in str(n)])
print(sumOfDigits(factorial(100)))
stop = timeit.default_timer()

print('Time: ', stop - start)  