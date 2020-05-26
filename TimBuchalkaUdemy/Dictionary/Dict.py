class PostalAddress:
    pass


cP1 = PostalAddress()
# Create an Instance for person ABC
cP1.name = "ABC"
cP1.street = "Central Street - 1"

# Create an Instance for person DEF
cP2 = PostalAddress()
cP2.name = "DEF"
cP2.street = "Central Street - 2"

p1 = {'name': "ABC", 'street': "Central Street - 1"}
p2 = {'name': "DEF", 'street': "Central Street - 2"}
p3 = {'name': "AXY", 'street': "Central Street - 1"}

print(cP1.__dict__)
print(p1["name"])
