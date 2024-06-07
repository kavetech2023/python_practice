# Duck typing = Concept where the class of an object is less important than the methods/attributes
#               classtype is not checked if minimum methods/attributes are present.
#               "If it walks like a duck, and it quacks like a duck then it is a duck"

class Mazda:

    
    def go(self):
        print("mazda is going")

    def stop(self):
        pprint("mazda has stopped")

class Bmw:

    def go(self):
        print("Bmw has started")

    def stop(self):
        pass

class Motorcycle:
    def move(self, bmw):
        bmw.stop()
        bmw.go()
        print("Now we are moving")


mazda = Mazda()
bmw = Bmw()
motorcycle = Motorcycle()

motorcycle.move(bmw) # Here i passed a CLASS as an argument