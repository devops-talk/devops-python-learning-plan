# 1. Basic Class and Object
# Problem: Create a class Car with attributes like make, model, and year. Add methods to:
# Print car details.
# Check if the car is old (older than 10 years).
# Objective: Understand basic class structure, attributes, and methods.

class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def print_details(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
    def is_old(self):
        current_year = 2024  # Let's assume the current year is 2024
        if current_year - self.year > 10:
            print("The car is old.")
        else:
            print("The car is not old.")


my_car = Car("Toyota", "Camry", 2012)


my_car.print_details()


my_car.is_old()