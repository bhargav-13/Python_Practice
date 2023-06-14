class Animal:

    alive = True
    name = ""
    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

class Rabbit(Animal):
    name = "Rabbit"

class Fish(Animal):
    name = "Fish"

class Cow(Animal):
    name = "Cow"

rabbit = Rabbit()
fish = Fish()
cow = Cow()

print(rabbit.alive)

fish.eat()
cow.sleep()