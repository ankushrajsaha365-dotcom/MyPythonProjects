# Rectangle

# Constructor: length, breadth
# Method: area
# Method: perimeter


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))

rect = Rectangle(length, breadth)

print("Area:", rect.area(), "square units")
print("Perimeter:", rect.perimeter(), "units")
