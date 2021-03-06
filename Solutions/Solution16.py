# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
import timeit

start = timeit.default_timer()

def sumOfDigits2N(n):
    return sum([int(x) for x in str(2**n)])
print(sumOfDigits2N(1000))
stop = timeit.default_timer()

print('Time: ', stop - start)  