# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.
import timeit

start = timeit.default_timer()

def divisors(number):
    divs=[]
    for i in range(1,(int)((number**(1/2)) + 1)) :
        if (number % i == 0) :
            if (number / i == i) :
                divs.append(i)
            else:
                divs.append(i)
                divs.append(int(number/i))
    divs.sort()
    if(number in divs):
        divs.remove(number)
    return divs

def amicableNum(number):
    if number==sum(divisors(sum(divisors(number)))) and number!=sum(divisors(number)):
        return True
    return False
totalSum=0
for i in range(1,10000):
    if amicableNum(i):
        totalSum+=i
print(totalSum)
stop = timeit.default_timer()

print('Time: ', stop - start)  