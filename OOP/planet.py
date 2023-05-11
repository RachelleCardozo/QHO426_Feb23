from human import Human
from robot import Robot

class Planet:
    def __init__(self):
        self.humans = []
        self.robots = []

    def __str__(self):
        return f"This planet contains \nhumans: {self.humans}\nrobots: {self.robots}"

    def __repr__(self):
        return f"Planet(humans = {self.humans}, robots = {self.robots})"

    def add_human(self, hum):
        self.humans.append(hum)

    def remove_human(self, hum):
        if hum in self.humans:
            self.humans.remove(hum)

    def add_robot(self, rob):
        self.robots.append(rob)

    def remove_robot(self, rob):
        if rob in self.robots:
            self.robots.remove(rob)

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

