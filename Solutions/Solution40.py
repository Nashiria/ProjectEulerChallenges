# An irrational decimal fraction is created by concatenating the positive integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
import timeit

start = timeit.default_timer()

def ChampernowneConstant():
    n=1
    d=0
    for i in range(0,1000000):
       for digit in str(i):
           if d in [1,10,100,1000,10000,100000,1000000]:
                n*=int(digit)
           d+=1
    return n
print(ChampernowneConstant())
stop = timeit.default_timer()

print('Time: ', stop - start)  