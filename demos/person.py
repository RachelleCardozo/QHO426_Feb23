#the class #person which is blueprint for my objects to store info abt humans/people
class Person:
    #class attribute is an attribute or a feature acessible/applied to every object of the class
    MAX_W = 200


    #static method = utility function, that does not require an object to work on
    def is_mature(age):
        if age >= 25:
            return "Person is mature."
        else:
            return  "Person is immature."

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
     # magic method str provides "informal" representation of object via string
    #it is invoked auto when when obj goes into print()
    #doesnot take any para except self
    def __str__(self):
        return f"{self.name} is {self.age} years old. They work as {self.job} and weight {self.weight}."
    # magic method repr provides formal representation of an obj
    #thats how u want to store ur obj for later
    def __repr__(self):
        return f"Person(name={self.name}, age= {self.age}, job= {self.job}, w={self.weight})"
    #methos = function attached to a specific data type(class)
    #Instance Method = it applies to a specific instance of a class(object)
    def eat(self, food, w):
        print (f"{self.name} have eaten {food}")
        self.weight += w
        print(f"{self.name} now weights {self.weight:.2f} KG")

    def exercise(self, burned):
        self.weight-= burned
        print(f"{self.name} has exercised and now weights {self.weight:.2f} KG.")

# to avoid running the below part when this file is imported in another file
if __name__ == "__main__":
    p1 = Person("Luke", 23, "Clerk", 55)
    p2 = Person("Mary", 19, "Waitress", 48)
    p3 = Person("Udoh", job="Headmaster")
    p4 = Person("Olu", w=600)

    # print(f"Person 1 is called {p1.name} and person 2 is called {p2.name}")
    # print(f"Together their total weight is {p1.weight + p2.weight}")
    print(p1)
    print(p2)
    # print(f"{p4.name} weights {p4.weight}")
    # print(f"{p3.name} weights {p3.weight} and works as {p3.job}")

    p1.eat("lasagna", 1.2)
    p1.exercise(0.4)
    p1.eat("sandwich", 0.2)
    print(repr(p3))

    print(Person.is_mature(18))
    print(Person.is_mature(55))
    print(Person.is_mature(p2.age))


