# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?
def PrimeCheck(n=10):
    if n == 1:return False
    i = 2
    while n>=i*i:
        if n % i == 0:return False
        i += 1
    return True
def permutations(maximum):
    pass
  

def circulasPrime(maximum=1000000):
    count=0
    for num in range(maximum):
        if PrimeCheck(num):
            print(permutations(num),num)
            if permutations(num)==1:
                count+=1
    return count
print(circulasPrime())