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
    def __init__(self,center: Point2D, radius: int, name: str):
        self.center = center
        self.radius = radius
        self.name = name
    
    def getName(self):
        return self.name

    def getArea(self):
        area = 3.14 * (self.radius**2)
        return area
    
    def getPerimeter(self):
        p = 2 * 3.14 * self.radius
        return p
    
    def __str__(self):
        return f"Circ: C=({self.center}), R={self.radius}"

class Rectangle(Shape):
    def __init__(self, p1: Point2D, p2: Point2D, name:str):
        self.name = name
        self.p1 = p1
        self.p2 = p2

    def getName(self):
        return self.name

    def getArea(self):
        x1 = self.p1.x
        x2 = self.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        l = x2 - x1
        h = y2 - y1
        f = l * h
        return f
    def getPerimeter(self):
        x1 = self.p1.x
        x2 = self.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        l = x2 - x1
        h = y2 - y1
        f = 2 * (l+h)
        return f
    
    def __str__(self):
        return f"Rect: P1=(x1, {}) P2=(x2, y2)"




