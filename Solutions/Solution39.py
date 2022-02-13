# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p ≤ 1000, is the number of solutions maximized?

from math import comb
import timeit

start = timeit.default_timer()

def formula():
    import math
    solMax=0
    solPMax=0
    for p in range(0,1001):
        solutions=[]
        for i in range(1,p):
            for j in range(1,p):
                if p==(i+j+math.sqrt(i**2+j**2)):
                    solutions.append((i,j,math.sqrt(i**2+j**2)))
        if len(solutions)>solMax:
            solMax=len(solutions)
            solPMax=p
    return solPMax
print(formula())
stop = timeit.default_timer()

print('Time: ', stop - start)  