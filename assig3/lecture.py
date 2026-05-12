"""
Task:
Create a class called Point.
Attributes:
x
y
Methods:
translate(dx, dy)
__str__()
The method translate(dx, dy) should change the coordinates of the point.
The method __str__() should return the point in this format:
(x, y)
Example:
p1 = Point(2, 3)
print(p1)

p1.translate(5, -1)
print(p1)
Example output:
(2, 3)
(7, 2)
"""
from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(frozen=False, order=True)
class Point:
    x: int = field(compare=True,default_factory=int)
    y: int = field(compare=True,default_factory=int)

    def __post_init__(self):
        if not isinstance(self.x, int):
            raise ValueError("x must be an integer")
        if not isinstance(self.y, int):
            raise ValueError("y must be an integer")
        
    def translate(self, dx: int, dy: int) -> Point:
        self.x += dx
        self.y += dy
        return self
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x 
    

p1 = Point(2, 3)
print(p1)

p1.translate(5, -1)

p2 = Point(7, 2)
print(p1 == p2)
print(p1)

print(__import__('sys').version)

from collections import namedtuple
Point2 = namedtuple('Point2', ['x', 'y'])
Point2.__str__ = lambda self: f"({self.x}, {self.y})"
Point2.translate = lambda self, dx, dy: Point2(self.x + dx, self.y + dy)
# class MutablePoint2(Point2):
#     def translate(self, dx: int, dy: int) -> MutablePoint2:
#         return MutablePoint2(self.x + dx, self.y + dy)

p3 = Point2(2, 3)
print(p3)
p4 = p3.translate(5, -1)
print(p4)

