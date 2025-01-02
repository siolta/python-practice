class Shape():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def what_am_i(self):
        return "I am a shape"


class Rectangle(Shape):
    def calculate_perimeter(self):
        return self.width * self.length


class Square(Shape):
    def __init__(self, width):
        self.length = width
        self.width = width

    def calculate_perimeter(self):
        return self.width * self.length

    def change_size(self, decrement):
        self.width += decrement
        self.length += decrement


rect = Rectangle(7, 8)
sqr = Square(7)

print(rect.calculate_perimeter())
print(sqr.calculate_perimeter())
print(f"Square width is: {sqr.width}")
sqr.change_size(-1)
print(f"Square width is: {sqr.width}")
print(f"rect is a : {rect.what_am_i()}")
print(f"sqr is a : {sqr.what_am_i()}")


class Horse():
    def __init__(self, rider, name, breed):
        self.rider = rider
        self.name = name
        self.breed = breed


class Rider():
    def __init__(self, name):
        self.name = name


hersy_rider = Rider("Thomas")
horsey = Horse(hersy_rider, "Hersy", "Staffordsher")
print(f"Horse is a {horsey.breed}, named {
      horsey.name} ridden by {horsey.rider.name}")
