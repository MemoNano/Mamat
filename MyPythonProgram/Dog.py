class Dog:
    species = 'mammal'

    def __init__ (self, name, age):
        self.name = name
        self.age = age


philo = Dog("Philo", 5)
mikey = Dog('Mikey' ,6)

print("{} is {} and  {}.".format(philo.name, philo.age, mikey.name, mikey.age))

"Id Philo a mammal ?"
if philo.species == 'mamal':
    print("{0} is a {1}!".format(philo.name, philo.species))

kashka = Dog('Kashka', 25)
markiza = Dog("Markiza", 15)
akDosh = Dog('AkDosh', 60)

def get_biggest_number(*args):
    if kashka.age > markiza.age and kashka.age > akDosh.age:
        return kashka.age
    elif markiza.age > kashka.age and markiza.age > akDosh.age:
        return markiza.age
    else:
        return akDosh.age

# This print only prints out 60
print(get_biggest_number('The oldest dog is {} year old .'.format(markiza.age,kashka.age, akDosh.age)))


# This print prints message and age of the dog
print('The oldest dog is {} years old'.format(get_biggest_number(kashka.age,markiza.age,akDosh.age)))




# Instance Method
def description(self):
    return '{} says {}'.format(self.age)