#!/usr/bin/env python3.6

def leapYear(year):
    year = abs(int(year))
    if (year % 400) == 0 or (year % 100 != 0 and year % 4 == 0):
        return (True)
    else:
        return (False)

if __name__  == '__main__':
    year = input("Type a year to find out weather it is a leap year: ")
    print('You typed', year)
    if (leapYear(year) == True):
        print("Year", year, "is a leap year")
    else:
        print("Year", year, "is not a leap year")

