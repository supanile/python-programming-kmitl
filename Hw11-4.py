class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Dog(Animal):
    def __init__(self, name, color, leg):
        super().__init__(name, color)
        self.leg = leg
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setLeg(self, leg):
        self.leg = leg

    def getLeg(self):
        return self.leg

name = input("Enter dog's name: ")
color = input("Enter dog's color: ")
legs = int(input("Enter number of legs: "))

dog1 = Dog(name, color, legs)

print("Name:", dog1.getName())
print("Color:", dog1.getColor())
print("Legs:", dog1.getLeg())
#Supawit Sangrattanayon 64050694
