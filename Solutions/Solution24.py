# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import timeit

start = timeit.default_timer()

def permutations(maximum):
    numbers=[str(x) for x in range(maximum+1)]
    max=sorted(numbers,reverse=True)
    n=0
    count=int("".join(sorted(numbers)))-1
    while n<1000000:
        num = str("0"*(len(numbers)-len(str(count))))+str(count)
        if set([x for x in str(num)]) == set(numbers) and len(num)==len(numbers):
            n+=1
            print(n,count)
            if ([x for x in str(num)]==max):
                break
        count+=1
    return count,n
print(permutations(9))
stop = timeit.default_timer()

print('Time: ', stop - start)  