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
    def __init__(self, model, carid, carpaint):
        self.model = model  # Add this line
        self.carid = carid
        self.carpaint = carpaint

    def carpainttype(self):
        if self.carpaint == "red":
            print("the car is red")    

car = Carmodel(model="mazda", carid=1, carpaint="red")
print(car.model)  # This should now print "mazda"
car.carpainttype()
             
