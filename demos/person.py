#the class #person which is blueprint for my objects to store info abt humans/people
class Person:
    #class attribute is an attribute or a feature acessible/applied to every object of the class
    MAX_W = 200

    #below is the initaliser/constructor -- function that is automatically called when an object is instantiated
    # __ - (magic method)
    #initialiser of ANY class has the same name
    # "DUNDER" - double underscore
    def __init__(self, name, age = 0, job = "", w=100):  # self must be there
        #below are the instance attributes which are features
        self.name = name
        self.age = age
        self.job = job
        if w > Person.MAX_W:
            self.weight = Person.MAX_W
        else:
            self.weight = w


p1 = Person("Luke", 23, "Clerk", 55)
p2 = Person("Mary", 19, "Waitress", 48)
p3 = Person("Udoh", job="Headmaster")
p4 = Person("Olu", w= 600)

print(f"Person 1 is called {p1.name} and person 2 is called {p2.name}")
print(f"Together their total weight is {p1.weight + p2.weight}")
print(p1)
print(p2)
print(f"{p4.name} weights {p4.weight}")
print(f"{p3.name} weights {p3.weight} and works as {p3.job}")
