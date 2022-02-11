# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import timeit

start = timeit.default_timer()
def PythagoreanTriplet(desiredSum=1000):
    import math
    
    for n1 in range(desiredSum):
        n1=desiredSum-n1
        for n2 in range(desiredSum):
            n2=desiredSum-n2
            n3=int(math.sqrt((n1*n1)+(n2*n2)))
            if n1+n2+n3==desiredSum and n3>n2 and n2>n1 and (n1*n1)+(n2*n2)==n3*n3:
                return (n1*n2*int(math.sqrt((n1*n1)+(n2*n2))))
print(PythagoreanTriplet())

stop = timeit.default_timer()

print('Time: ', stop - start)  
