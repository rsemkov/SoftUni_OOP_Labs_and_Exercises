from typing import List
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    @property
    def make_sound(self):
        return "meow"


class Dog(Animal):
    @property
    def make_sound(self):
        return "woof-woof"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)


tom = Cat("Tom")
spike = Dog("Spike")
print(tom.make_sound)
print(spike.make_sound)




# Refactor the provided code, so you do not need to make ANY changes to it when you want to add new species to the animals' list
