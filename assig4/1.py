from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        raise "Animal makes a sound"


class Dog(Animal):
    def make_sound(self):
        return "Dog barks!"


d = Dog("Buddy")
print(d.make_sound())
