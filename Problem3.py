# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

def PrimeCheck(n=10):
    for num in range(n-2):
        num+=2
        if n%num==0:
            return False
    return True
def LargestPrimeFactor(n=600851475143):
    dividers=[]
    for num in range(n-2):
        num+=2
        if n % num == 0:
            if (num not in dividers) and (n/num) not in dividers:
                dividers.append(num)
                dividers.append(int(n/num))
            else:
                break
    dividers.sort()
    dividers.reverse()
    for div in dividers:
        if PrimeCheck(div):
            return div
print(LargestPrimeFactor())


