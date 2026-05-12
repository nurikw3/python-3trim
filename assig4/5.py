class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height


circle = Circle(5)
rectangle = Rectangle(5, 5)

print(circle.area())
print(rectangle.area())
