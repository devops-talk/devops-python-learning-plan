# Polymorphism
# Problem: Implement two classes, Dog and Cat, each with a make_sound() method that prints the respective sound the animal makes. Write a function that accepts objects of either class and calls make_sound().
# Objective: Practice polymorphism by overriding methods in different classes.


class Dog:
    def make_sound(self):
        print("Woof! Woof!")


class Cat:
    def make_sound(self):
        print("Meow! Meow!")


def animal_sound(animal):
    animal.make_sound()


my_dog = Dog()
my_cat = Cat()

animal_sound(my_dog) 
animal_sound(my_cat) 
