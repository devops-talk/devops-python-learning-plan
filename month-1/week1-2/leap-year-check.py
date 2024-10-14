# 17. Leap Year Check
# Description: Create a program that checks if a given year is a leap year.
# Objective: Practice if-else conditions with multiple criteria.

year=int(input("enter a year: ").strip())
print(f"let's check {year} is leap year or not")
if year%4==0 and (year%100!=0 or year%400==0):
                  print(f"{year} is leap year")

else:
    print("It's not !!")