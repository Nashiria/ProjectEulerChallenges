
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
import timeit

start = timeit.default_timer()
def findMultiplesOfN(n1=3,n2=5,limit=1000):
    sums=0
    for num in range(limit):
        if num %n1 == 0 or (num) %n2 == 0:
            sums+=num
    # return tmp for numbers in list
    return sums
print(findMultiplesOfN())
stop = timeit.default_timer()

print('Time: ', stop - start)  