
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def findMultiplesOfN(n=3,limit=1000):
    tmp=[]
    for num in range(limit-10):
        if(num+10) %n == 0:
            tmp.append(num+10)
    # return tmp for numbers in list
    return sum(tmp)
print(findMultiplesOfN())
