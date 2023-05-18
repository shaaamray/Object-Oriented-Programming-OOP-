class Animal: # parent class
    def __init__(self, name):
        self.name = name

    def voice(self):
        pass

class Cat(Animal): #child class 1
    def voice(self):
        return "Meow"

myCat = Cat("Ziu");

print(myCat.name)
print(myCat.voice())

#child classes can access attributes and methods of the parent classes