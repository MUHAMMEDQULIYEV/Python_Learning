class Duck:
    def quack(self):
        print("Quack")

    def fly(self):
        print("FLAP,FLAP")


class Person:
    def quack(self):
        print("I 'm quaking like a duck")

    def fly(self):
        print("I 'm flying like a duck")


def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)


d = Duck()
quack_and_fly(d)
p = Person()
quack_and_fly(p)
