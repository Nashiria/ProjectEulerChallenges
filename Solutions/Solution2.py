# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
import timeit

start = timeit.default_timer()
def SumOfFibonacciEvenValues(limit=4000000):
    tmp=[]
    toReturn=0
    tmp.append(1)
    n=tmp[0]
    while n<limit:
        if n%2==0:
            toReturn+=n
        n=n+tmp[len(tmp)-2]
        tmp.append(n)
    print(tmp)
    return toReturn
print(SumOfFibonacciEvenValues())
stop = timeit.default_timer()

print('Time: ', stop - start)  
