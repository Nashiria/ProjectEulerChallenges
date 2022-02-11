# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import timeit

start = timeit.default_timer()
def DivisibleThroughAll(limit=20):
    numsInLimit=[a+1 for a in range(limit)]
    toReturn = 1
    numsInLimit.reverse()
    for number in numsInLimit:
        if toReturn % number != 0:
            toReturn *= number
    for number in numsInLimit:
        divide=True
        for number2 in numsInLimit:
            if (toReturn/number)%number2 != 0:
                divide=False
                break
        if divide:
            toReturn/=number
    return (int(toReturn))
print(DivisibleThroughAll())
stop = timeit.default_timer()

print('Time: ', stop - start)  
