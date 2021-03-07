class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def __str__(self):
        return f"Rectangle {self.get_x(), self.get_y(), self.get_width(), self.get_height()}"


rectangle = Rectangle(5, 10, 50, 100)
print(str(rectangle))
