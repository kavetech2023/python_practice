"""create a function that adds variables together"""
def push_button(param=350):
    w = param
    x = w+2
    y = x+3
    print(y)

push_button(250)  

class Dog():
    def __init__(self, y):
        self.y = y
        

    def chase(self):
        print("hello")
        print(self.y)

dog = Dog(5)       
dog.chase()