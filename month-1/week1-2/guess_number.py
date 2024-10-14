# 19. Number Guessing Game
# Description: Develop a simple number guessing game where the user has to guess a number between 1 and 100. The program should give hints if the guess is too high or too low.
# Objective: Combine loops, conditional logic, and random number generation.
import random

random_number = random.randint(1, 100)

print("Hey! let's see if you are able to guess number! inital hint it is between 1-100")


user_input=int(input("my input:").strip())
count=1
if user_input<101:
    while user_input!=random_number:
        if user_input<random_number:
            print("guess is low")
        elif user_input>random_number:
            print("guess is high")
        user_input=int(input("my input:").strip())
        count+=1




print("good job its a match")
print(f"you took {count} attempt in guessing")

