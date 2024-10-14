# 6. Simple Calculator
# Description: Create a basic calculator that can perform addition, subtraction, multiplication, and division based on user input.
# Objective: Reinforce control structures (if-else statements).

operation = input("Enter the operation (+, -, *, /): ").strip()

num1=int((input("enter first numer: ")).strip())
num2=int((input("enter second numer: ")).strip())
if operation=="+":
    print("sum = " ,num1+num2)
elif operation=="-":
    print("difference= " ,num1-num2)
elif operation=="*":
    print("multiplication= ",num1*num2)
elif operation=="/":
    print("division= " ,int(num1/num2))
elif operation=="%":
    print("quotient= " ,int(num1%num2))
else:
    print("wrong input")