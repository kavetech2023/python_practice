# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used.  


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)


class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)