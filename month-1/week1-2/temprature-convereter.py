# 5. Temperature Converter
# Description: Write a program that converts temperature from Celsius to Fahrenheit and vice versa.
# Objective: Practice input/output and basic arithmetic operations.


unit=input("enter the input unit of temprature out of celcius/fahrenheit: ").strip().lower()
temp=int((input("enter the temprature to convert: ")).strip())

if unit=="celcius":
    converted_temp= temp*9/5 + 32
    print(converted_temp)
elif unit=="fahrenheit":
    converted_temp=(temp-32)*5/9
    print(converted_temp)
else:
    print("wrong input")


