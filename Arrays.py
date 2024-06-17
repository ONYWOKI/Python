class Animal:
    """A generic animal"""
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    """A dog, a sub-class of Animal"""
    def bark(self):
        print("Woof!")

fido = Dog("Fido")
fido.bark() # prints "Woof!"
