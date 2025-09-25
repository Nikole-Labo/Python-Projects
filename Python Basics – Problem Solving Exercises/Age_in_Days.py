"""Determine the age of a person, in number of days. Take into account leap years,
as well as the date of birth and current date (year, month, day). Do not use Python's inbuilt date/time functions."""


def findAge(year, month, day, currentYear, currentMonth, currentDay):
    numberOfDays = 0

    if month in [2, 4, 6, 9, 11] :
        if(day > 30):
            print("Invalid day for that month!")
            return
    if(month == 2 and year % 4 == 0):
        if(day > 29):
            print("Invalid day for that month!")
            return
    if(month == 2 and day > 28):
        print("Invalid day for that month!")
        return



    if currentMonth in [2, 4, 6, 9, 11]:
        if (currentDay > 30):
            print("Invalid day for that month!")
            return
    if (currentMonth == 2 and currentYear % 4 == 0):
        if (currentDay > 29):
            print("Invalid day for that month!")
            return
    if (currentMonth == 2 and currentDay > 28):
        print("Invalid day for that month!")
        return

    while month < 13:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            numberOfDays = 31 - day
            month += 1
            day = 0
        else:
            if month in [4, 6, 9, 11]:
                numberOfDays = 30 -day
                month += 1
                day = 0
            else:
                if month == 2 and year % 4 == 0:
                    numberOfDays = 29 - day
                    month += 1
                    day = 0
                else:
                    numberOfDays = 28 - day
                    month += 1
                    day = 0

    year +=1
    month = 1
    while year < currentYear:
        if year % 4 == 0:
            numberOfDays += 366
            year += 1
        else:
            numberOfDays += 365
            year += 1


    while month < currentMonth:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            numberOfDays += 31
            month += 1
        else:
            if month in [4, 6, 9, 11]:
                numberOfDays += 30
                month += 1
            else:
                if month == 2 and year % 4 == 0:
                    numberOfDays += 29
                    month += 1
                else:
                    numberOfDays += 28
                    month += 1


    numberOfDays += currentDay
    return numberOfDays



def main():
    print("give the date of birth (year/month/day): ")
    year, month, day = map(int, input().split('/'))

    print("\n Give the current date (year/moth/day): ")
    currentYear, currentMonth, currentDay = map(int, input().split('/'))

    if(year > 2024 or year < 1900 or currentYear > 2024 or currentYear < 1900):
        print("Invalid year!")
        return
    else:
        if (month < 1 or month > 12 or currentMonth > 12 or currentMonth < 1 ):
            print("Invalid month!")
            return
        else:
            if(day < 1 or day > 31 or currentDay < 1 or currentDay > 31):
                print("Invalid day!")
                return 
            else:
                print("The number of days lived: ", findAge(year, month, day, currentYear, currentMonth, currentDay))

if __name__ == '__main__':
    main()
