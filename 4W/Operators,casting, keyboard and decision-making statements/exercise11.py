# ask for current year in order to change verb tense
current_year = int(input("Enter current year: "))
# input the year you want to know information of
year = int(input("Enter year. "))
# declare a bool false variable for the possibility of leap year
# the variable is false, meaning that if it doesn´t change into true, the year is seen
# automatically as not leap
year_is_leap = bool(False)
# declare a variable named verb_tense that changes depending of the relation of the years
# inputted in order to output the correct tense
verb_tense = str()
if current_year < year:
    verb_tense = "will be"
if current_year > year:
    verb_tense = "was"
if current_year == year:
    verb_tense = "is"

# check for the conditions for a year to be leap, if its divisible by 4,the year
# is leap unless its divisible by 100 and not 400
if year % 4 == 0:
    year_is_leap = True
# if its divisible by both 100 and 400 its leap
if year % 100 == 0 and year % 400 == 0:
    year_is_leap = True
# if its divisible by 100 but not 400 its not. This statement is necessary because the bool
# variable could change to true in year % 4 when the year is not leap
elif year % 100 == 0 and year % 400 != 0:
    year_is_leap = False

# check the variable for true or false and output the correct verb tense

if year_is_leap:
    print(year, verb_tense, "a leap year")

if not year_is_leap:
    print(year, verb_tense, "not a leap year")
