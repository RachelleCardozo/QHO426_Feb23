class Human:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def __str__(self):
        return f"{self.name} of age {self.age} has {self.energy} energy."

    def __repr__(self):
        return f"Human(name={self.name}, age= {self.age}, energy={self.energy})"

    def display(self):
        print(f"I am {self.name}.")

    def grow(self):
        self.age += 1

    def eat(self,amount):
        self.energy += amount
        if self.energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY

    def move(self, distance):
        self.energy -= distance
        if self.energy < 0:
            self.energy = 0



if __name__ == "__main__":
    h = Human()
    h.display()
    print(h)
    print(repr(h))
    h.move(55)
    h.eat(28)
    for i in range(4):
        h.grow()
    print(h)
