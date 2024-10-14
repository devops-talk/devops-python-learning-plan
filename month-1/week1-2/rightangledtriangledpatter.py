# 20. Print a Triangle Pattern
# Description: Write a program that prints a right-angled triangle pattern of stars (*), with the number of rows specified by the user.
# Objective: Practice nested loops.



n=int(input("enter number of lines of for right angled star pattern triangle: ").strip())
i=1
while i<=n:
    j=1
    while j<=i:
        print("*", end='')
        j+=1
    print("")
    i+=1

