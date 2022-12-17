"""This function gives a bool value whether a year is leap or not"""
def leap_year (year: int):
    year_is_leap = False
    if year % 4 == 0:
        year_is_leap = True
    # if its divisible by both 100 and 400 its leap
    if year % 100 == 0 and year % 400 == 0:
        year_is_leap = True
    # if its divisible by 100 but not 400 its not. This statement is necessary because the bool
    # variable could change to true in year % 4 when the year is not leap
    elif year % 100 == 0 and year % 400 != 0:
        year_is_leap = False

    # returns a bool value True if its leap, false if its not
    return year_is_leap


def days_in_month (month: int, year:int):
    """Check for leap year and for the second month, if it`s the case, just return its values"""
    if month == 2 and (leap_year(year)):
        days = 29
        return days
    elif month == 2:
        days = 28
        return days
    """If the year is not leap"""
    if month % 2 == 0:
        days = 30
    else:
        days = 31
    return days


year_global = int(input("Enter an int value for the year: "))
month_global = int(input("Enter an int value for the month: "))
print("The days in the month are: ", days_in_month(month_global,year_global))