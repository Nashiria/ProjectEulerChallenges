# Problem 6
# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import timeit

start = timeit.default_timer()
def SumSquareDifference(limit=100):
    return sum([(a+1) for a in range(limit) ])**2 - sum([(a+1)*(a+1) for a in range(limit) ])
print(SumSquareDifference())
stop = timeit.default_timer()

print('Time: ', stop - start)  