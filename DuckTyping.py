class Duck:
    def walk(self):
        print("Duck is walking")

    def talk(self):
        print("The duck is Quacking")

class Chicken:
    def walk(self):
        print("chicken is walking")
    def talk(self):
        print("The chicken is clucking")

class Person():

    def catch_a_duck(self, duck):
        duck.walk()
        duck.talk()
        print("You caught!!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch_a_duck(chicken)