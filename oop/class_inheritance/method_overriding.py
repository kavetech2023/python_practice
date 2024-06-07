class Animal:
    def eat(self):
        print("This animals is eating")        # 1) Ignores this 

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")# 2) uses this method even though inheritance.

rabbit = Rabbit()
rabbit.eat()