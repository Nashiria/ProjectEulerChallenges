# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
def PrimeCheck(n=10):
    for num in range(n-2):
        num+=2
        if n%num==0:
            return False
    return True
def SumOfPrimesBelowN(n=2000000):
    sum=0
    for num in range(n-1):
        if PrimeCheck(num+2):
            sum+=num+2
    return sum
print(SumOfPrimesBelowN())