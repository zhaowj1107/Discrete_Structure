'''
this program will solve the Calendar Problem! 
three variables (Year, Month, Day)
output the correct day of the week 
Author: David Zhao
Date: 2025-01-13

'''
from datetime import datetime

def counting_days_shortcut(target_date):
    # This is the shortcut way to calculate the days between two dates
    base_date = "20250101"
    target_date = str(target_date)
    target_date = datetime.strptime(target_date, "%Y%m%d")
    base_date = datetime.strptime(base_date, "%Y%m%d")
    #print(target_date - base_date)
    #print((target_date - base_date).days)
    return (target_date - base_date).days

def main(target_date):
    """
    >>> main(20250101)
    2
    >>> main(20250105)
    6
    >>> main(20241228)
    5    
    """
    #we use 0 to 6 to represent Monday to Sunday
    BASE_WEEKDAY = 2
    #20250101 is Wed
    counting_day = counting_days_shortcut(target_date)
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

"""
if __name__ == "__main__":
    import doctest 
    doctest.testmod(verbose=True)
"""