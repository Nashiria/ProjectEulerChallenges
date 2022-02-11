# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
import timeit

start = timeit.default_timer()

def patternFinder(divider):
    num=1
    remainders = []
    remainder=-1
    while remainder not in remainders:
        remainders.append(remainder)
        num *= 10
        remainder = num % divider
    return len(remainders)
    
maxp=0
maxn=0
for n in range(1000):
    p=patternFinder((n+1))-1
    if p>maxp:
        maxp=p
        maxn=n+1
print(maxn,maxp)
stop = timeit.default_timer()

print('Time: ', stop - start)  