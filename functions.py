def puppy():
    print("the word puppy")
    print("Not the word puppy")


puppy()    

def car():
    model = input("Enter car model: ")
    print("Your car model is: " + model)
    print("Would you like to place an order of your "+ model +"?")
    answer = input("Please enter yes or no: ")
    if answer == "yes":
        print("Thanks for placing an order with us. Have a nice day!")
        extras = input("Would you like to check out the extra features?: ")
        if extras == "yes":
            print("Please click the link to check out extra features")    

car()    

# functions.py

class Carmodel:
    def __init__(self, **kwargs):
        self.model = kwargs.get('model', None)  # Default value if 'model' not provided
        self.carid = kwargs.get('carid', None)  # Default value if 'carid' not provided
        self.carpaint = kwargs.get('carpaint', None)  # Default value if 'carpaint' not provided

    def carpainttype(self):
        if self.carpaint == "red":
            print("The car is red")  # Capitalized 'The' for better readability

car = Carmodel(model="mazda", carid=1, carpaint="red")
print(car.model)  # This should now print "mazda"
car.carpainttype()