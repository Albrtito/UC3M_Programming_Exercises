# define both variables, base salary is asked in input and final salary is defined but not
# given a value. Seniority is also declared blank
base_salary = float(input("Base salary: "))
final_salary = float()

# first check
if base_salary >= 1000:
    final_salary = base_salary

else:
    # seniority is in years son its an int. It takes whole years
    seniority = int(input("Enter seniority in years: "))
    if seniority >= 10:
        # increase salary to 120% over base salary
        final_salary = base_salary * 1.2
    else:
        # increase salary to 115%
        final_salary = base_salary * 1.15

print("""Final salary of the worker is:
 """, final_salary, """Euros""")
