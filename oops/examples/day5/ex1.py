class Shape:
    def calculate_area(self):
        print("Area calculation not defined.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print("Circle Area:", area)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Rectangle Area:", area)


# Creating objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Polymorphism in action
circle.calculate_area()
rectangle.calculate_area()
