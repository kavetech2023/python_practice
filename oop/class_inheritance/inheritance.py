class Animal:
    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.eat()
fish.sleep()
hawk.run()