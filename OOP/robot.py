from inhabitant import Inhabitant

class Robot(Inhabitant):
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0, energy=0):
        super().__init__(name, age, energy)

    def __str__(self):
        return f"{self.name} of age {self.age} has {self.energy} energy."

    def __repr__(self):
        return f"Robot(name={self.name}, age= {self.age}, energy={self.energy})"




if __name__ == "__main__":
    r = Robot("Walle",12, 88 )
    r.display()
    print(r)
    print(repr(r))
