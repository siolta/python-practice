
class Shape():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def what_am_i(self):
        return "I am a shape"


class Rectangle(Shape):
    def calculate_perimeter(self):
        return self.width * self.length

    def what_am_i(self):
        return "I am a Rectangle"


class Square(Shape):
    square_list = []

    def __init__(self, width):
        self.square_list.append(self)
        self.length = width
        self.width = width

    def what_am_i(self):
        return "I am a Square"

    def __repr__(self):
        return f"{self.width} by {self.width} by {self.width} by {self.width}"

    def calculate_perimeter(self):
        return self.width * self.length

    def change_size(self, decrement):
        self.width += decrement
        self.length += decrement


sqr1 = Square(4)
sqr2 = Square(5)
sqr3 = Square(6)

print(Square.square_list)
print(sqr3)


def is_same(obj1, obj2):
    return obj1 is obj2


print(is_same(sqr1, sqr2))
