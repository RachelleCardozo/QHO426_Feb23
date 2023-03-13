#Declare empty list
bleh = []
meh = list()
#Declare a non-empty list
yummy = ["Chicken", "Ice Cream", "Chocolate", "Chips"]
#Print entire list
print(yummy)
#Print a single item
print(yummy[-2])
#Print some items
print(yummy[1:3])
#Add elements to our list (expand it) - adding at the end of the list
print(bleh)
bleh.append("Marmite")
bleh.append("Anchioves")
bleh.append("Carrot")
bleh.append("Liver")
bleh.append("Tomato")
print(bleh)
yummy.append("Pierogi")
print(yummy)
#Add multiple items to a list
n = int(input("How many items to add: "))
for i in range(n):
    bleh.append(input("Enter horrible food: "))
print(bleh)
bleh.extend(["Horse Meat", "Pancakes"])
print(bleh)
#Insert items at specific positions on the list
bleh.insert(1, "Cabbage")
print(bleh)
bleh.insert(4, "Onions")
print(bleh)
#Remove item from the list
bleh.remove("Carrot")
bleh.remove("Tato")
print(bleh)