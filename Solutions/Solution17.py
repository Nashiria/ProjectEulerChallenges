# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
import timeit

start = timeit.default_timer()

def numberToWord(number):
    oneDigit=["","one","two","three","four","five","six","seven","eight","nine"]
    twoDigit=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tenDigit=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    hundredDigit=["hundred","thousand"]
    if len(str(number))<2:
        return (oneDigit[number])
    elif len(str(number))==2 and number<20:
        return (twoDigit[number-10])
    elif len(str(number))==2:
        return (tenDigit[int(str(number)[0])-2])+(oneDigit[int(str(number)[1])])
    elif len(str(number))==3:
        stxr=(oneDigit[int(str(number)[0])])+(hundredDigit[0])+"and"+(numberToWord(int(str(number)[1:])))
        if stxr[-3:]=="and":
            stxr=stxr[:-3]
        return stxr
    elif len(str(number))==4:
        return (oneDigit[int(str(number)[0])])+(hundredDigit[1])
n=0
num1=[]
for i in range(1,1001):
    num1.append([numberToWord(i),len(numberToWord(i))])
    n+=len(numberToWord(i))
print(n)
stop = timeit.default_timer()

print('Time: ', stop - start)  