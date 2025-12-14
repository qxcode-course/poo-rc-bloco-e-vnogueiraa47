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
        return f"{self.x:.2f}, {self.y:.2f}"

class Circle(Shape):
    def __init__(self,center: Point2D, radius: int, name: str):
        self.center = center
        self.radius = radius
        self.name = name
    
    def getName(self):
        return self.name

    def getArea(self):
        area = 3.141592 * (self.radius**2)
        return area
    
    def getPerimeter(self):
        p = 2 * 3.141592 * self.radius
        return p
    
    def __str__(self):
        return f"Circ: C=({self.center}), R={self.radius:.2f}"

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
        return f"Rect: P1=({self.p1}) P2=({self.p2})"

def main():
    shapes = []

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        command = args[0]

        if command == "end":
            break

        elif command == "show":
            for s in shapes:
                print(s)

        elif command == "circle":
            x = float(args[1])
            y = float(args[2])
            radius = float(args[3])
            center = Point2D(x, y)
            circ = Circle(center, radius, "Circ")
            shapes.append(circ)
        
        elif command == "rect":
            x1 = float(args[1])
            y1 = float(args[2])
            x2 = float(args[3])
            y2 = float(args[4])
            p1 = Point2D(x1, y1)
            p2 = Point2D(x2, y2)
            rect = Rectangle(p1, p2, "Rect")
            shapes.append(rect)
        
        elif command == "info":
            for s in shapes:
                print(f"{s.getName()}: A={s.getArea():.2f} P={s.getPerimeter():.2f}")

main()

    




