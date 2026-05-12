class Engine:
    def __init__(self, horsepower):
        self.__horsepower = horsepower

    def show_engine(self, brand):
        print(f"{brand} has engine power: {self.__horsepower} hp")


class Car:
    def __init__(self, brand, engine):
        self.__brand = brand
        self.engine = engine

    def show_info(self):
        self.engine.show_engine(self.__brand)


engine = Engine(300)
car = Car("BMW", engine)

car.show_info()
