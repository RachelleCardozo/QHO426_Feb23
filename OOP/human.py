from inhabitant import Inhabitant

class Human(Inhabitant):
    MAX_ENERGY = 100

    def __init__(self, name ="Human", age=0, energy=MAX_ENERGY):
        super().__init__(name, age, energy)

    def __str__(self):
        return f"{self.name} of age {self.age} has {self.energy} energy."

    def __repr__(self):
        return f"Human(name={self.name}, age= {self.age}, energy={self.energy})"





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
