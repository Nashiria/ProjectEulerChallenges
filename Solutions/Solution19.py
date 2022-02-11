# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import timeit

start = timeit.default_timer()

def leapYear(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False
def monthDay(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month==2:
        if leapYear(year):
            return 29
        return 28

day=0
totalDay=-1
month=1
year=1900
sunday=0
while year<2001:
    day+=1
    totalDay+=1
    if monthDay(month,year)<day:
        month+=1
        day=1
    if month==13:
        month=1
        year+=1
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if days[totalDay%7]=="Sunday" and day==1 and year>1900:
        sunday+=1
print(sunday)
stop = timeit.default_timer()

print('Time: ', stop - start)  

