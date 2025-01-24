'''
File: weekday_calculator.py
Authors: Jun/Xiang/Ziming/Weijian(David)
Date: 2025-01-17
Class: CS_5002, Spring_2025
Description: 
The program calculates the weekday of a given date.
'''


def month_day_count(target_month,leap = 0):
    """
    Figure out the days in the target month
    input: target_month==>int, leap(1/0)
    output: days==>int
    """
    target_month = int(target_month)
    leap = int(leap)
    days = 0
    while target_month > 0:
            if target_month == "Jan" or target_month == 1 or target_month == "January":
                days = days + 31
                target_month = target_month -1

            elif (
                target_month == "Feb" or target_month == 2 or 
                target_month == "February"
            ):
                if leap == 1:
                    days = days + 29
                    target_month = target_month -1
                else:
                    days = days + 28
                    target_month = target_month -1
            elif target_month == "Mar" or target_month == 3 or target_month == "March":
                days = days + 31
                target_month = target_month -1
            elif target_month == "Apr" or target_month == 4 or target_month == "April":
                days = days + 30
                target_month = target_month -1
            elif target_month == "May" or target_month == 5 or target_month == "May":
                days = days + 31
                target_month = target_month -1
            elif target_month == "Jun" or target_month == 6 or target_month == "June":
                days = days + 30
                target_month = target_month -1
            elif target_month == "Jul" or target_month == 7 or target_month == "July":
                days = days + 31
                target_month = target_month -1
            elif target_month == "Aug" or target_month == 8 or target_month == "August":
                days = days + 31
                target_month = target_month -1
            elif (
                target_month == "Sep" or target_month == 9 or 
                target_month == "September"
            ):
                days = days + 30
                target_month = target_month -1
            elif (
                target_month == "Oct" or target_month == 10 or 
                target_month == "October"
            ):
                days = days + 31
                target_month = target_month -1
            elif (
                target_month == "Nov" or target_month == 11 or 
                target_month == "November"
            ):
                days = days + 30
                target_month = target_month -1
            elif (
                target_month == "Dec" or target_month == 12 or 
                target_month == "December"
            ):
                days = days + 31
                target_month = target_month -1
            else:
                print(f"Please enter a valid month.    {target_month}")
                break
    return days


def days_in_year(target_date_4, leap = 0):
    """
    Figure out the days in the target year
    inut: target_date_4==>str, leap==>int
    output: days==>int
    Days in the year is 32

    >>> days_in_year("0201",0) 
    32
    >>> days_in_year("0228",0) 
    59
    >>> days_in_year("1231",0) 
    365

    """
    target_month = int(target_date_4[:2])
    target_date_days = int(target_date_4[-2:])
    target_month_days = month_day_count(target_month - 1, leap)
    #print(f"Days in the year is {target_month_days + target_date_days}")
    return target_month_days + target_date_days


def is_leap(target_year):
    """
    Figure out if the year is a leap year
    inut: target_date_4==>int/str
    output: 1/0 ==>int
    """
    target_year = int(target_year)
    if target_year % 400 == 0:
        return 1
    elif target_year % 100 == 0:
        return 0
    elif target_year % 4 == 0:
        return 1
    else:
        return 0


def Counting_years(target_year, base_year = 2025):
    """
    Figure out the number of leap years and non-leap years between the target year and the base year
    input: target_year==>int/str, base_year==>int/str
    output: non_leap_year, leap_year ==>int, direction==>int
    """
    base_year = int(base_year)
    target_year = int(target_year)
    non_leap_year = 0
    leap_year = 0
    if target_year < base_year:
        direction = 1
    else:
        direction = -1
    while (base_year - target_year):
        if is_leap(target_year) == 1:
            leap_year = leap_year + 1
            if target_year < base_year:
                target_year = target_year + 1
            else:
                target_year = target_year - 1
        else:
            non_leap_year = non_leap_year + 1
            if target_year < base_year:
                target_year = target_year + 1
            else:
                target_year = target_year - 1
    return non_leap_year, leap_year, direction


def counting_days(target_date):
    """
    Figure out the number of days between the target date and the base date
    """
    BASE_DATE = "20250101"
    target_date = str(target_date)
    target_year = target_date[:4]
    target_date_4 = target_date[-4:]
    leap = is_leap(target_year)
    non_leap_year, leap_year, direction = Counting_years(target_year)
    days_years = non_leap_year * 365 + leap_year * 366
    days_inyear = days_in_year(target_date_4, leap)
    
    if direction == 1:
        return (days_years - (days_inyear-1))*(-1)
    else:
        return days_years + (days_inyear-1)


def main(year, month, day):
    """
    Calculate the weekday of the target date
    input: year==>int, month==>int, day==>int
    output: weekday==>int

    >>> main(2025,1,1)
    Wednesday
    2
    >>> main(2025,1,5)
    Sunday
    6
    >>> main(2024,12,28)
    Saturday
    5

    """
    #we use 0 to 6 to represent Monday to Sunday
    BASE_WEEKDAY = 2
    #20250101 is Wed
    month = str(month)
    month = month.zfill(2)
    day = str(day)
    day = day.zfill(2)
    target_date = str(year) + str(month) + str(day)
    counting_day = counting_days(target_date)
    print(f"The counting day is {counting_day}")
    weekday = (counting_day + BASE_WEEKDAY) % 7
    if weekday == 0:
        print("Monday")
    elif weekday == 1:
        print("Tuesday")
    elif weekday == 2:
        print("Wednesday")
    elif weekday == 3:
        print("Thursday")
    elif weekday == 4:
        print("Friday")
    elif weekday == 5:
        print("Saturday")
    else:
        print("Sunday")
    return weekday


def curry(f):
    """
    >>> a = curry(main)
    >>> a(2020)(1)(1)
    Wednesday
    2
    >>> a(2000)(1)(1) 
    Saturday
    5
    >>> a        
    <function curry.<locals>.year at 0x000001C95C8B0220>
    >>> a_2000 = a(2000) 
    >>> a
    <function curry.<locals>.year at 0x000001C95C8B0220>
    >>> a_2000          
    <function curry.<locals>.year.<locals>.month at 0x000001C95C8B0360>
    >>> a_2000(12)(1)
    Friday
    4
    """
    def year(year):
        def month(month):
            def day(day):
                return f(year, month, day)
            return day
        return month
    return year

curry2 = lambda f: lambda year: lambda month: lambda day: f(year, month, day)
# curry2(main)(2020)(1)(1)
# this function is the same as the curry function


if __name__ == "__main__":
    main(2003,12,28)
    # doctect for the main function
    #import doctest 
    #doctest.testmod(verbose=True)