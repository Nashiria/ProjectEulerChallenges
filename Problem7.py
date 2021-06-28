# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10 001st prime number?

def PrimeCheck(n=10):
    for num in range(n-2):
        num+=2
        if n%num==0:
            return False
    return True
def nThPrime(n=10001):
    count=0
    num=1
    while count!=n:
        num += 1
        if PrimeCheck(num):
            count+=1
    return num
print(nThPrime())
