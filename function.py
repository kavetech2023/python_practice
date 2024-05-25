"""create a function that adds variables together"""
def push_button(param=350):
    w = param
    x = w+2
    y = x+3
    print(y)

push_button(250)  

class Dog():
    def __init__(self, y, z):
        self.y = y
        self.z = z
        

    def chase(self):
        print("hello")
        print(self.y)
        print(self.z)

dog = Dog(5,6)       
dog.chase()