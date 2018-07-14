#Parent class

class Dogs:


    #class Attributes
    species = 'mammal'

    # Initializer / Instance attribures
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Instance method
    def speak(self, sound):
        return '{} says {}'.format(self.name, self.sound)


#Child class (inherits from Dog() class
class RussellTerrier(Dogs):
    def run (self, speed):
        return "{} runs {}".format(self.name, self.speed)



# Child class (inherits from Dog() class)
class BullDog(Dogs):
    def run(self,speed):
        return "{} runs {}".format(self.name, speed)

#Child classes inherit attributes and behavior from the Parent class    // Jim runs fast
jim = BullDog("Jim",23)
print(jim.run('fast'))


# Child classes have specific attributes and behavior as well   // Jim runs slowly
print(jim.run('slowly'))


# Is jim an instance of Dog()?    // True
print(isinstance(jim,Dogs))

# Id julie is instance of Dog()?  // True
julie = Dogs("Julie", 100)
print(isinstance(julie, Dogs))

# Is Johnny walker an instance of Bulldog   // True
johnnywalker = RussellTerrier("Johnny Walker",4)
print(isinstance(johnnywalker, RussellTerrier))
