class Shape:
    def __init__(self, Scolour, Slength, Swidth):
        self.colour = Scolour
        self.length = Slength
        self.width = Swidth
        self.area = Swidth * Slength
    
    def show_area(self):
        print(f"Area of the shape is {self.area}")
    
    def show_colour(self):
        print(f"Colour of the shape is {self.colour}")

    def ret_area(self):
        return self.area


shape1 = Shape("blue", 6, 7)
shape1.show_colour()
shape1.show_area()
print(f"Area of the shape is {shape1.ret_area()}")
