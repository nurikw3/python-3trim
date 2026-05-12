class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} can fly"


class Swimmable:
    def swim(self):
        return f"{self.__class__.__name__} can swim"


class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"


d = Duck()
print(d.fly())
print(d.swim())
print(d.quack())
