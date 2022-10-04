from importlib_metadata import re


def leap_year(year):
    '''
    This functions takes in a year and determines if it is a leap year or not.
    '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_months(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,31,31]
    is_leap_year = leap_year()
    if month > 12 or month < 12:
        return "Invalid argument for month"
    if is_leap_year:
        month_days[1] = 29
    days = month_days[month - 1]
    return days



month = int(input("Enter the month:\n"))
year = int(input("Enter the year:\n"))
days = days_in_months(year, month)
print(days)