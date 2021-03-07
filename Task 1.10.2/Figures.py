class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_area_rectangle(self):
        return self.get_length() * self.get_width()

    def __str__(self):
        return f"Length: {self.get_length()}, Width: {self.get_width()}, Area: {self.get_area_rectangle()}"


rectangle = Rectangle(5, 10)
print(str(rectangle))
