from human import Human
from robot import Robot

class Planet:
    def __init__(self):
        self.inhabitants = {"Humans":[], "Robots":[]}

    def __str__(self):
        return f"This planet contains \nhumans: {self.inhabitants['Humans']}\nrobots: {self.inhabitants['Robots']}"

    def __repr__(self):
        return f"Planet(humans = {self.inhabitants['Humans']}, robots = {self.inhabitants['Robots']})"


    def add(self, inh):
        if isinstance(inh, Human):
            self.inhabitants["Humans"].append(inh)
        elif isinstance(inh, Robot):
            self.inhabitants["Robots"].append(inh)

    def remove(self, inh):
        if isinstance(inh, Human):
            if inh in self.inhabitants["Humans"]:
                self.inhabitants["Humans"].remove(inh)
        elif isinstance(inh, Robot):
            if inh in self.inhabitants["Robots"]:
                self.inhabitants["Robots"].remove(inh)

if __name__ == "__main__":
    h1 = Human()
    h2 = Human()
    r1 = Robot()
    r2 = Robot()
    r3 = Robot()
    earth = Planet()
    earth.add_human(h2)
    earth.add_robot(r1)
    print(earth)
    print("-"*20)
    earth.add_human(h1)
    earth.add_robot(r3)
    print(earth)
    print("-" * 20)
    earth.add_robot(r2)
    earth.remove_robot(r3)
    print(earth)

