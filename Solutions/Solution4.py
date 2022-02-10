# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def PalindromeCheck(n):
    for index in range(len(str(n))//2):
        if str(n)[index] != str(n)[len(str(n))-1-index]:
            return False
    return True
def LargestPalindromeFromTwoNDigitNumbers(digitcount=3):
    largest=10**(digitcount)-1
    palindromes=[]
    for num1 in range(largest-(10**(digitcount-1))+1):
        num1=largest-(num1)
        for num2 in range(largest - (10 ** (digitcount - 1)) + 1):
            num2 =largest-(num2)
            if  PalindromeCheck(num1*num2):
                palindromes.append(num1*num2)
    return max(palindromes)
print(LargestPalindromeFromTwoNDigitNumbers())

