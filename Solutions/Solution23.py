# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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
def isAbundant(number):
    return number<sum(divisors(number))
def isSumOfTwoAbundant(number):
    for i in range(1,number) :
                if isAbundant(i) and isAbundant(number-i):
                    return True
    return False
cannotWritables=0
for i in range(1,28123):
    if not isSumOfTwoAbundant(i):
        cannotWritables+=i
print(cannotWritables)
stop = timeit.default_timer()

print('Time: ', stop - start)  