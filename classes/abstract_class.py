# Prevents a user from creating an object of that class
# + comples a user to override abstract methods in a child class


from abc import ABC, abstractmethod

class vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):

    @abstractmethod
    def go(self):
        pass

class Motorcycle(Vehicle):
    def go(self):
        print("Driving")

    def stop(self):
        print("Stopped")

