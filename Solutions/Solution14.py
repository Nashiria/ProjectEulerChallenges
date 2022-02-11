# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
import timeit

start = timeit.default_timer()

def chainCount(number):
    chain=0
    while number!=1:
        if number%2==0:
            number=number/2
        else:
            number=3*number+1
        chain+=1
    return chain

def maxChainCount(number):
    maxChainNumber=0
    maxChain=0
    for i in range(number):
        chain=chainCount(i+1)
        if chain>maxChain:
            maxChain=chain
            maxChainNumber=i+1
    return maxChainNumber,maxChain

print(maxChainCount(1000000))
stop = timeit.default_timer()

print('Time: ', stop - start)  