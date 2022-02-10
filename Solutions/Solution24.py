# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?



def permutations(maximum):
    numbers=[str(x) for x in range(maximum+1)]
    n=1
    lastIndex=len(numbers)-1
    startIndex=0
    currentIndex=0
    combinations=[]
    while n<1000000:
        print(n,numbers)
        n+=1
        if currentIndex==lastIndex:
            startIndex+=1
            currentIndex=startIndex
        if startIndex==lastIndex:
            break
        else:
            combinations.append(numbers)
            numbers[currentIndex],numbers[currentIndex+1]=numbers[currentIndex+1],numbers[currentIndex]
        currentIndex+=1
permutations(2)

