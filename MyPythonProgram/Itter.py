class Itter:


    # Class Attributes
    species = 'mammal'

    #Initializer / Instance Attributes
    def __init__ (self, name, age):
        self.name = name
        self.age = age


    # instance method
    def decription(self):
        return "{} is {} years old".format(self.name, self.age)

    # Instance method
    def speak (self, sound):
        return "{} says {}".format(self.name, sound)

# Instantiate the Itter Object
mikey = Itter("Mikey",6)


# Call our instance methods
print(mikey.decription())
print(mikey.speak('Guff Guff'))