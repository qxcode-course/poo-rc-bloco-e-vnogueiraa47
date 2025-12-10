from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x:.2f}:{self.y:.2f})"

class Circle(Shape):
    def __init__(self,center: Point2D, radius: int):
        self.center = center
        self.radius = radius
    
    def getName(self):
        return f"Circ"

    def getArea(self):
        area = 3,14 * (self.radius**2)
        return area
    
    def getPerimeter(self):
        