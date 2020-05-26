class ClassesExample:
    """ A simple example class"""

    def __init__(self):
        pass

    def sum1(self, x1, y):
        return x1 + y


print(ClassesExample.__doc__)


class Complex:
    """Complex class example"""

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.214, -9.6)
print(x.r + x.i)
print(x.r, x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)


class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)  # shared by all dogs
print(e.kind)  # shared by all dogs

print(d.name)  # unique to d instance
print(e.name)  # unique to e instance


class Doggy:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # Creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

    print(object.__class__)


dog1 = Doggy('Kashka')
dog2 = Doggy('Akdosh')

dog1.add_trick('roll over')
dog2.add_trick('play dead')

print(dog1.name, dog1.tricks)
print(dog2.name, dog2.tricks)

"  I stop in here --->  9.4. Random Remarks"
