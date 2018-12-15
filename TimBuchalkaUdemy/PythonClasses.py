class Kattle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kattle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kattle("Hamilton", 14.55)

print("Module: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
