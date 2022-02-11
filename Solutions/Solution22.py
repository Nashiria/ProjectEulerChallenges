# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?
import timeit

start = timeit.default_timer()


def getNameScore(name, position):
    return sum([ord(x)-64 for x in name]) * position
def sortedNamesList():
    with open("./Solutions/problemDatas/p022_names.txt", "r") as file:
        names = file.read().replace('"', '').split(',')
        names.sort()
    return names
def allNameScore():
    names = sortedNamesList()
    total = 0
    for i in range(len(names)):
        total += getNameScore(names[i], i+1)
    return total
print(allNameScore())
stop = timeit.default_timer()

print('Time: ', stop - start)  