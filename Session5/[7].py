class Rectangle:
    def __init__(self, w, h):
        self.height = h
        self.width = w
    def print_w_h(self):
        print("w: ",self.width)
        print("h: ",self.height)
    def area(self):
        print(self.width * self.height)

a = Rectangle(10,20)
a.print_w_h()
a.area()