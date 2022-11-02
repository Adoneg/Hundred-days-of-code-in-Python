
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def reproduce(self):
        print("reproduce")

# creating a class inheritance


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def repro(self):
        super().reproduce()
        print("Kitens are my children")

    def claw(self):
        print("Claws present")


pus = Cat()
pus.repro()